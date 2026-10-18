# -*- coding: utf-8 -*-
"""dr_compare.py — fusion vs. motion-only (dead_reckoning = VIO/IMU alone) on existing F5 results, no rerun.
Per head x scenario, pooled over the 3 training seeds: p95 (whole window and after the first 60 s), % windows
with error > 100 m after 60 s, and the paired p95 difference (method - dead_reckoning) with a bootstrap CI that
resamples whole FLIGHTS (windows of one flight overlap and are not independent).
usage: python dr_compare.py <results prefix, e.g. F5-05_testlong> [n_boot]"""
import glob, json, re, sys
import numpy as np

pre = sys.argv[1]
n_boot = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
SC = ["vio", "imu", "init300", "imuinit300"]
ME = ["dead_reckoning", "ekf_gated", "pf_topk", "mh_ekf"]
SKIP = 60  # s, initial convergence

runs = {}  # (head, scenario) -> list of (errors dict, flight id per window)
for f in sorted(glob.glob(f"results/{pre}_*_s*_*/errors.npz")):
    m = re.search(rf"{pre}_(\w+?)_s(\d+)_(\w+)/errors", f)
    e = np.load(f)
    meta = json.load(open(f.replace("errors.npz", "summary.json")))["meta"]
    runs.setdefault((m.group(1), m.group(3)), []).append(({k: e[k] for k in ME}, np.array([x[0] for x in meta])))


def stats(err):
    late = err[:, SKIP:]
    return np.percentile(err, 95), np.percentile(late, 95), 100 * (late.max(1) > 100).mean()


def boot_diff(rs, a, b, rng):
    """p95(a) - p95(b) pooled over seeds; CI by resampling flights (same flights for every seed)."""
    flights = np.unique(rs[0][1])
    by = [[(e[a][fl == s], e[b][fl == s]) for s in flights] for e, fl in rs]
    def p95diff(sel):
        A = np.concatenate([by[r][i][0] for r in range(len(rs)) for i in sel])
        B = np.concatenate([by[r][i][1] for r in range(len(rs)) for i in sel])
        return np.percentile(A, 95) - np.percentile(B, 95)
    d = p95diff(range(len(flights)))
    bs = [p95diff(rng.integers(0, len(flights), len(flights))) for _ in range(n_boot)]
    return d, np.percentile(bs, [2.5, 97.5]), len(flights)


rng = np.random.default_rng(0)
print(f"## {pre}: fusion vs. dead reckoning (VIO/IMU alone)\n")
print("p95 cả cửa sổ / p95 sau 60 s / % cửa sổ > 100 m sau 60 s (gộp 3 seed train). "
      "Hiệu p95 (mh − DR): CI 95 % bootstrap theo **chuyến bay**.\n")
print("| Head | Kịch bản | " + " | ".join(ME) + " | mh − DR p95 [CI] | n chuyến |")
print("|---" * (len(ME) + 4) + "|")
for h in ("baseline", "lpn", "fsra"):
    for sc in SC:
        rs = runs.get((h, sc))
        if not rs:
            continue
        cell = []
        for k in ME:
            s = np.mean([stats(e[k]) for e, _ in rs], 0)
            cell.append(f"{s[0]:.0f} / {s[1]:.0f} / {s[2]:.1f}")
        d, ci, nf = boot_diff(rs, "mh_ekf", "dead_reckoning", rng)
        sig = "*" if ci[1] < 0 or ci[0] > 0 else ""
        print(f"| {h} | {sc} | " + " | ".join(cell) + f" | {d:+.0f} [{ci[0]:+.0f}, {ci[1]:+.0f}]{sig} | {nf} |")

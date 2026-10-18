# -*- coding: utf-8 -*-
"""aggregate_f6.py — NaviLoc vs MH-EKF.
  val  : python aggregate_f6.py val          -> F6-01 window sweep: mean p95 per (dataset, variant, W), picks W
  test : python aggregate_f6.py test short|long|dense -> NaviLoc (F6-02) merged with the other methods of the same
         runs (F5-04 / F5-05 / F3-09 + F3-08), per head x scenario: p95 mean ± std, wins of mh, % lost
"""
import glob, re, sys
import numpy as np

SC = ["vio", "imu", "init300", "imuinit300"]
NL = ["naviloc", "naviloc_yaw", "naviloc_causal"]


def lost(e, skip):  # % runs with any error > 100 m after the initial convergence
    return 100 * (e[:, skip:] > 100).any(1).mean()


if sys.argv[1] == "val":
    res = {}
    for f in glob.glob("*/results/F6-01_*_W*_*/errors.npz"):
        m = re.search(r"F6-01_(aerialvl|dense)_(\w+?)_W(\d+)_(\w+)/errors", f)
        e = np.load(f)
        for k in NL + ["mh_ekf"]:
            res.setdefault((m.group(1), k, int(m.group(3))), []).append(np.percentile(e[k], 95))
    print("| Dataset | Phương pháp | W = 30 | W = 60 | W = 120 | W chọn |\n|---|---|---|---|---|---|")
    for ds in ("aerialvl", "dense"):
        for k in NL + ["mh_ekf"]:
            v = {W: np.mean(res[(ds, k, W)]) for W in (30, 60, 120) if (ds, k, W) in res}
            n = {W: len(res[(ds, k, W)]) for W in v}
            best = min(v, key=v.get) if k != "mh_ekf" else "—"
            print(f"| {ds} | {k} | " + " | ".join(f"{v[W]:.1f} (n={n[W]})" if W in v else "—" for W in (30, 60, 120))
                  + f" | {best} |")
    sys.exit()

ds = sys.argv[2]  # short | long | dense
# base experiments holding the other methods on the SAME runs; `check` must be bit-identical
BASES = {"short": ("aerialvl", [("F5-04_test", ["dead_reckoning", "ekf_gated", "pf_topk", "mh_ekf"])], "dead_reckoning", 60),
         "long": ("aerialvl", [("F5-05_testlong", ["dead_reckoning", "ekf_gated", "pf_topk", "mh_ekf"])], "dead_reckoning", 60),
         "dense": ("prototype", [("F3-09", ["ekf_gated", "mh_ekf"]), ("F3-08", ["pf_topk"])], "ekf_gated", 30)}
root, bases, check, skip = BASES[ds]
ME = ["dead_reckoning", "ekf_gated", "pf_topk"] + NL + ["mh_ekf"]
cells, bad = {}, []
for f in sorted(glob.glob(f"{root}/results/F6-02_{ds}_*/errors.npz")):
    m = re.search(rf"F6-02_{ds}_((baseline|lpn|fsra)_s\d+_(?:t\d+_)?(vio|imu|init300|imuinit300))/errors", f)
    e = dict(np.load(f))
    ok = True
    for pre, keys in bases:
        b = np.load(f"{root}/results/{pre}_{m.group(1)}/errors.npz")
        if check in b.files and not np.array_equal(b[check], e[check]):
            ok = False
        e.update({k: b[k] for k in keys})
    if not ok:
        bad.append(m.group(1))
        continue
    cells.setdefault((m.group(2), m.group(3)), []).append(
        {k: (np.percentile(e[k], 95), lost(e[k], skip)) for k in ME if k in e})
have = [k for k in ME if all(k in c for cs in cells.values() for c in cs)]
print(f"## F6-02 {ds}: {sum(map(len, cells.values()))} ô ghép được, {len(bad)} ô {check} không trùng: {bad}\n")
print(f"p95 (m), mean ± std qua các ô; mất dấu = % run có lỗi > 100 m sau {skip} s đầu\n")
print("| Head | Kịch bản | n | " + " | ".join(have) + " | mh < naviloc | mh < naviloc_yaw | mh < causal | mất dấu %: "
      + " / ".join(k for k in have if k != "dead_reckoning") + " |")
print("|---" * (len(have) + 7) + "|")
for h in ("baseline", "lpn", "fsra"):
    for sc in SC:
        cs = cells.get((h, sc))
        if not cs:
            continue
        p = {k: np.array([c[k][0] for c in cs]) for k in have}
        lo = {k: np.mean([c[k][1] for c in cs]) for k in have}
        w = lambda k: f"{(p['mh_ekf'] < p[k]).sum()}/{len(cs)}"
        print(f"| {h} | {sc} | {len(cs)} | " + " | ".join(f"{p[k].mean():.1f} ± {p[k].std():.1f}" for k in have)
              + f" | {w('naviloc')} | {w('naviloc_yaw')} | {w('naviloc_causal')} | "
              + " / ".join(f"{lo[k]:.1f}" for k in have if k != "dead_reckoning") + " |")

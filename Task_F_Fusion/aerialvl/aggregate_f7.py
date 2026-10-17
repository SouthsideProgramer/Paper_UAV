# -*- coding: utf-8 -*-
"""aggregate_f7.py — F7-02: fusion on AerialVL test with zero-shot (F5-04/05 + NaviLoc of F6-02) vs fine-tuned
retrieval (F7-02), same runs. Per flight set x head x scenario, mean over the 3 training seeds:
p95 (m) zero-shot -> fine-tuned, and % windows with error > 100 m after the first 60 s.
usage: python aggregate_f7.py short|long"""
import sys
import numpy as np

ds = sys.argv[1]
ZS = {"short": "F5-04_test", "long": "F5-05_testlong"}[ds]
SC = ["vio", "imu", "init300", "imuinit300"]
ME = ["retrieval_top1", "dead_reckoning", "ekf_gated", "pf_topk", "naviloc_yaw", "mh_ekf"]


def stats(e):
    return np.percentile(e, 95), 100 * (e[:, 60:] > 100).any(1).mean()


print(f"## F7-02 {ds}: zero-shot → fine-tune (mean 3 seed train)\n")
print("| Head | Kịch bản | " + " | ".join(f"{k} p95" for k in ME) + " | mất dấu % mh | mất dấu % pf | mh thấp nhất (ft) |")
print("|---" * (len(ME) + 5) + "|")
for h in ("baseline", "lpn", "fsra"):
    for sc in SC:
        z, f, best = [], [], 0
        for s in (666, 667, 668):
            c = f"{h}_s{s}_{sc}"
            a = dict(np.load(f"results/{ZS}_{c}/errors.npz"))
            a["naviloc_yaw"] = np.load(f"results/F6-02_{ds}_{c}/errors.npz")["naviloc_yaw"]
            b = np.load(f"results/F7-02_{ds}_{c}/errors.npz")
            assert np.array_equal(a["dead_reckoning"], b["dead_reckoning"]), c
            z.append({k: stats(a[k]) for k in ME})
            f.append({k: stats(b[k]) for k in ME})
            p = {k: np.percentile(b[k], 95) for k in ME if k not in ("retrieval_top1", "dead_reckoning")}
            best += min(p, key=p.get) == "mh_ekf"
        m = lambda L, k, i: np.mean([x[k][i] for x in L])
        print(f"| {h} | {sc} | " + " | ".join(f"{m(z, k, 0):.0f} → {m(f, k, 0):.0f}" for k in ME)
              + f" | {m(z, 'mh_ekf', 1):.1f} → {m(f, 'mh_ekf', 1):.1f} | {m(z, 'pf_topk', 1):.1f} → {m(f, 'pf_topk', 1):.1f} | {best}/3 |")

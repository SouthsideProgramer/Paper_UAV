# -*- coding: utf-8 -*-
"""
aggregate_f3_09.py — F3-08 table redone with MH-EKF v3 (v_max = 0). For each (model, model seed, trajectory seed,
scenario) cell it takes retrieval_top1 / ekf_gated / pf_topk / mh_ekf v2 from F3-08 and mh_ekf v3 from F3-09,
after checking that ekf_gated is bit-identical in both runs (same flights, same measurements).
Prints per model and scenario: mean ± std p95 over the 9 cells, wins of v3 over gated, mean % flights lost
(> 100 m after the first 30 s), and the v3 − v2 p95 difference.
"""
import glob
import re
import numpy as np

SCEN = ["vio", "imu", "init300", "imuinit300"]
METH = ["retrieval_top1", "ekf_gated", "pf_topk", "mh_v2", "mh_v3"]
cells, mismatch = {}, []
for f in glob.glob("results/F3-09_*_s*_t*_*/errors.npz"):
    m = re.search(r"F3-09_(\w+?)_s(\d+)_t(\d+)_(\w+)/errors", f)
    key = (m.group(1), m.group(4), m.group(2), m.group(3))
    new, old = np.load(f), np.load(f.replace("F3-09_", "F3-08_"))
    if not np.array_equal(new["ekf_gated"], old["ekf_gated"]):
        mismatch.append(key)
        continue
    e = {k: old[k] for k in ("retrieval_top1", "ekf_gated", "pf_topk")}
    e["mh_v2"], e["mh_v3"] = old["mh_ekf"], new["mh_ekf"]
    cells[key] = {k: (np.percentile(v, 95), 100 * (v[:, 30:] > 100).any(1).mean()) for k, v in e.items()}

print(f"{len(cells)} ô ghép được, {len(mismatch)} ô ekf_gated KHÔNG trùng F3-08: {mismatch}\n")
rows = ["| Model | Kịch bản | n | " + " | ".join(f"{k} p95" for k in METH)
        + " | v3 thắng gated | mất dấu % gated / pf / v2 / v3 | v3 − v2 p95 (max \\|·\\|) |",
        "|---" * (len(METH) + 6) + "|"]
for model in ("baseline", "lpn", "fsra"):
    for sc in SCEN:
        cs = [v for k, v in cells.items() if k[0] == model and k[1] == sc]
        if not cs:
            continue
        p95 = {k: np.array([c[k][0] for c in cs]) for k in METH}
        lost = {k: np.mean([c[k][1] for c in cs]) for k in METH}
        d = p95["mh_v3"] - p95["mh_v2"]
        rows.append(f"| {model} | {sc} | {len(cs)} | " + " | ".join(f"{p95[k].mean():.1f} ± {p95[k].std():.1f}" for k in METH)
                    + f" | {int((p95['mh_v3'] < p95['ekf_gated']).sum())}/{len(cs)}"
                    + f" | {lost['ekf_gated']:.1f} / {lost['pf_topk']:.1f} / {lost['mh_v2']:.1f} / {lost['mh_v3']:.1f}"
                    + f" | {d.mean():+.2f} ({np.abs(d).max():.2f}) |")
print("\n".join(rows))

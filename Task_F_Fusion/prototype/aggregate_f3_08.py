# -*- coding: utf-8 -*-
"""
aggregate_f3_08.py — F3-08 summary over model seeds x trajectory seeds (test campuses).
Reads results/F3-08_<model>_s<mseed>_t<tseed>_<scenario>/errors.npz and prints, per model and
scenario: mean ± std of p95 over all (model seed, trajectory seed) cells, how many cells
mh_ekf beats ekf_gated on p95, and the mean % of flights lost (> 100 m after the first 30 s).
"""
import glob
import re
import numpy as np

SCEN = ["vio", "imu", "init300", "imuinit300"]
METH = ["retrieval_top1", "ekf_gated", "pf_topk", "mh_ekf"]
cells = {}
for f in glob.glob("results/F3-08_*_s*_t*_*/errors.npz"):
    m = re.search(r"F3-08_(\w+?)_s(\d+)_t(\d+)_(\w+)/errors", f)
    model, ms, ts, sc = m.group(1), m.group(2), m.group(3), m.group(4)
    e = np.load(f)
    cells[(model, sc, ms, ts)] = {k: (np.percentile(e[k], 95), 100 * (e[k][:, 30:] > 100).any(1).mean())
                                  for k in METH if k in e.files}

rows = ["| Model | Kịch bản | n | " + " | ".join(f"{k} p95" for k in METH) + " | mh thắng gated | mất dấu % gated / pf / mh |",
        "|---" * (len(METH) + 5) + "|"]
for model in sorted({k[0] for k in cells}):
    for sc in SCEN:
        cs = [v for k, v in cells.items() if k[0] == model and k[1] == sc]
        if not cs:
            continue
        p95 = {k: np.array([c[k][0] for c in cs]) for k in METH}
        lost = {k: np.mean([c[k][1] for c in cs]) for k in METH}
        wins = int((p95["mh_ekf"] < p95["ekf_gated"]).sum())
        rows.append(f"| {model} | {sc} | {len(cs)} | " + " | ".join(f"{p95[k].mean():.1f} ± {p95[k].std():.1f}" for k in METH)
                    + f" | {wins}/{len(cs)} | {lost['ekf_gated']:.1f} / {lost['pf_topk']:.1f} / {lost['mh_ekf']:.1f} |")
print("\n".join(rows))

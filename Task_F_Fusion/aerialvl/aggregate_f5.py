# -*- coding: utf-8 -*-
"""aggregate_f5.py — F5 summary over the 3 training seeds per head: p95 (mean ± std), catastrophic windows
(max error > 500 m), and how many seeds mh_ekf beats ekf_gated / pf_topk on p95.
usage: python aggregate_f5.py <results prefix, e.g. F5-04_test>"""
import glob, re, sys
import numpy as np

pre = sys.argv[1]
SC = ["vio", "imu", "init300", "imuinit300"]
ME = ["retrieval_top1", "dead_reckoning", "ekf_gated", "pf_topk", "mh_ekf"]
cells = {}
for f in glob.glob(f"results/{pre}_*_s*_*/errors.npz"):
    m = re.search(rf"{pre}_(\w+?)_s(\d+)_(\w+)/errors", f)
    e = np.load(f)
    cells[(m.group(1), m.group(3), m.group(2))] = {
        k: (np.percentile(e[k], 95), 100 * (e[k].max(1) > 500).mean()) for k in ME if k in e.files}
print("| Head | Kịch bản | n seed | " + " | ".join(f"{k} p95" for k in ME) + " | mh < gated | mh < pf | cửa sổ > 500 m %: gated / pf / mh |")
print("|---" * (len(ME) + 6) + "|")
for h in ("baseline", "lpn", "fsra"):
    for sc in SC:
        cs = [v for k, v in cells.items() if k[0] == h and k[1] == sc]
        if not cs:
            continue
        p = {k: np.array([c[k][0] for c in cs]) for k in ME}
        cat = {k: np.mean([c[k][1] for c in cs]) for k in ME}
        print(f"| {h} | {sc} | {len(cs)} | " + " | ".join(f"{p[k].mean():.1f} ± {p[k].std():.1f}" for k in ME)
              + f" | {(p['mh_ekf'] < p['ekf_gated']).sum()}/{len(cs)} | {(p['mh_ekf'] < p['pf_topk']).sum()}/{len(cs)}"
              + f" | {cat['ekf_gated']:.1f} / {cat['pf_topk']:.1f} / {cat['mh_ekf']:.1f} |")

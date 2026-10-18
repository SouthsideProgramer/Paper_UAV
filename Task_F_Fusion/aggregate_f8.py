# -*- coding: utf-8 -*-
"""aggregate_f8.py — F8-01 MH-EKF ablation table. For each variant (one factor changed from v3) and each
data set x scenario: p95 (m) and % runs lost (> 100 m after the first 60 s AerialVL / 30 s DenseUAV), mean over
LPN s666/667/668. Reference v3 errors are taken from the same runs (F7-02 ft, F5-04/F5-05 zero-shot, F3-09).
A cell is marked ▲ when the variant's p95 is >= 10 % worse than v3, ▼ when >= 10 % better.
usage: python aggregate_f8.py > paper_tables/ablation_mh.md"""
import os
import numpy as np

SC = ["vio", "imu", "init300", "imuinit300"]
SETS = {"shortft": ("aerialvl", lambda s, t: f"F7-02_short_lpn_s{s}_{t}", 60),
        "longft": ("aerialvl", lambda s, t: f"F7-02_long_lpn_s{s}_{t}", 60),
        "shortzs": ("aerialvl", lambda s, t: f"F5-04_test_lpn_s{s}_{t}", 60),
        "longzs": ("aerialvl", lambda s, t: f"F5-05_testlong_lpn_s{s}_{t}", 60),
        "dense": ("prototype", lambda s, t: f"F3-09_lpn_s{s}_t0_{t}", 30)}
VAR = [("max1", "1 hypothesis (mh_max = 1)"), ("max3", "mh_max = 3"), ("max5", "mh_max = 5"), ("max20", "mh_max = 20"),
       ("k1", "Top-1 only (K = 1)"), ("k3", "K = 3"), ("k5", "K = 5"),
       ("gate599", "gate χ² 5.99 (95 %)"), ("gate1382", "gate χ² 13.82 (99.9 %)"), ("gateinf", "no gating"),
       ("noreacq", "no re-acquisition"), ("reachoff", "re-acq. anywhere (v1)"), ("vmax10", "re-acq. 3σ + 10 m/s·Δt (v2)"),
       ("bestchild", "lost rule best-child (v0)")]


def stat(path, skip):
    e = np.load(path)["mh_ekf"]
    return np.percentile(e, 95), 100 * (e[:, skip:] > 100).any(1).mean()


def cell(ds, ref_fn, skip, v, t):
    root = os.path.join(ds, "results")
    r, x = [], []
    for s in (666, 667, 668):
        tail = f"lpn_s{s}_t0_{t}" if ds == "prototype" else f"lpn_s{s}_{t}"
        f = os.path.join(root, f"F8_{set_name}_{v}_{tail}/errors.npz")
        if not os.path.exists(f):
            return None
        r.append(stat(os.path.join(root, ref_fn(s, t), "errors.npz"), skip))
        x.append(stat(f, skip))
    return np.mean(r, 0), np.mean(x, 0)


for set_name, (ds, ref_fn, skip) in SETS.items():
    print(f"\n### {set_name} — p95 (m) / % lost; v3 reference in the first row; ▲ ≥ 10 % worse p95, ▼ ≥ 10 % better\n")
    print("| Variant | " + " | ".join(SC) + " |\n|---|" + "---|" * len(SC))
    ref = [np.mean([stat(os.path.join(ds, "results", ref_fn(s, t), "errors.npz"), skip) for s in (666, 667, 668)], 0) for t in SC]
    print("| **v3 (ours)** | " + " | ".join(f"{c[0]:.0f} / {c[1]:.1f}" for c in ref) + " |")
    for v, name in VAR:
        row = []
        for t in SC:
            c = cell(ds, ref_fn, skip, v, t)
            if c is None:
                row.append("—")
                continue
            (rp, _), (xp, xl) = c
            mark = " ▲" if xp >= 1.1 * rp else (" ▼" if xp <= 0.9 * rp else "")
            row.append(f"{xp:.0f} / {xl:.1f}{mark}")
        print(f"| {name} | " + " | ".join(row) + " |")

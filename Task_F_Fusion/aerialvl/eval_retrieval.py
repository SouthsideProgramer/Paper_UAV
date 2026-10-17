# -*- coding: utf-8 -*-
"""eval_retrieval.py — F5: top-1 / Top-K localisation error of retrieval on AerialVL (per sequence)."""
import sys
import numpy as np

for path in sys.argv[1:]:
    d = np.load(path)
    gf, qf = d["gallery_f"].astype(np.float32), d["query_f"].astype(np.float32)
    gxy, qxy, seq = d["gallery_xy"], d["query_xy"], d["query_seq"]
    top = np.zeros((len(qf), 10), int)
    for a in range(0, len(qf), 512):
        S = qf[a:a + 512] @ gf.T
        p = np.argpartition(-S, 10, 1)[:, :10]
        top[a:a + 512] = np.take_along_axis(p, np.argsort(-np.take_along_axis(S, p, 1), 1), 1)
    e1 = np.hypot(*(gxy[top[:, 0]] - qxy).T)
    ek = np.hypot(*(gxy[top] - qxy[:, None]).transpose(2, 0, 1)).min(1)
    print(f"== {path}  (gallery {len(gf)}, chance top-1 <= 50 m ~ {np.pi*50**2/ (len(gf)*25**2) :.4f})")
    print("seq | n | top1<=25m | <=50m | <=100m | median top1 err | p95 | any Top-10 <=50m")
    for s in list(np.unique(seq)) + ["ALL"]:
        m = np.ones(len(seq), bool) if s == "ALL" else seq == s
        print(f"{s} | {m.sum()} | {(e1[m]<=25).mean():.3f} | {(e1[m]<=50).mean():.3f} | {(e1[m]<=100).mean():.3f} | "
              f"{np.median(e1[m]):.0f} | {np.percentile(e1[m],95):.0f} | {(ek[m]<=50).mean():.3f}")

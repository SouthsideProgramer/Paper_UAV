# -*- coding: utf-8 -*-
"""
analyze_f2.py — Paired bootstrap differences between any two methods of a finished F2 run.

    python analyze_f2.py results/F2-01_val ekf_gated retrieval_top1 ekf_disp_gated ekf_gated
(arguments after the run directory are A B pairs; prints stat(A) - stat(B) with 95 % CI)
"""

import sys
import numpy as np
import metrics as M


def main():
    run_dir, pairs = sys.argv[1], sys.argv[2:]
    errs = np.load(f"{run_dir}/errors.npz")
    for a, b in zip(pairs[::2], pairs[1::2]):
        d = M.paired_diff(list(errs[a]), list(errs[b]), n_boot=1000, seed=0)
        cells = []
        for k in ("mean", "p95", "GFR@100"):
            lo, hi = d[k]["ci95"]
            sig = "*" if (lo > 0 or hi < 0) else " "
            cells.append(f"{k} {d[k]['diff']:+8.1f} [{lo:+8.1f}, {hi:+8.1f}]{sig}")
        print(f"{run_dir.split('/')[-1]:>10} {a:>15} - {b:<15} " + " | ".join(cells))


if __name__ == "__main__":
    main()

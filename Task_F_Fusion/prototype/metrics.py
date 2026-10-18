# -*- coding: utf-8 -*-
"""
metrics.py — Metre-level metrics for Task F2, same definitions as Task K1
(GFR@rho = P(err > rho), p50/p90/p95), plus trajectory-level tail metrics.
Confidence intervals bootstrap over TRAJECTORIES (errors within one flight are correlated).
"""

import numpy as np

RHOS = (50, 100, 200, 500)


def _stats(errs):
    e = np.concatenate(errs)
    tmax = np.array([x.max() for x in errs])
    out = {
        "mean": float(e.mean()),
        "p50": float(np.percentile(e, 50)),
        "p90": float(np.percentile(e, 90)),
        "p95": float(np.percentile(e, 95)),
        "p99": float(np.percentile(e, 99)),
        "max": float(e.max()),
        "traj_max_median": float(np.median(tmax)),
        "traj_catastrophic_pct": float(100 * (tmax > 500).mean()),  # flights that ever drift > 500 m
    }
    for r in RHOS:
        out[f"GFR@{r}"] = float(100 * (e > r).mean())
    return out


CI_KEYS = ("mean", "p95", "GFR@100", "traj_catastrophic_pct")


def summarize(errs, n_boot=1000, seed=0):
    rng = np.random.default_rng(seed)
    out = _stats(errs)
    n = len(errs)
    boots = {k: [] for k in CI_KEYS}
    for _ in range(n_boot):
        s = _stats([errs[i] for i in rng.integers(n, size=n)])
        for k in CI_KEYS:
            boots[k].append(s[k])
    for k in CI_KEYS:
        out[f"{k}_ci95"] = [float(np.percentile(boots[k], 2.5)), float(np.percentile(boots[k], 97.5))]
    return out


def paired_diff(errs_a, errs_b, n_boot=1000, seed=0):
    """Bootstrap CI of stat(A) - stat(B) with the SAME resampled trajectories."""
    rng = np.random.default_rng(seed)
    n = len(errs_a)
    point_a, point_b = _stats(errs_a), _stats(errs_b)
    diffs = {k: [] for k in CI_KEYS}
    for _ in range(n_boot):
        idx = rng.integers(n, size=n)
        sa, sb = _stats([errs_a[i] for i in idx]), _stats([errs_b[i] for i in idx])
        for k in CI_KEYS:
            diffs[k].append(sa[k] - sb[k])
    return {k: {"diff": point_a[k] - point_b[k],
                "ci95": [float(np.percentile(diffs[k], 2.5)), float(np.percentile(diffs[k], 97.5))]}
            for k in CI_KEYS}

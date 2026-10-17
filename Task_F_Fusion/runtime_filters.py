# -*- coding: utf-8 -*-
"""
runtime_filters.py — F8-02: wall-clock cost of every estimator per 1 Hz retrieval tick, single process / one core
(run with OMP_NUM_THREADS=1 etc. and nothing else on the CPU). Runs = the first --n windows of the AerialVL long
test flights (fine-tuned LPN s666), VIO and IMU-only. NaviLoc (batch) is timed per window and divided by its ticks.
Motion propagation inside the filters (VIO 10 Hz, IMU 100 Hz) is included in the per-tick time.
usage: OMP_NUM_THREADS=1 python runtime_filters.py [--n 20]
"""
import json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
AV = os.path.join(HERE, "aerialvl")
sys.path.insert(0, AV)
sys.path.insert(0, os.path.join(HERE, "prototype"))
N = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 20
os.chdir(AV)
import run_aerialvl as RA  # noqa: E402
import filters as F  # noqa: E402
import world as W  # noqa: E402
import naviloc  # noqa: E402,F401

ME = ["dead_reckoning", "ekf_gated", "pf_topk", "mh_ekf", "naviloc_yaw", "naviloc_causal"]
res = {}
for motion in ("vio", "imu"):
    sys.argv = ["x", "--feats", "feats/ft/merged/lpn_s666.npz", "--calib_from", "feats/ft/lpn_s666.npz", "--split", "test_long",
                "--win_step", "60", "--n_noise", "1", "--motion", motion, "--tag", "unused"]
    opt = RA.get_parse()
    cfg = dict(F.DEFAULT_CFG)
    cfg.update(RA.FROZEN_CFG)
    d = np.load(opt.feats)
    idx, sim = RA.topk(d["query_f"].astype(np.float32), d["gallery_f"].astype(np.float32), opt.K)
    world = W.World(d["gallery_xy"], np.zeros(len(d["gallery_xy"]), int), np.ones(len(d["gallery_xy"]), bool),
                    np.arange(len(d["gallery_xy"])))
    QF, GF = d["query_f"].astype(np.float32), d["gallery_f"].astype(np.float32)
    simq = lambda q, t: np.einsum("ij,ij->i", QF[q], GF[t])
    runs, _ = RA.build_runs(opt, d, world, idx, sim, simq)
    sel = runs[:: max(1, len(runs) // N)][:N]
    for k in ME:
        per_tick = []
        for r in sel:
            t0 = time.perf_counter()
            F.METHODS[k](r, cfg)
            per_tick.append((time.perf_counter() - t0) / r.n_ticks * 1e3)
        res[f"{motion}/{k}"] = {"mean_ms": float(np.mean(per_tick)), "p95_ms": float(np.percentile(per_tick, 95)), "n_windows": len(sel)}
        print(f"{motion:4s} {k:15s} {np.mean(per_tick):8.2f} ms/tick (p95 over windows {np.percentile(per_tick, 95):8.2f})", flush=True)
json.dump(res, open(os.path.join(HERE, "paper_tables", "runtime_filters.json"), "w"), indent=1)

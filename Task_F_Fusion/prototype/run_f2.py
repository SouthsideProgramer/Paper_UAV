# -*- coding: utf-8 -*-
"""
run_f2.py — Task F2: semi-synthetic camera (cross-view retrieval) + IMU/VIO fusion.

Synthetic world + calibrated retrieval model (runs anywhere, numpy + matplotlib):
    python run_f2.py --preset fsra --motion vio --n_traj 100 --seed 0 --tag fsra_vio_val

Real DenseUAV retrieval (server; needs scipy, the .mat and Dense_GPS_ALL.txt):
    python run_f2.py --world real --result_mat <pytorch_result_1.mat> \
        --gps_path <Dense_GPS_ALL.txt> --motion vio --tag lpn_real_vio

Seed convention: --seed 0 = validation (choose hyper-parameters here),
--seed 1 = test (run once, report). Outputs go to results/<tag>/.
"""

import argparse
import json
import os
import time
from dataclasses import dataclass
from multiprocessing import Pool

import numpy as np

import world as W
import sensors as S
import filters as F
import naviloc  # noqa: F401  registers naviloc, naviloc_causal
import metrics as M

HERE = os.path.dirname(os.path.abspath(__file__))


@dataclass
class Run:
    world: object
    motion: str
    per_tick: int
    dt_motion: float
    n_ticks: int
    meas: list            # meas[j] = (tiles, scores) or None, j = 0..n_ticks
    true_xy: np.ndarray   # (n_ticks, 2) truth at ticks 1..n_ticks
    p0_est: np.ndarray
    v0_est: np.ndarray = None
    psi0_est: float = 0.0
    v_odom: np.ndarray = None
    acc: np.ndarray = None
    gyro: np.ndarray = None
    vio_spec: object = None
    imu_spec: object = None
    qidx: list = None     # qidx[j] = query frame index of tick j (-1 if none); used by NaviLoc
    simq: object = None   # simq(query_idx, tiles) -> similarity to any tile; used by NaviLoc


def get_parse():
    p = argparse.ArgumentParser(description="Task F2: retrieval + IMU/VIO fusion (semi-synthetic)")
    p.add_argument("--world", default="synthetic", choices=["synthetic", "real"])
    p.add_argument("--result_mat", default="")
    p.add_argument("--gps_path", default="")
    p.add_argument("--preset", default="fsra", choices=list(S.RETRIEVAL_PRESETS))
    p.add_argument("--motion", default="vio", choices=["vio", "imu"])
    p.add_argument("--imu_grade", default="consumer", choices=list(S.IMU_PRESETS))
    p.add_argument("--n_traj", default=100, type=int)
    p.add_argument("--T", default=300.0, type=float, help="flight length (s)")
    p.add_argument("--meas_every", default=1, type=int, help="retrieval every N seconds")
    p.add_argument("--init_err", default=10.0, type=float, help="std of the true initial position error (m)")
    p.add_argument("--snap", default=20.0, type=float, help="max distance to a query tile for a measurement (m)")
    p.add_argument("--K", default=10, type=int)
    p.add_argument("--persist", default=0.5, type=float)
    p.add_argument("--p_true_in_topk", default=0.5, type=float)
    p.add_argument("--anchor_truth", default=0.5, type=float)
    p.add_argument("--methods", default="")
    p.add_argument("--campuses", default="all", choices=["all", "val", "test"],
                   help="real world: fly only over the first (val) or second (test) half of the test campuses")
    p.add_argument("--seed", default=0, type=int)
    p.add_argument("--workers", default=max(1, (os.cpu_count() or 2) - 1), type=int)
    p.add_argument("--n_boot", default=1000, type=int)
    p.add_argument("--tag", default="")
    p.add_argument("--cfg", default="", help="JSON overrides for filters.DEFAULT_CFG")
    return p.parse_args()


def build_world(opt):
    if opt.world == "synthetic":
        return W.synthetic_world(np.random.default_rng(12345)), None
    import scipy.io as sio
    m = sio.loadmat(opt.result_mat, variable_names=["gallery_label", "query_label"])
    world = W.real_world(opt.gps_path, m["gallery_label"].ravel(), m["query_label"].ravel())
    return world, None


def campus_split(world):
    """Query campuses sorted by smallest class label; first half = val, second half = test."""
    qc = np.unique(world.campus[world.query_idx])
    qc = sorted(qc, key=lambda c: world.labels[world.campus == c].min())
    h = len(qc) // 2
    return {"all": list(qc), "val": list(qc[:h]), "test": list(qc[h:])}


def pick_campus(opt, world, rng):
    return None if opt.campuses == "all" else rng.choice(campus_split(world)[opt.campuses])


def build_run(opt, world, retr, i):
    rng = lambda k: np.random.default_rng([opt.seed, i, k])
    tr = W.make_trajectory(world, rng(0), T=opt.T, campus=pick_campus(opt, world, rng(4)))
    per_sec = int(round(1.0 / tr.dt))
    n_ticks = int(opt.T)
    r0 = rng(1)
    p0_est = tr.p[0] + r0.normal(0, opt.init_err, 2)
    run = Run(world, opt.motion, 0, 0.0, n_ticks, [None] * (n_ticks + 1),
              tr.p[per_sec::per_sec][:n_ticks], p0_est)
    if opt.motion == "vio":
        run.vio_spec = S.VioSpec()
        _, run.v_odom = S.simulate_vio(tr, run.vio_spec, rng(2))
        run.per_tick = int(round(run.vio_spec.rate))
        run.dt_motion = 1.0 / run.vio_spec.rate
    else:
        run.imu_spec = S.IMU_PRESETS[opt.imu_grade]
        run.acc, run.gyro = S.simulate_imu(tr, run.imu_spec, rng(2))
        run.per_tick, run.dt_motion = per_sec, tr.dt
        run.v0_est = tr.v[0] + r0.normal(0, 0.2, 2)
        run.psi0_est = tr.yaw[0] + r0.normal(0, np.radians(3.0))
    retr.rng = rng(3)
    retr.reset()
    if hasattr(retr, "tile_sim"):
        run.qidx, run.simq = [-1] * (n_ticks + 1), retr.simq
    for j in range(1, n_ticks + 1):
        if j % opt.meas_every:
            continue
        t, d = world.nearest(run.true_xy[j - 1], world.query_idx)
        if d <= opt.snap:
            run.meas[j] = retr.query(t)
            if run.qidx is not None and run.meas[j] is not None:
                run.qidx[j] = retr.last_qi
    return run


_G = {}


def _eval_one(args):
    i, names = args
    run, cfg = _G["runs"][i], _G["cfg"]
    out = {}
    for n in names:
        est = F.METHODS[n](run, cfg)
        out[n] = np.hypot(*(est - run.true_xy).T)
    return out


def plot_cdf(errs, path, title):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    for n, e in errs.items():
        x = np.sort(np.concatenate(e))
        ax.plot(np.maximum(x, 0.5), np.arange(1, len(x) + 1) / len(x), label=n, lw=1.6)
    ax.set_xscale("log")
    ax.set_xlabel("Position error (m)")
    ax.set_ylabel("CDF")
    for r in (50, 100, 500):
        ax.axvline(r, color="0.8", lw=0.8, zorder=0)
    ax.set_title(title, fontsize=10)
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    opt = get_parse()
    cfg = dict(F.DEFAULT_CFG)
    cfg["sig_p0"] = max(cfg["sig_p0"], 1.5 * opt.init_err)
    if opt.cfg:
        cfg.update(json.loads(opt.cfg))
    names = opt.methods.split(",") if opt.methods else list(F.METHODS)
    tag = opt.tag or f"{opt.world}_{opt.preset}_{opt.motion}_s{opt.seed}"
    out_dir = os.path.join(HERE, "results", tag)
    os.makedirs(out_dir, exist_ok=True)

    t0 = time.time()
    world, _ = build_world(opt)
    extra = {}
    if opt.world == "synthetic":
        retr = S.SyntheticRetrieval(world, S.RETRIEVAL_PRESETS[opt.preset], None, K=opt.K,
                                    persist=opt.persist, p_true_in_topk=opt.p_true_in_topk,
                                    anchor_truth=opt.anchor_truth)
    else:
        retr = S.MatRetrieval(opt.result_mat, world, None, K=opt.K)
        cats = retr.category_stats()
        extra["real_top1_categories"] = dict(zip(["correct", "local<=100", "far_same_campus", "other_campus"],
                                                 cats.round(4).tolist()))
        extra["n_campus"] = int(len(np.unique(world.campus)))
        extra["campus_split"] = {k: [int(c) for c in v] for k, v in campus_split(world).items()}
        print("[INFO] campus split:", extra["campus_split"], "-> using", opt.campuses)
        print("[INFO] real top-1 categories:", extra["real_top1_categories"])
    print(f"[INFO] world: {len(world.xy)} tiles, {len(np.unique(world.campus))} campuses")

    runs = [build_run(opt, world, retr, i) for i in range(opt.n_traj)]
    n_meas = sum(m is not None for r in runs for m in r.meas)
    print(f"[INFO] built {len(runs)} runs, {n_meas} retrieval measurements ({time.time() - t0:.1f}s)")

    _G["runs"], _G["cfg"] = runs, cfg
    jobs = [(i, names) for i in range(len(runs))]
    if opt.workers > 1:
        with Pool(opt.workers) as pool:
            res = pool.map(_eval_one, jobs)
    else:
        res = [_eval_one(j) for j in jobs]
    errs = {n: [r[n] for r in res] for n in names}
    print(f"[INFO] filtering done ({time.time() - t0:.1f}s)")

    summary = {n: M.summarize(errs[n], opt.n_boot, opt.seed) for n in names}
    diffs = {}
    for prop in ("ekf_disp_gated", "ekf_dispgate", "ekf_topk_nn", "pf_topk", "mh_ekf", "ekf_gated"):
        for ref in ("retrieval_top1", "ekf_naive"):
            if prop in errs and ref in errs:
                diffs[f"{prop} - {ref}"] = M.paired_diff(errs[prop], errs[ref], opt.n_boot, opt.seed)

    cols = ["mean", "p50", "p90", "p95", "max", "GFR@50", "GFR@100", "GFR@500", "traj_catastrophic_pct"]
    lines = ["| Method | " + " | ".join(cols) + " | p95 CI95 |", "|---" * (len(cols) + 2) + "|"]
    for n in names:
        s = summary[n]
        ci = s["p95_ci95"]
        lines.append(f"| {n} | " + " | ".join(f"{s[c]:.1f}" for c in cols) + f" | [{ci[0]:.1f}, {ci[1]:.1f}] |")
    table = "\n".join(lines)
    print(table)
    for k, d in diffs.items():
        print(f"  {k}: p95 {d['p95']['diff']:+.1f} m {d['p95']['ci95']}, "
              f"GFR@100 {d['GFR@100']['diff']:+.2f} pt {d['GFR@100']['ci95']}")

    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump({"opt": vars(opt), "cfg": cfg, "extra": extra, "summary": summary, "paired_diffs": diffs},
                  f, indent=2)
    with open(os.path.join(out_dir, "table.md"), "w") as f:
        f.write(f"Config: `{json.dumps(vars(opt))}`\n\n{table}\n")
    np.savez_compressed(os.path.join(out_dir, "errors.npz"),
                        **{n: np.stack(errs[n]) for n in names})
    plot_cdf(errs, os.path.join(out_dir, "cdf.png"),
             f"{opt.world} | {opt.preset if opt.world == 'synthetic' else 'real .mat'} | {opt.motion} | seed {opt.seed}")
    print(f"[INFO] wrote {out_dir} ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()

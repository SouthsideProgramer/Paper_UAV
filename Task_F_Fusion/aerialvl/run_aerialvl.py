# -*- coding: utf-8 -*-
"""
run_aerialvl.py — F5: retrieval + IMU/VIO fusion on REAL AerialVL flights.

Real: trajectory (GNSS, 2 Hz -> smoothing spline -> 100 Hz), images, satellite map, retrieval Top-K
(features from aerialvl_extract.py). Simulated: IMU / VIO, generated from the real trajectory with the
same noise models as F2/F3 (sensors.py). Filters and their config are unchanged from F3 (frozen design).

A run = one window of --T seconds of one sequence (windows start every --win_step s) x one motion-noise
seed (--n_noise). Measurement at tick j (1 Hz) = Top-K of the frame closest in time (<= 0.3 s).
usage: python run_aerialvl.py --feats feats/lpn_s666.npz --split val --motion vio --tag F5-01_lpn_val_vio
"""
import argparse, json, os, sys, time
from multiprocessing import Pool
import numpy as np
from scipy.interpolate import make_smoothing_spline

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "prototype"))
import world as W  # noqa: E402
import sensors as S  # noqa: E402
import filters as F  # noqa: E402
import metrics as M  # noqa: E402
import run_f2 as R  # noqa: E402

# F5 protocol: val = flights of 2023-03-11 and 2023-03-16 (tuning), test = 2023-03-18 (run once)
# MH-EKF v3 (F5-03, frozen before the AerialVL test): re-acquire only inside 3 sigma of the propagated
# covariance (no v_max * dt growth). Identical to v2 on DenseUAV val.
FROZEN_CFG = {"v_max": 0.0}
SPLITS = {"val": ("2023-03-11", "2023-03-16"), "test": ("2023-03-18",)}
# F5-05: the 5 long test-day flights (not in F5-04); the long 2023-03-16 dusk flight belongs to val
LONG_TEST = ("2023-03-18-12-18-25", "2023-03-18-12-47-05", "2023-03-18-14-38-32", "2023-03-18-15-01-14",
             "2023-03-18-15-40-18")


def get_parse():
    p = argparse.ArgumentParser()
    p.add_argument("--feats", required=True)
    p.add_argument("--split", default="val", choices=list(SPLITS) + ["test_long", "all"])
    p.add_argument("--motion", default="vio", choices=["vio", "imu"])
    p.add_argument("--imu_grade", default="consumer", choices=list(S.IMU_PRESETS))
    p.add_argument("--T", default=240.0, type=float)
    p.add_argument("--win_step", default=20.0, type=float)
    p.add_argument("--n_noise", default=5, type=int)
    p.add_argument("--init_err", default=10.0, type=float)
    p.add_argument("--K", default=10, type=int)
    p.add_argument("--methods", default="retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf")
    p.add_argument("--seed", default=0, type=int)
    p.add_argument("--workers", default=8, type=int)
    p.add_argument("--n_boot", default=500, type=int)
    p.add_argument("--tag", required=True)
    p.add_argument("--cfg", default="")
    p.add_argument("--calib", default="val", choices=["none", "val"],
                   help="val: subtract the mean top-1 offset of good matches (<= 50 m) measured on the VAL flights")
    p.add_argument("--calib_from", default="", help="feature file whose val flights give the offset (default --feats)")
    return p.parse_args()


def topk(qf, gf, K, chunk=512):
    idx, sim = np.zeros((len(qf), K), int), np.zeros((len(qf), K), np.float32)
    for a in range(0, len(qf), chunk):
        Sm = qf[a:a + chunk] @ gf.T
        p = np.argpartition(-Sm, K, 1)[:, :K]
        s = np.take_along_axis(Sm, p, 1)
        o = np.argsort(-s, 1)
        idx[a:a + chunk], sim[a:a + chunk] = np.take_along_axis(p, o, 1), np.take_along_axis(s, o, 1)
    return idx, sim


def val_offset(d, idx, gate=50.0):
    """Camera / map registration bias: mean (tile - GNSS) of top-1 matches within `gate` m, VAL flights only."""
    val = np.array([str(s).startswith(SPLITS["val"]) for s in d["query_seq"]])
    e = d["gallery_xy"][idx[:, 0]] - d["query_xy"]
    m = val & (np.hypot(*e.T) <= gate)
    return e[m].mean(0), int(m.sum())


def gnss_trajectory(t, xy, dt=0.01):
    """Smoothing spline through the 2 Hz GNSS fixes -> W.Trajectory at 100 Hz (yaw = course over ground)."""
    tt = np.arange(t[0], t[-1], dt)
    sp = [make_smoothing_spline(t - t[0], xy[:, k], lam=2.0) for k in range(2)]
    P = np.stack([s(tt - t[0]) for s in sp], 1)
    V = np.stack([s.derivative(1)(tt - t[0]) for s in sp], 1)
    A = np.stack([s.derivative(2)(tt - t[0]) for s in sp], 1)
    yaw = np.arctan2(V[:, 1], V[:, 0])
    slow = np.hypot(*V.T) < 1.0                     # course is undefined while hovering: hold the last one
    if slow.all():
        yaw[:] = 0.0
    else:
        last = np.where(~slow, np.arange(len(yaw)), 0)
        np.maximum.accumulate(last, out=last)
        first = np.flatnonzero(~slow)[0]
        last[:first] = first
        yaw = yaw[last]
    # body yaw of a multirotor need not follow the course: track it with a rate limit (U-turns at the
    # end of survey legs would otherwise be instantaneous 180 deg yaw flips)
    body = np.zeros(len(yaw))
    rate = np.zeros(len(yaw))
    body[0] = yaw[0]
    for k in range(1, len(yaw)):
        rate[k - 1] = np.clip(W._wrap(yaw[k - 1] - body[k - 1]), -0.5, 0.5)
        body[k] = body[k - 1] + rate[k - 1] * dt
    rate[-1] = rate[-2]
    yaw = body
    return tt, W.Trajectory(dt, P, V, A, W._wrap(yaw), rate)


def build_runs(opt, d, world, idx, sim, simq=None):
    if opt.split == "test_long":
        seqs = [s for s in np.unique(d["query_seq"]) if str(s) in LONG_TEST]
    else:
        seqs = [s for s in np.unique(d["query_seq"])
                if opt.split == "all" or str(s).startswith(SPLITS[opt.split])]
    runs, meta = [], []
    for si, s in enumerate(seqs):
        m = np.flatnonzero(d["query_seq"] == s)
        t, xy = d["query_t"][m], d["query_xy"][m]
        tt, tr_full = gnss_trajectory(t, xy)
        per_sec = int(round(1.0 / tr_full.dt))
        for w0 in np.arange(0.0, (t[-1] - t[0]) - opt.T + 1e-6, opt.win_step):
            k0 = int(round(w0 * per_sec))
            k1 = k0 + int(round(opt.T * per_sec)) + 1
            tr = W.Trajectory(tr_full.dt, tr_full.p[k0:k1], tr_full.v[k0:k1], tr_full.a[k0:k1],
                              tr_full.yaw[k0:k1], tr_full.yawrate[k0:k1])
            n_ticks = int(opt.T)
            meas = [None] * (n_ticks + 1)
            qidx = [-1] * (n_ticks + 1)
            for j in range(1, n_ticks + 1):
                tj = tt[k0] + j
                q = int(np.argmin(np.abs(t - tj)))
                if abs(t[q] - tj) <= 0.3:
                    meas[j] = (idx[m[q]], sim[m[q]])
                    qidx[j] = int(m[q])
            for ns in range(opt.n_noise):
                rng = lambda k: np.random.default_rng([opt.seed, si, int(w0), ns, k])
                r0 = rng(1)
                run = R.Run(world, opt.motion, 0, 0.0, n_ticks, meas,
                            tr.p[per_sec::per_sec][:n_ticks], tr.p[0] + r0.normal(0, opt.init_err, 2))
                if opt.motion == "vio":
                    run.vio_spec = S.VioSpec()
                    _, run.v_odom = S.simulate_vio(tr, run.vio_spec, rng(2))
                    run.per_tick, run.dt_motion = int(round(run.vio_spec.rate)), 1.0 / run.vio_spec.rate
                else:
                    run.imu_spec = S.IMU_PRESETS[opt.imu_grade]
                    run.acc, run.gyro = S.simulate_imu(tr, run.imu_spec, rng(2))
                    run.per_tick, run.dt_motion = per_sec, tr.dt
                    run.v0_est = tr.v[0] + r0.normal(0, 0.2, 2)
                    run.psi0_est = tr.yaw[0] + r0.normal(0, np.radians(3.0))
                run.qidx, run.simq = qidx, simq
                runs.append(run)
                meta.append((str(s), float(w0), ns))
    return runs, meta


def main():
    opt = get_parse()
    cfg = dict(F.DEFAULT_CFG)
    cfg.update(FROZEN_CFG)
    cfg["sig_p0"] = max(cfg["sig_p0"], 1.5 * opt.init_err)
    if opt.cfg:
        cfg.update(json.loads(opt.cfg))
    names = opt.methods.split(",")
    out_dir = os.path.join(HERE, "results", opt.tag)
    os.makedirs(out_dir, exist_ok=True)
    t0 = time.time()

    d = np.load(opt.feats)
    idx, sim = topk(d["query_f"].astype(np.float32), d["gallery_f"].astype(np.float32), opt.K)
    gxy = d["gallery_xy"].copy()
    calib = [0.0, 0.0]
    if opt.calib == "val":
        if opt.calib_from:
            dc = np.load(opt.calib_from)
            off, n = val_offset(dc, topk(dc["query_f"].astype(np.float32), dc["gallery_f"].astype(np.float32), 1)[0])
        else:
            off, n = val_offset(d, idx)
        gxy -= off
        calib = off.tolist()
        print(f"[INFO] calib from {n} val matches: tile - GNSS = ({off[0]:+.1f}, {off[1]:+.1f}) m, removed")
    world = W.World(gxy, np.zeros(len(gxy), int), np.ones(len(gxy), bool), np.arange(len(gxy)))
    QF, GF = d["query_f"].astype(np.float32), d["gallery_f"].astype(np.float32)
    simq = lambda q, tiles: np.einsum("ij,ij->i", QF[q], GF[tiles])  # NaviLoc: similarity to any tile
    runs, meta = build_runs(opt, d, world, idx, sim, simq)
    print(f"[INFO] {len(runs)} runs from {len(set(m[0] for m in meta))} sequences ({time.time() - t0:.0f}s)")

    R._G["runs"], R._G["cfg"] = runs, cfg
    with Pool(opt.workers) as pool:
        res = pool.map(R._eval_one, [(i, names) for i in range(len(runs))])
    errs = {n: [r[n] for r in res] for n in names}

    summary = {n: M.summarize(errs[n], opt.n_boot, opt.seed) for n in names}
    diffs = {f"mh_ekf - {ref}": M.paired_diff(errs["mh_ekf"], errs[ref], opt.n_boot, opt.seed)
             for ref in names if ref != "mh_ekf" and "mh_ekf" in errs}
    per_seq = {}
    for s in sorted(set(m[0] for m in meta)):
        sel = [i for i, m in enumerate(meta) if m[0] == s]
        per_seq[s] = {n: float(np.percentile(np.concatenate([errs[n][i] for i in sel]), 95)) for n in names}

    cols = ["mean", "p50", "p95", "max", "GFR@50", "GFR@100", "traj_catastrophic_pct"]
    lines = ["| Method | " + " | ".join(cols) + " | p95 CI95 |", "|---" * (len(cols) + 2) + "|"]
    for n in names:
        s, ci = summary[n], summary[n]["p95_ci95"]
        lines.append(f"| {n} | " + " | ".join(f"{s[c]:.1f}" for c in cols) + f" | [{ci[0]:.1f}, {ci[1]:.1f}] |")
    table = "\n".join(lines)
    print(table)
    for k, v in diffs.items():
        print(f"  {k}: p95 {v['p95']['diff']:+.1f} m {v['p95']['ci95']}")
    for s, v in per_seq.items():
        print(f"  p95 {s}: " + ", ".join(f"{n} {x:.1f}" for n, x in v.items()))

    with open(os.path.join(out_dir, "summary.json"), "w") as f:
        json.dump({"opt": vars(opt), "cfg": cfg, "calib_offset": calib, "summary": summary, "paired_diffs": diffs, "per_seq_p95": per_seq,
                   "meta": meta}, f, indent=2)
    with open(os.path.join(out_dir, "table.md"), "w") as f:
        f.write(f"Config: `{json.dumps(vars(opt))}`\n\n{table}\n")
    np.savez_compressed(os.path.join(out_dir, "errors.npz"), **{n: np.stack(errs[n]) for n in names})
    R.plot_cdf(errs, os.path.join(out_dir, "cdf.png"), f"AerialVL {opt.split} | {os.path.basename(opt.feats)} | {opt.motion}")
    print(f"[INFO] wrote {out_dir} ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    main()

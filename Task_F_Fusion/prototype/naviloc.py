# -*- coding: utf-8 -*-
"""
naviloc.py — re-implementation of NaviLoc (Shpagin, Drones 10(2):97, 2026; preprint zenodo 17779254,
Algorithm 1 + Appendix A1-A5) as a competitor for MH-EKF. Registered into filters.METHODS on import.

Inputs, same as the other estimators: the run's motion stream and, per 1 s tick, the retrieval of one query
frame. NaviLoc additionally needs the similarity of a frame to ANY tile (the tile nearest to a candidate
position), given by run.simq(query_idx, tiles); run.qidx[j] is the query frame of tick j (-1 if none).

Faithful to the paper:
- Stage 1 GlobalAlign (A1): top-1 targets; theta by 36-step coarse grid on [-pi, pi) + bounded Brent in
  +-0.2 rad; translation = coordinate-wise median of (target - R v); score = sum of similarity at the
  nearest tile of every aligned frame.
- Stage 3 (A3-A5): windows of W frames, overlap O, K anchors = most similar frames at their current nearest
  tile, targets = those tiles; theta by 12-step grid on [-0.2, 0.2] + Brent; translation = median anchor
  residual; windows processed in order on the updated positions; overlapping estimates averaged.
- Defaults W = 30, O = 15, K = 3 (paper: "not tuned per dataset").
Adaptations (stated in the paper write-up):
- "VIO positions" = the motion-only track (filters.run_dead_reckoning: VIO or IMU integration), i.e. the
  same motion information the filters get; NaviLoc ignores its absolute start (global alignment).
- Stage 2 heading rectification is not applied: query features are the same for every method. AerialVL
  frames are already orientation-fixed (F5-00), i.e. rectification is given for free (oracle); on DenseUAV
  the query images are not tied to the simulated heading.
- Ticks without a frame: nearest frame position + globally rotated motion-track displacement.
- naviloc_yaw = naviloc with Stage 1 rotation limited to +-0.2 rad (the heading the filters also get).
- naviloc = batch over the whole window (as published; uses future frames). naviloc_causal = at every tick,
  Stage 1 on all frames so far + Stage 3 on the last window, estimate of the newest frame only (online).
"""
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.spatial import cKDTree

import filters as F


def _rot(th):
    c, s = np.cos(th), np.sin(th)
    return np.array([[c, -s], [s, c]])


def _kd(world):
    if getattr(world, "_kd", None) is None:
        world._kd = cKDTree(world.xy)
    return world._kd


def _search(score, lo, hi, n, delta):
    """Coarse grid of n angles on [lo, hi) then bounded Brent around the best (maximise score)."""
    grid = lo + (hi - lo) * np.arange(n) / n
    th_c = grid[int(np.argmax([score(t) for t in grid]))]
    r = minimize_scalar(lambda t: -score(t), bounds=(th_c - delta, th_c + delta), method="bounded",
                        options={"xatol": 1e-4})
    return r.x if -r.fun >= score(th_c) else th_c


def _global_align(V, T, q, world, simq, th_range=None):
    kd = _kd(world)

    def apply(th):
        Vr = V @ _rot(th).T
        return Vr + np.median(T - Vr, 0)

    def score(th):
        _, j = kd.query(apply(th))
        return float(simq(q, j).sum())

    if th_range is None:
        th = _search(score, -np.pi, np.pi, 36, 0.2)
    else:  # heading prior: the motion track is already in the world frame up to a small yaw error
        th = float(np.clip(_search(score, -th_range, th_range, 12, th_range), -th_range, th_range))
    return apply(th), th


def _optimize_se2(Pw, A, Tg, qw, world, simq, th_max=0.2, n_c=12):
    kd = _kd(world)

    def apply(th):
        Pr = Pw @ _rot(th).T
        return Pr + np.median(Tg - Pr[A], 0)

    def score(th):
        _, j = kd.query(apply(th))
        return float(simq(qw, j).sum())

    return apply(_search(score, -th_max, th_max, n_c, 0.2))


def _refine(P, q, world, simq, W, O, K):
    kd = _kd(world)
    N, step = len(P), max(1, W - O)
    S, C = np.zeros_like(P), np.zeros(N)
    for k in range(0, N, step):
        w = slice(k, min(k + W, N))
        Pw, qw = P[w], q[w]
        _, j = kd.query(Pw)
        c = simq(qw, j)
        A = np.argsort(-c)[:min(K, len(c))]
        P[w] = _optimize_se2(Pw, A, world.xy[j[A]], qw, world, simq)
        S[w] += P[w]
        C[w] += 1
        if k + W >= N:
            break
    return S / C[:, None]


def _naviloc_frames(V, T, q, world, simq, cfg):
    P, th = _global_align(V, T, q, world, simq, cfg.get("nl_th_range"))
    P = _refine(P.copy(), q, world, simq, cfg["nl_W"], cfg["nl_O"], cfg["nl_K"])
    return P, th


def _frames(run):
    fr = np.array([j for j in range(1, run.n_ticks + 1) if run.meas[j] is not None and run.qidx[j] >= 0])
    q = np.array([run.qidx[j] for j in fr])
    T = np.array([run.world.xy[run.meas[j][0][0]] for j in fr])
    return fr, q, T


def _fill(run, D, fr, Pf, th):
    """Per-tick output: nearest frame + rotated motion-track displacement."""
    ticks = np.arange(1, run.n_ticks + 1)
    near = np.abs(ticks[:, None] - fr[None, :]).argmin(1)
    R = _rot(th)
    return Pf[near] + (D[ticks - 1] - D[fr[near] - 1]) @ R.T


def run_naviloc(run, cfg):
    D = F.run_dead_reckoning(run, cfg)
    fr, q, T = _frames(run)
    if len(fr) < 3:
        return D
    Pf, th = _naviloc_frames(D[fr - 1], T, q, run.world, run.simq, cfg)
    return _fill(run, D, fr, Pf, th)


def run_naviloc_causal(run, cfg):
    D = F.run_dead_reckoning(run, cfg)
    fr, q, T = _frames(run)
    est = D.copy()
    W, O, K = cfg["nl_W"], cfg["nl_O"], cfg["nl_K"]
    for n in range(3, len(fr) + 1):
        P, th = _global_align(D[fr[:n] - 1], T[:n], q[:n], run.world, run.simq, cfg.get("nl_th_range"))
        a = max(0, n - W)
        P[a:] = _refine(P[a:].copy(), q[a:n], run.world, run.simq, W, O, K)
        j_lo = fr[n - 1]
        j_hi = fr[n] if n < len(fr) else run.n_ticks + 1
        for j in range(j_lo, j_hi):   # newest frame + motion until the next frame arrives
            est[j - 1] = P[-1] + (D[j - 1] - D[j_lo - 1]) @ _rot(th).T
    return est


F.METHODS["naviloc"] = run_naviloc
F.METHODS["naviloc_causal"] = run_naviloc_causal
F.METHODS["naviloc_yaw"] = lambda r, c: run_naviloc(r, dict(c, nl_th_range=0.2))
F.DEFAULT_CFG.update({"nl_W": 30, "nl_O": 15, "nl_K": 3})

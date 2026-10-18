# -*- coding: utf-8 -*-
"""
filters.py — Estimators compared in Task F2. All consume the SAME precomputed run
(trajectory, motion stream, retrieval Top-K per 1 s tick) and return one position
estimate per tick.

Motion models (EKF prediction):
- VioEkf  state [px, py, dpsi, s, bx, by]: VIO velocity minus its bias b, rotated back by
  the yaw offset dpsi and divided by (1+s). 10 Hz.
- InsEkf  state [px, py, vx, vy, psi, bax, bay, bg]: 2-D strapdown INS on raw IMU. 100 Hz.

Measurement variants (retrieval -> position update):
- naive       top-1 tile, fixed R, always accepted
- gated       + chi-square gate on the innovation, covariance inflation after long rejection
- disp_gated  + R grown with the score-weighted Top-K dispersion      (proposed A)
- dispgate    skip the measurement when Top-K dispersion > disp_thr, then chi-square gate
- topk_nn     Top-K candidate with the smallest Mahalanobis distance, gated
- mh_ekf      multi-hypothesis EKF: <= 10 Gaussian hypotheses spawned from Top-K   (proposed C)
- PF: particles [px, py, dpsi, s, bx, by] (VIO) or the INS state (IMU); likelihood = Top-K
  Gaussian mixture + uniform outlier floor                            (proposed B)
"""

import numpy as np
from sensors import rot, rot_d

CHI2_2DOF_99 = 9.21


def softmax(s, tau):
    z = (np.asarray(s) - np.max(s)) / tau
    e = np.exp(z)
    return e / e.sum()


def topk_dispersion(cxy, scores, tau):
    """Score-weighted RMS distance of the Top-K tiles from the top-1 tile (metres)."""
    w = softmax(scores, tau)
    return float(np.sqrt((w * ((cxy - cxy[0]) ** 2).sum(1)).sum()))


class _PosEkf:
    """Shared position update for both motion models (position is x[0:2])."""

    def update_pos(self, z, Rm, gate=None):
        P = self.P
        nu = z - self.x[:2]
        S = P[:2, :2] + Rm
        Si = np.linalg.inv(S)
        d2 = float(nu @ Si @ nu)
        if gate is not None and d2 > gate:
            return False
        K = P[:, :2] @ Si
        self.x = self.x + K @ nu
        IKH = np.eye(len(self.x))
        IKH[:, :2] -= K
        self.P = IKH @ P @ IKH.T + K @ Rm @ K.T
        return True

    def mahalanobis(self, z, Rm):
        nu = z - self.x[:2]
        return float(nu @ np.linalg.solve(self.P[:2, :2] + Rm, nu))

    def inflate(self, sigma):
        self.P[:2, :2] += sigma ** 2 * np.eye(2)


class VioEkf(_PosEkf):
    def __init__(self, p0, sig_p0, vio_spec):
        self.x = np.array([p0[0], p0[1], 0.0, 0.0, 0.0, 0.0])
        self.P = np.diag([sig_p0 ** 2, sig_p0 ** 2, vio_spec.yaw0_std ** 2, vio_spec.scale_std ** 2,
                          1e-6, 1e-6])
        self.spec = vio_spec

    def predict(self, v_odom, dt):
        psi, s, b = self.x[2], self.x[3], self.x[4:6]
        u = (v_odom - b) / (1 + s)
        R = rot(-psi)
        F = np.eye(6)
        F[:2, 2] = -rot_d(-psi) @ u * dt
        F[:2, 3] = -R @ u / (1 + s) * dt
        F[:2, 4:6] = -R / (1 + s) * dt
        self.x[:2] += R @ u * dt
        sp = self.spec
        Q = np.diag([(sp.vel_noise * dt) ** 2] * 2 + [sp.yaw_rw ** 2 * dt, 1e-10]
                    + [sp.vel_bias_rw ** 2 * dt] * 2)
        self.P = F @ self.P @ F.T + Q


class InsEkf(_PosEkf):
    def __init__(self, p0, v0, psi0, sig_p0, imu_spec, sig_v0=0.2, sig_psi0=np.radians(3.0)):
        self.x = np.array([p0[0], p0[1], v0[0], v0[1], psi0, 0.0, 0.0, 0.0])
        self.P = np.diag([sig_p0 ** 2] * 2 + [sig_v0 ** 2] * 2 + [sig_psi0 ** 2]
                         + [imu_spec.acc_bias0 ** 2] * 2 + [imu_spec.gyro_bias0 ** 2])
        self.spec = imu_spec

    def predict(self, acc, gyro, dt):
        x, sp = self.x, self.spec
        f = acc - x[5:7]
        psi = x[4]
        R = rot(psi)
        F = np.eye(8)
        F[0:2, 2:4] = np.eye(2) * dt
        F[2:4, 4] = rot_d(psi) @ f * dt
        F[2:4, 5:7] = -R * dt
        F[4, 7] = -dt
        x[0:2] += x[2:4] * dt
        x[2:4] += R @ f * dt
        x[4] += (gyro - x[7]) * dt
        q = np.zeros(8)
        q[2:4] = (sp.acc_noise * dt) ** 2
        q[4] = (sp.gyro_noise * dt) ** 2
        q[5:7] = sp.acc_bias_rw ** 2 * dt
        q[7] = sp.gyro_bias_rw ** 2 * dt
        self.P = F @ self.P @ F.T + np.diag(q)


# ------------------------------------------------------------ runners

def _motion_steps(run, j):
    """Motion samples between tick j-1 and tick j."""
    lo, hi = (j - 1) * run.per_tick, j * run.per_tick
    return range(lo, hi)


def run_retrieval_top1(run, cfg):
    est, last = [], run.p0_est.copy()
    for j in range(1, run.n_ticks + 1):
        m = run.meas[j]
        if m is not None:
            last = run.world.xy[m[0][0]]
        est.append(last)
    return np.array(est)


def run_dead_reckoning(run, cfg):
    ekf = _make_ekf(run, cfg)
    est = []
    for j in range(1, run.n_ticks + 1):
        _propagate(ekf, run, j)
        est.append(ekf.x[:2].copy())
    return np.array(est)


def _make_ekf(run, cfg):
    if run.motion == "vio":
        return VioEkf(run.p0_est, cfg["sig_p0"], run.vio_spec)
    return InsEkf(run.p0_est, run.v0_est, run.psi0_est, cfg["sig_p0"], run.imu_spec)


def _propagate(ekf, run, j):
    if run.motion == "vio":
        for k in _motion_steps(run, j):
            ekf.predict(run.v_odom[k], run.dt_motion)
    else:
        for k in _motion_steps(run, j):
            ekf.predict(run.acc[k], run.gyro[k], run.dt_motion)


def run_ekf(run, cfg, variant):
    ekf = _make_ekf(run, cfg)
    R0 = cfg["sig_meas"] ** 2 * np.eye(2)
    gate = None if variant == "naive" else CHI2_2DOF_99
    n_rej, est = 0, []
    for j in range(1, run.n_ticks + 1):
        _propagate(ekf, run, j)
        m = run.meas[j]
        if m is not None:
            tiles, scores = m
            cxy = run.world.xy[tiles]
            if variant == "topk_nn":
                d2 = [ekf.mahalanobis(c, R0) for c in cxy]
                z, Rm = cxy[int(np.argmin(d2))], R0
            elif variant == "dispgate":
                if topk_dispersion(cxy, scores, cfg["tau"]) > cfg["disp_thr"]:
                    est.append(ekf.x[:2].copy())
                    continue
                z, Rm = cxy[0], R0
            elif variant == "disp_gated":
                disp = topk_dispersion(cxy, scores, cfg["tau"])
                z, Rm = cxy[0], (cfg["sig_meas"] ** 2 + (cfg["alpha"] * disp) ** 2) * np.eye(2)
            else:
                z, Rm = cxy[0], R0
            if ekf.update_pos(z, Rm, gate):
                n_rej = 0
            else:
                n_rej += 1
                if n_rej >= cfg["n_reacq"]:
                    ekf.inflate(cfg["sig_inflate"])
                    n_rej = 0
        est.append(ekf.x[:2].copy())
    return np.array(est)


def _pf_init(run, cfg, rng, N):
    if run.motion == "vio":
        sp = run.vio_spec
        X = np.zeros((N, 6))
        X[:, 2] = rng.normal(0, sp.yaw0_std, N)
        X[:, 3] = rng.normal(0, sp.scale_std, N)
    else:
        sp = run.imu_spec
        X = np.zeros((N, 8))
        X[:, 2:4] = run.v0_est + rng.normal(0, 0.2, (N, 2))
        X[:, 4] = run.psi0_est + rng.normal(0, np.radians(3.0), N)
        X[:, 5:7] = rng.normal(0, sp.acc_bias0, (N, 2))
        X[:, 7] = rng.normal(0, sp.gyro_bias0, N)
    X[:, :2] = run.p0_est + rng.normal(0, cfg["sig_p0"], (N, 2))
    return X


def _pf_propagate(X, run, k, rng):
    N, dt = len(X), run.dt_motion
    if run.motion == "vio":
        sp = run.vio_spec
        c, s = np.cos(-X[:, 2]), np.sin(-X[:, 2])
        u = (run.v_odom[k][None, :] - X[:, 4:6]) / (1 + X[:, 3:4])
        X[:, 0] += (c * u[:, 0] - s * u[:, 1]) * dt
        X[:, 1] += (s * u[:, 0] + c * u[:, 1]) * dt
        X[:, :2] += rng.normal(0, sp.vel_noise * dt, (N, 2))
        X[:, 2] += rng.normal(0, sp.yaw_rw * np.sqrt(dt), N)
        X[:, 4:6] += rng.normal(0, sp.vel_bias_rw * np.sqrt(dt), (N, 2))
    else:
        sp = run.imu_spec
        f = run.acc[k][None, :] - X[:, 5:7] + rng.normal(0, sp.acc_noise, (N, 2))
        c, s = np.cos(X[:, 4]), np.sin(X[:, 4])
        X[:, 0:2] += X[:, 2:4] * dt
        X[:, 2] += (c * f[:, 0] - s * f[:, 1]) * dt
        X[:, 3] += (s * f[:, 0] + c * f[:, 1]) * dt
        X[:, 4] += (run.gyro[k] - X[:, 7] + rng.normal(0, sp.gyro_noise, N)) * dt
        X[:, 5:7] += rng.normal(0, sp.acc_bias_rw * np.sqrt(dt), (N, 2))
        X[:, 7] += rng.normal(0, sp.gyro_bias_rw * np.sqrt(dt), N)


def run_pf(run, cfg):
    """Particle filter driven by VIO or raw IMU; Top-K mixture likelihood with an outlier floor."""
    rng = np.random.default_rng(cfg["pf_seed"])
    N = cfg["n_particles"]
    X = _pf_init(run, cfg, rng, N)
    logw = np.zeros(N)
    sk2 = cfg["sig_meas"] ** 2
    log_norm = -np.log(2 * np.pi * sk2)
    log_floor = np.log(cfg["pf_eps"]) - np.log(cfg["pf_area"])
    est = []
    for j in range(1, run.n_ticks + 1):
        for k in _motion_steps(run, j):
            _pf_propagate(X, run, k, rng)
        m = run.meas[j]
        if m is not None:
            tiles, scores = m
            cxy = run.world.xy[tiles]
            pi = softmax(scores, cfg["tau"])
            d2 = ((X[:, None, :2] - cxy[None]) ** 2).sum(2)                   # (N, K)
            comp = np.log(pi)[None] + log_norm - 0.5 * d2 / sk2
            cmax = comp.max(1)
            log_mix = cmax + np.log(np.exp(comp - cmax[:, None]).sum(1))
            loglik = np.logaddexp(np.log(1 - cfg["pf_eps"]) + log_mix, log_floor)
            logw += loglik
            logw -= logw.max()
            w = np.exp(logw)
            w /= w.sum()
            if 1.0 / (w ** 2).sum() < N / 2:
                pos = (rng.random() + np.arange(N)) / N
                idx = np.minimum(np.searchsorted(np.cumsum(w), pos), N - 1)
                X = X[idx]
                X[:, :2] += rng.normal(0, cfg["pf_roughen"], (N, 2))
                if run.motion == "imu":
                    X[:, 2:4] += rng.normal(0, cfg["pf_roughen_v"], (N, 2))
                logw = np.zeros(N)
        w = np.exp(logw - logw.max())
        w /= w.sum()
        est.append(w @ X[:, :2])
    return np.array(est)


# ------------------------------------------------------------ multi-hypothesis EKF

def _rot_batch(th):
    c, s = np.cos(th), np.sin(th)
    return np.stack([np.stack([c, -s], -1), np.stack([s, c], -1)], -2)       # (M, 2, 2)


def _rot_d_batch(th):
    c, s = np.cos(th), np.sin(th)
    return np.stack([np.stack([-s, -c], -1), np.stack([c, -s], -1)], -2)


def _bank_predict(X, P, run, k):
    """Batched EKF prediction for all hypotheses (same models as VioEkf / InsEkf)."""
    M, n = X.shape
    dt = run.dt_motion
    F = np.repeat(np.eye(n)[None], M, 0)
    if run.motion == "vio":
        sp = run.vio_spec
        s, b = X[:, 3], X[:, 4:6]
        u = (run.v_odom[k][None] - b) / (1 + s)[:, None]
        R, Rd = _rot_batch(-X[:, 2]), _rot_d_batch(-X[:, 2])
        Ru = np.einsum("mij,mj->mi", R, u)
        F[:, :2, 2] = -np.einsum("mij,mj->mi", Rd, u) * dt
        F[:, :2, 3] = -Ru / (1 + s)[:, None] * dt
        F[:, :2, 4:6] = -R / (1 + s)[:, None, None] * dt
        X[:, :2] += Ru * dt
        q = np.array([(sp.vel_noise * dt) ** 2] * 2 + [sp.yaw_rw ** 2 * dt, 1e-10]
                     + [sp.vel_bias_rw ** 2 * dt] * 2)
    else:
        sp = run.imu_spec
        f = run.acc[k][None] - X[:, 5:7]
        R, Rd = _rot_batch(X[:, 4]), _rot_d_batch(X[:, 4])
        F[:, 0, 2] = F[:, 1, 3] = dt
        F[:, 2:4, 4] = np.einsum("mij,mj->mi", Rd, f) * dt
        F[:, 2:4, 5:7] = -R * dt
        F[:, 4, 7] = -dt
        X[:, 0:2] += X[:, 2:4] * dt
        X[:, 2:4] += np.einsum("mij,mj->mi", R, f) * dt
        X[:, 4] += (run.gyro[k] - X[:, 7]) * dt
        q = np.zeros(8)
        q[2:4] = (sp.acc_noise * dt) ** 2
        q[4] = (sp.gyro_noise * dt) ** 2
        q[5:7] = sp.acc_bias_rw ** 2 * dt
        q[7] = sp.gyro_bias_rw ** 2 * dt
    return F @ P @ F.transpose(0, 2, 1) + np.diag(q)[None]


def _logsumexp(a):
    m = a.max()
    return m + np.log(np.exp(a - m).sum())


def run_mh_ekf(run, cfg):
    """
    Gaussian-sum / multi-hypothesis EKF. Each tick every hypothesis branches into
    "measurement is an outlier" (no update) and one child per gated Top-K candidate
    (EKF update on that candidate). Weights follow the same Top-K mixture + outlier floor
    as pf_topk. Keep the best `mh_max` after merging children closer than `mh_merge` m.
    If no Top-K candidate has fallen inside the gate of the best hypothesis for `n_reacq`
    consecutive measurements (track lost), new hypotheses are spawned on the Top-K candidates
    that are reachable: within 3 sigma + v_max * (time since last support) of the best one. Output = position of the heaviest hypothesis.
    """
    ekf = _make_ekf(run, cfg)
    X, P, logw = ekf.x[None].copy(), ekf.P[None].copy(), np.zeros(1)
    n = X.shape[1]
    R0 = cfg["sig_meas"] ** 2 * np.eye(2)
    log_out = np.log(cfg["pf_eps"]) - np.log(cfg["pf_area"])
    log_in = np.log(1 - cfg["pf_eps"])
    gate, topk = cfg.get("mh_gate", CHI2_2DOF_99), cfg.get("mh_topk")
    n_unsup, j_sup, est = 0, 0, []
    for j in range(1, run.n_ticks + 1):
        for k in _motion_steps(run, j):
            P = _bank_predict(X, P, run, k)
        m = run.meas[j]
        if m is not None:
            tiles, scores = m
            if topk:                                   # ablation: use only the first topk candidates
                tiles, scores = tiles[:topk], scores[:topk]
            cxy = run.world.xy[tiles]
            lpi = np.log(softmax(scores, cfg["tau"]))
            S = P[:, :2, :2] + R0
            Si = np.linalg.inv(S)
            logdet = np.log(np.linalg.det(S))
            nu = cxy[None] - X[:, None, :2]                                       # (M, K, 2)
            d2 = np.einsum("mki,mij,mkj->mk", nu, Si, nu)
            ll = lpi[None] - np.log(2 * np.pi) - 0.5 * logdet[:, None] - 0.5 * d2
            hm, hk = np.nonzero(d2 < gate)
            # "lost" = no Top-K candidate falls inside the gate of the current best hypothesis
            lost = not (d2[int(np.argmax(logw))] < gate).any()
            n_before = len(logw)
            G = np.einsum("mij,mjk->mik", P[hm][:, :, :2], Si[hm])               # (C, n, 2)
            Xc = X[hm] + np.einsum("cij,cj->ci", G, nu[hm, hk])
            IKH = np.repeat(np.eye(n)[None], len(hm), 0)
            IKH[:, :, :2] -= G
            Pc = IKH @ P[hm]
            Pc = 0.5 * (Pc + Pc.transpose(0, 2, 1))
            X = np.concatenate([X, Xc])
            P = np.concatenate([P, Pc])
            logw = np.concatenate([logw + log_out, logw[hm] + log_in + ll[hm, hk]])
            # prune + merge
            order = np.argsort(-logw)
            keep, kw = [], []
            for i in order:
                for t, kept in enumerate(keep):
                    if np.hypot(*(X[i, :2] - X[kept, :2])) < cfg["mh_merge"]:
                        kw[t] = np.logaddexp(kw[t], logw[i])
                        break
                else:
                    if len(keep) < cfg["mh_max"]:
                        keep.append(i)
                        kw.append(logw[i])
            keep = np.array(keep)
            X, P = X[keep], P[keep]
            if cfg["mh_lost_rule"] == "best_child":       # original (F2-12) rule, kept for ablation
                lost = bool(keep[0] < n_before)
            logw = np.array(kw)
            logw -= _logsumexp(logw)
            n_unsup = n_unsup + 1 if lost else 0
            if not lost:
                j_sup = j
            if n_unsup >= cfg["n_reacq"] and cfg["mh_reach"]:
                # motion-consistent re-acquisition: only candidates the UAV could have reached
                b = int(np.argmax(logw))
                sig = np.sqrt(np.linalg.eigvalsh(P[b, :2, :2]).max())
                reach = 3 * sig + cfg["v_max"] * (j - j_sup) * run.dt_motion * run.per_tick
                ok = np.hypot(*(cxy - X[b, :2]).T) <= reach
                cxy, lpi = cxy[ok], lpi[ok]
            if n_unsup >= cfg["n_reacq"] and len(cxy):
                Xs = np.repeat(X[:1], len(cxy), 0)
                Xs[:, :2] = cxy
                Ps = np.repeat(P[:1], len(cxy), 0)
                Ps[:, :2, :] = 0.0
                Ps[:, :, :2] = 0.0
                Ps[:, :2, :2] = np.eye(2) * cfg["sig_meas"] ** 2
                X, P = np.concatenate([X, Xs]), np.concatenate([P, Ps])
                logw = np.concatenate([logw, logw[0] + np.log(cfg["mh_spawn_w"]) + lpi])
                logw -= _logsumexp(logw)
                n_unsup = 0
        est.append(X[int(np.argmax(logw)), :2].copy())
    return np.array(est)


METHODS = {
    "retrieval_top1": run_retrieval_top1,
    "dead_reckoning": run_dead_reckoning,
    "ekf_naive": lambda r, c: run_ekf(r, c, "naive"),
    "ekf_gated": lambda r, c: run_ekf(r, c, "gated"),
    "ekf_disp_gated": lambda r, c: run_ekf(r, c, "disp_gated"),
    "ekf_dispgate": lambda r, c: run_ekf(r, c, "dispgate"),
    "ekf_topk_nn": lambda r, c: run_ekf(r, c, "topk_nn"),
    "pf_topk": run_pf,
    "mh_ekf": run_mh_ekf,
}

DEFAULT_CFG = {
    "sig_p0": 15.0,        # initial position std (m); start point is known (take-off)
    "sig_meas": 20.0,      # retrieval position std ~ one grid step (m)
    "tau": 0.02,           # softmax temperature on cosine scores
    "alpha": 1.0,          # R grows with alpha * Top-K dispersion
    "disp_thr": 200.0,     # m, ekf_dispgate drops measurements with larger Top-K dispersion
    "n_reacq": 20,         # consecutive rejections before covariance inflation
    "sig_inflate": 50.0,   # m
    "n_particles": 2000,
    "pf_eps": 0.3,         # outlier probability of a retrieval measurement
    "pf_area": 1.0e6,      # m^2, support of the uniform outlier density (~ one campus)
    "pf_roughen": 2.0,     # m
    "pf_roughen_v": 0.05,  # m/s, velocity roughening (IMU particles)
    "pf_seed": 0,
    "mh_max": 10,          # hypotheses kept after each update
    "mh_merge": 15.0,      # m, children closer than this are merged
    "mh_spawn_w": 0.05,    # prior weight (x softmax score) of re-acquisition hypotheses
    "v_max": 10.0,         # m/s, UAV speed bound for motion-consistent re-acquisition
    "mh_lost_rule": "no_gate",  # "no_gate": no candidate in the best gate (F3-02); "best_child": F2-12
    "mh_reach": True,      # restrict re-acquisition to reachable candidates (F3-03)
    # ablation only (F8): "mh_gate" chi-square gate (default CHI2_2DOF_99), "mh_topk" candidates used (default all K)
}

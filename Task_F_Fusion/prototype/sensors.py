# -*- coding: utf-8 -*-
"""
sensors.py — Simulated motion sensors and retrieval measurements for Task F2.

Motion (relative) sources:
- simulate_imu(): 2-D strapdown IMU (body-frame accel + yaw gyro) with turn-on bias,
  bias random walk and white noise. Presets: consumer MEMS / tactical.
- simulate_vio(): VIO body velocity at 10 Hz with an unknown scale error and a slowly
  drifting yaw offset (what makes VIO drift in position).

Absolute (retrieval) sources — both return Top-K tile indices + similarity scores:
- SyntheticRetrieval: error model calibrated on the team's measured statistics
  (K2 table, Robustness task 4). Its Top-K structure is an ASSUMPTION, see README.
- MatRetrieval: real Top-K from a pytorch_result_*.mat (needs real_world()).
"""

from dataclasses import dataclass
import numpy as np


def rot(th):
    c, s = np.cos(th), np.sin(th)
    return np.array([[c, -s], [s, c]])


def rot_d(th):
    """d rot(th) / d th."""
    c, s = np.cos(th), np.sin(th)
    return np.array([[-s, -c], [c, -s]])


# ---------------------------------------------------------------- IMU

@dataclass
class ImuSpec:
    acc_noise: float = 0.05      # m/s^2, white noise std per sample
    acc_bias0: float = 0.05      # m/s^2, turn-on bias std
    acc_bias_rw: float = 1e-3    # m/s^2/sqrt(s)
    gyro_noise: float = 0.005    # rad/s, white noise std per sample
    gyro_bias0: float = 0.003    # rad/s (~0.17 deg/s)
    gyro_bias_rw: float = 1e-4   # rad/s/sqrt(s)


IMU_PRESETS = {
    "consumer": ImuSpec(),
    "tactical": ImuSpec(0.01, 0.005, 1e-4, 0.001, 1e-4, 1e-5),
}


def simulate_imu(tr, spec, rng):
    n, dt = len(tr.p), tr.dt
    ba = rng.normal(0, spec.acc_bias0, 2) + np.cumsum(rng.normal(0, spec.acc_bias_rw * np.sqrt(dt), (n, 2)), 0)
    bg = rng.normal(0, spec.gyro_bias0) + np.cumsum(rng.normal(0, spec.gyro_bias_rw * np.sqrt(dt), n))
    c, s = np.cos(tr.yaw), np.sin(tr.yaw)
    a_body = np.stack([c * tr.a[:, 0] + s * tr.a[:, 1], -s * tr.a[:, 0] + c * tr.a[:, 1]], 1)
    acc = a_body + ba + rng.normal(0, spec.acc_noise, (n, 2))
    gyro = tr.yawrate + bg + rng.normal(0, spec.gyro_noise, n)
    return acc, gyro


# ---------------------------------------------------------------- VIO

@dataclass
class VioSpec:
    rate: float = 10.0                                  # Hz
    vel_noise: float = 0.10                             # m/s
    scale_std: float = 0.02                             # 2 % scale error, constant per flight
    yaw0_std: float = np.radians(3.0)                   # initial yaw misalignment
    yaw_rw: float = np.radians(0.5) / np.sqrt(60.0)     # 0.5 deg per sqrt(min)
    vel_bias_rw: float = 0.003                          # m/s/sqrt(s), velocity bias in the VIO frame
                                                        # -> drift grows with distance (~1 % at 6 m/s)


def simulate_vio(tr, spec, rng):
    """Returns (idx, v_odom): v_odom[j] = (1+s) R(dpsi_j) v_true[idx[j]] + b_j + noise."""
    step = int(round(1.0 / (spec.rate * tr.dt)))
    idx = np.arange(0, len(tr.p), step)
    dtv = step * tr.dt
    dpsi = rng.normal(0, spec.yaw0_std) + np.cumsum(rng.normal(0, spec.yaw_rw * np.sqrt(dtv), len(idx)))
    s = rng.normal(0, spec.scale_std)
    c, sn = np.cos(dpsi), np.sin(dpsi)
    v = tr.v[idx]
    v_rot = np.stack([c * v[:, 0] - sn * v[:, 1], sn * v[:, 0] + c * v[:, 1]], 1)
    b = np.cumsum(rng.normal(0, spec.vel_bias_rw * np.sqrt(dtv), v_rot.shape), 0)
    v_odom = (1 + s) * v_rot + b + rng.normal(0, spec.vel_noise, v_rot.shape)
    return idx, v_odom


# ---------------------------------------------------------------- retrieval

# Top-1 outcome probabilities: (correct, local <=100 m, far same campus, other campus).
# correct / GFR@100 come from Task_K_Gap_Recall@1 K2; the far vs other-campus split uses
# Robustness task 4 (>1 km drift share). vits_82 is an ASSUMED split for the reproduced model.
RETRIEVAL_PRESETS = {
    "baseline_vits_19": (0.19, 0.18, 0.33, 0.30),
    "fsra": (0.645, 0.165, 0.07, 0.12),
    "lpn": (0.672, 0.157, 0.06, 0.111),
    "vits_82": (0.82, 0.08, 0.04, 0.06),
}


class SyntheticRetrieval:
    """
    Top-1 category drawn from `probs`; with prob `persist` the previous category repeats and a
    wrong top-1 moves with the UAV (aliasing is temporally correlated). The rest of the Top-K:
    the true tile is present with prob `p_true_in_topk` (if top-1 is wrong); each other slot is a
    tile within 60 m of an anchor with prob `p_near`, else a random tile (same campus as the
    truth with prob `p_same_campus`). For a wrong top-1 the anchor is the truth with prob
    `anchor_truth`, else the wrong top-1. anchor_truth=0 makes Top-K dispersion carry NO
    information about correctness (ablation of the key assumption).
    """

    def __init__(self, world, probs, rng, K=10, persist=0.5, p_true_in_topk=0.5,
                 p_near=0.5, p_same_campus=0.7, anchor_truth=0.5):
        self.w, self.rng, self.K = world, rng, K
        self.probs = np.asarray(probs, float) / np.sum(probs)
        self.persist, self.p_true, self.p_near = persist, p_true_in_topk, p_near
        self.p_same, self.anchor_truth = p_same_campus, anchor_truth
        self.reset()

    def reset(self):
        self.prev_cat, self.prev_top1, self.prev_true = None, None, None

    def _pick(self, idx):
        return int(idx[self.rng.integers(len(idx))])

    def _top1(self, cat, t):
        w, rng = self.w, self.rng
        tp, camp = w.xy[t], w.campus[t]
        if cat == 0:
            return t
        if cat >= 2 and self.prev_cat == cat and self.prev_top1 is not None:
            # correlated aliasing: the wrong match follows the UAV's motion
            target = w.xy[self.prev_top1] + (tp - w.xy[self.prev_true])
            j, _ = w.nearest(target, w.campus_tiles[w.campus[self.prev_top1]])
            if np.hypot(*(w.xy[j] - tp)) > 100.0:
                return j
        same = w.campus_tiles[camp]
        d = np.hypot(*(w.xy[same] - tp).T)
        if cat == 1:
            pool = same[(d > 1.0) & (d <= 100.0)]
        elif cat == 2:
            pool = same[d > 100.0]
        else:
            pool = np.flatnonzero(w.campus != camp)
        return self._pick(pool) if len(pool) else t

    def query(self, t):
        w, rng, K = self.w, self.rng, self.K
        if self.prev_cat is not None and rng.random() < self.persist:
            cat = self.prev_cat
        else:
            cat = int(rng.choice(4, p=self.probs))
        top1 = self._top1(cat, t)
        wrong = np.hypot(*(w.xy[top1] - w.xy[t])) > 100.0

        cands = [top1]
        if top1 != t and rng.random() < self.p_true:
            cands.append(t)
        anchor = t if (not wrong or rng.random() < self.anchor_truth) else top1
        near = w.campus_tiles[w.campus[anchor]]
        near = near[np.hypot(*(w.xy[near] - w.xy[anchor]).T) <= 60.0]
        tries = 0
        while len(cands) < K and tries < 20 * K:
            tries += 1
            r = rng.random()
            if r < self.p_near:
                j = self._pick(near)
            elif rng.random() < self.p_same:
                j = self._pick(w.campus_tiles[w.campus[t]])
            else:
                j = int(rng.integers(len(w.xy)))
            if j not in cands:
                cands.append(j)
        # true tile (if present) sits at a random rank > 1
        head, rest = cands[0], cands[1:]
        rng.shuffle(rest)
        cands = np.array([head] + rest)

        s1 = rng.normal(0.70, 0.07) + (0.02 if cat == 0 else 0.0)
        scores = s1 - np.concatenate([[0.0], np.cumsum(np.abs(rng.normal(0, 0.02, len(cands) - 1)))])

        self.prev_cat, self.prev_top1, self.prev_true = cat, top1, t
        return cands, scores


class MatRetrieval:
    """Real Top-K from a DenseUAV result .mat: pick a random altitude image of the true class."""

    def __init__(self, mat_path, world, rng, K=10, topn=80, chunk=256):
        import scipy.io as sio
        m = sio.loadmat(mat_path)
        qf, gf = m["query_f"].astype(np.float32), m["gallery_f"].astype(np.float32)
        ql, gl = m["query_label"].ravel(), m["gallery_label"].ravel()
        tile_of = {int(l): i for i, l in enumerate(world.labels)}
        self.g_tile = np.array([tile_of[int(l)] for l in gl])
        self.q_tile = np.array([tile_of[int(l)] for l in ql])
        self.q_by_tile = {}
        for qi, ti in enumerate(self.q_tile):
            self.q_by_tile.setdefault(int(ti), []).append(qi)
        self.top_idx = np.zeros((len(qf), topn), np.int64)
        self.top_sim = np.zeros((len(qf), topn), np.float32)
        for a in range(0, len(qf), chunk):
            S = qf[a:a + chunk] @ gf.T
            part = np.argpartition(-S, topn, axis=1)[:, :topn]
            ps = np.take_along_axis(S, part, 1)
            order = np.argsort(-ps, 1)
            self.top_idx[a:a + chunk] = np.take_along_axis(part, order, 1)
            self.top_sim[a:a + chunk] = np.take_along_axis(ps, order, 1)
        # query x tile similarity (max over the tile's gallery images), for NaviLoc's score at any position
        self.tile_sim = np.full((len(qf), len(world.xy)), -np.inf, np.float32)
        for a in range(0, len(qf), chunk):
            S = qf[a:a + chunk] @ gf.T
            for gi in range(len(gl)):
                np.maximum(self.tile_sim[a:a + chunk, self.g_tile[gi]], S[:, gi],
                           out=self.tile_sim[a:a + chunk, self.g_tile[gi]])
        self.tile_sim[~np.isfinite(self.tile_sim)] = -1.0
        self.last_qi = -1
        self.w, self.rng, self.K = world, rng, K

    def simq(self, q, tiles):
        return self.tile_sim[q, tiles]

    def reset(self):
        pass

    def topk_for_query(self, qi):
        tiles, scores = [], []
        for gi, s in zip(self.top_idx[qi], self.top_sim[qi]):
            t = int(self.g_tile[gi])
            if t not in tiles:
                tiles.append(t)
                scores.append(float(s))
                if len(tiles) == self.K:
                    break
        return np.array(tiles), np.array(scores)

    def query(self, t):
        qs = self.q_by_tile.get(int(t))
        if not qs:
            return None
        self.last_qi = int(qs[self.rng.integers(len(qs))])
        return self.topk_for_query(self.last_qi)

    def category_stats(self):
        """Top-1 outcome shares of the real model, for calibrating RETRIEVAL_PRESETS."""
        w = self.w
        cats = np.zeros(4)
        for qi in range(len(self.q_tile)):
            t = self.q_tile[qi]
            j = int(self.g_tile[self.top_idx[qi, 0]])
            d = np.hypot(*(w.xy[j] - w.xy[t]))
            if j == t:
                cats[0] += 1
            elif d <= 100.0:
                cats[1] += 1
            elif w.campus[j] == w.campus[t]:
                cats[2] += 1
            else:
                cats[3] += 1
        return cats / cats.sum()

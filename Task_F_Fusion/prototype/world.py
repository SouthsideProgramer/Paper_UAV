# -*- coding: utf-8 -*-
"""
world.py — World model for Task F2 (semi-synthetic camera + IMU fusion).

A "world" is the set of satellite gallery tiles (tile centres in local metres),
the campus each tile belongs to, and which tiles have a drone query (only those
can produce a retrieval measurement). Two sources:
- synthetic_world(): rectangular campus grids with DenseUAV spacing, runs anywhere.
- real_world():      tile centres from Dense_GPS_ALL.txt (not public, server only).

make_trajectory() flies a smooth path between tiles of one campus and records
true position / velocity / acceleration / yaw at a fixed rate.
"""

from dataclasses import dataclass
import numpy as np

GRID_STEP = 19.71  # DenseUAV gallery spacing in metres (reports/report.tex)
EARTH_R = 6371000.0


@dataclass
class World:
    xy: np.ndarray        # (N, 2) tile centres, metres, local east-north
    campus: np.ndarray    # (N,) campus id per tile
    query_ok: np.ndarray  # (N,) bool, tile has a drone query
    labels: np.ndarray    # (N,) DenseUAV class label (real) or tile index (synthetic)

    def __post_init__(self):
        self.query_idx = np.flatnonzero(self.query_ok)
        self.campus_tiles = {c: np.flatnonzero(self.campus == c) for c in np.unique(self.campus)}

    def nearest(self, p, idx=None):
        """Nearest tile to point p among `idx` (all tiles if None). Returns (tile, distance)."""
        idx = np.arange(len(self.xy)) if idx is None else idx
        d2 = ((self.xy[idx] - p) ** 2).sum(1)
        i = int(np.argmin(d2))
        return int(idx[i]), float(np.sqrt(d2[i]))


def synthetic_world(rng, n_campus=14, box=6000.0, min_sep=1200.0, size=(18, 36)):
    """14 rectangular campuses (like DenseUAV: 10 train + 4 test) scattered in a box."""
    centres = []
    while len(centres) < n_campus:
        c = rng.uniform(0, box, 2)
        if all(np.hypot(*(c - o)) > min_sep for o in centres):
            centres.append(c)
    xy, campus = [], []
    for k, c in enumerate(centres):
        nx, ny = rng.integers(size[0], size[1] + 1, 2)
        gx, gy = np.meshgrid(np.arange(nx), np.arange(ny))
        pts = np.stack([gx.ravel(), gy.ravel()], 1) * GRID_STEP
        xy.append(pts - pts.mean(0) + c)
        campus.append(np.full(len(pts), k))
    xy, campus = np.concatenate(xy), np.concatenate(campus)
    return World(xy, campus, np.ones(len(xy), bool), np.arange(len(xy)))


def load_gps_by_label(gps_path):
    """Dense_GPS_ALL.txt -> {class_label(int): (lon, lat)}; same parsing as Task K1."""
    gps = {}
    with open(gps_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 3:
                continue
            key = parts[0].replace("\\", "/").split("/")[-2]
            try:
                lab = int(key)
            except ValueError:
                continue
            if lab not in gps:
                gps[lab] = (float(parts[1].split("E")[-1]), float(parts[2].split("N")[-1]))
    return gps


def real_world(gps_path, gallery_labels, query_labels, link_dist=150.0):
    """Tiles = gallery classes placed at their GPS; campus = connected components (link < link_dist)."""
    from scipy.spatial import cKDTree
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components

    gps = load_gps_by_label(gps_path)
    labels = np.array(sorted(set(int(l) for l in gallery_labels)))
    missing = [l for l in labels if l not in gps]
    if missing:
        raise KeyError(f"{len(missing)} gallery labels have no GPS entry, e.g. {missing[:5]}")
    lonlat = np.array([gps[l] for l in labels])
    lon0, lat0 = lonlat.mean(0)
    x = np.radians(lonlat[:, 0] - lon0) * EARTH_R * np.cos(np.radians(lat0))
    y = np.radians(lonlat[:, 1] - lat0) * EARTH_R
    xy = np.stack([x, y], 1)

    pairs = np.array(sorted(cKDTree(xy).query_pairs(link_dist)))
    n = len(xy)
    adj = coo_matrix((np.ones(len(pairs)), (pairs[:, 0], pairs[:, 1])), shape=(n, n))
    _, campus = connected_components(adj, directed=False)
    query_ok = np.isin(labels, np.unique(query_labels))
    return World(xy, campus, query_ok, labels)


@dataclass
class Trajectory:
    dt: float
    p: np.ndarray      # (n, 2) position
    v: np.ndarray      # (n, 2) velocity, world frame
    a: np.ndarray      # (n, 2) acceleration applied from step k to k+1, world frame
    yaw: np.ndarray    # (n,) heading (body x-axis), rad
    yawrate: np.ndarray


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def make_trajectory(world, rng, T=300.0, dt=0.01, speed=(4.0, 8.0), turn_rate=0.35, campus=None):
    """Waypoint-following flight inside one campus (waypoints = random query tiles >150 m away)."""
    ok = world.query_idx
    if campus is None:
        campus = rng.choice(np.unique(world.campus[ok]))
    pts = world.xy[ok[world.campus[ok] == campus]]

    def new_target(p):
        far = np.flatnonzero(np.hypot(*(pts - p).T) > 150.0)
        return pts[rng.choice(far)] if len(far) else pts[rng.integers(len(pts))]

    p = pts[rng.integers(len(pts))].astype(float).copy()
    target = new_target(p)
    v_des = rng.uniform(*speed)
    heading = np.arctan2(*(target - p)[::-1])
    spd = v_des

    n = int(round(T / dt)) + 1
    P, V, A = np.zeros((n, 2)), np.zeros((n, 2)), np.zeros((n, 2))
    YAW, RATE = np.zeros(n), np.zeros(n)
    for k in range(n):
        if np.hypot(*(target - p)) < 25.0:
            target = new_target(p)
            v_des = rng.uniform(*speed)
        err = _wrap(np.arctan2(*(target - p)[::-1]) - heading)
        r = np.clip(1.0 * err, -turn_rate, turn_rate)
        acc_t = np.clip(0.5 * (v_des - spd), -1.0, 1.0)
        c, s = np.cos(heading), np.sin(heading)
        v = spd * np.array([c, s])
        a = acc_t * np.array([c, s]) + spd * r * np.array([-s, c])
        P[k], V[k], A[k], YAW[k], RATE[k] = p, v, a, heading, r
        p = p + v * dt
        heading = _wrap(heading + r * dt)
        spd = spd + acc_t * dt
    return Trajectory(dt, P, V, A, YAW, RATE)

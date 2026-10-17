# -*- coding: utf-8 -*-
"""
traj_example.py — F8-04: estimates of every method on ONE test window, for fig_traj (make_figures.py).
Window choice (stated in the caption): AerialVL long test flights, fine-tuned LPN s666, IMU-only scenario;
among windows where MH-EKF stays below 100 m p95, the one with the largest p95 gap to PF Top-K, i.e. an
illustration of re-acquisition after aliasing, not a typical window.
usage: python traj_example.py [scenario]
"""
import json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
AV = os.path.join(HERE, "..", "aerialvl")
sys.path.insert(0, AV)
sys.path.insert(0, os.path.join(HERE, "..", "prototype"))
sc = sys.argv[1] if len(sys.argv) > 1 else "imu"
args = {"vio": ["--motion", "vio"], "imu": ["--motion", "imu"], "init300": ["--motion", "vio", "--init_err", "300"],
        "imuinit300": ["--motion", "imu", "--init_err", "300"]}[sc]
os.chdir(AV)
sys.argv = ["x", "--feats", "feats/ft/merged/lpn_s666.npz", "--calib_from", "feats/ft/lpn_s666.npz", "--split", "test_long",
            "--win_step", "60", "--n_noise", "3", "--tag", "unused"] + args
import run_aerialvl as RA  # noqa: E402
import filters as F  # noqa: E402
import world as W  # noqa: E402
import naviloc  # noqa: E402,F401
from aerialvl_io import load_map, EARTH_R  # noqa: E402

opt = RA.get_parse()
cfg = dict(F.DEFAULT_CFG)
cfg.update(RA.FROZEN_CFG)
cfg["sig_p0"] = max(cfg["sig_p0"], 1.5 * opt.init_err)
d = np.load(opt.feats)
idx, sim = RA.topk(d["query_f"].astype(np.float32), d["gallery_f"].astype(np.float32), opt.K)
dc = np.load(opt.calib_from)
off, _ = RA.val_offset(dc, RA.topk(dc["query_f"].astype(np.float32), dc["gallery_f"].astype(np.float32), 1)[0])
gxy = d["gallery_xy"] - off
world = W.World(gxy, np.zeros(len(gxy), int), np.ones(len(gxy), bool), np.arange(len(gxy)))
QF, GF = d["query_f"].astype(np.float32), d["gallery_f"].astype(np.float32)
simq = lambda q, t: np.einsum("ij,ij->i", QF[q], GF[t])
runs, meta = RA.build_runs(opt, d, world, idx, sim, simq)

E = np.load(f"results/F7-02_long_lpn_s666_{sc}/errors.npz")
p95 = {k: np.percentile(E[k], 95, axis=1) for k in ("mh_ekf", "pf_topk")}
cand = np.flatnonzero(p95["mh_ekf"] < 100)
i = int(cand[np.argmax(p95["pf_topk"][cand] - p95["mh_ekf"][cand])])
run = runs[i]
out = {"truth": run.true_xy}
for k in ("dead_reckoning", "ekf_gated", "pf_topk", "naviloc_yaw", "mh_ekf"):
    out[k] = F.METHODS[k](run, cfg)
    err = np.hypot(*(out[k] - run.true_xy).T)
    if k in E.files:
        assert np.allclose(err, E[k][i]), f"{k}: estimate does not reproduce F7-02 errors"
out["top1"] = np.array([world.xy[m[0][0]] for m in run.meas[1:] if m is not None])

# satellite background around the window (map xy: east / north of the map's top-left corner, north negative)
mp = load_map("../../datasets/AerialVL/extracted", "large")
gsd_y = np.radians(mp["lat0"] - mp["lat1"]) * EARTH_R / mp["H"]
lo = out["truth"].min(0) - 400
hi = out["truth"].max(0) + 400
c = max(hi - lo) / 2
mid = (lo + hi) / 2
x0, x1, y0, y1 = mid[0] - c, mid[0] + c, mid[1] - c, mid[1] + c
px = lambda x: int(np.clip(round(x / mp["gsd"]), 0, mp["W"]))
py = lambda y: int(np.clip(round(-y / gsd_y), 0, mp["H"]))
bg = mp["img"][py(y1):py(y0), px(x0):px(x1)][::4, ::4]
err = {k: float(np.percentile(np.hypot(*(out[k] - run.true_xy).T), 95)) for k in ("dead_reckoning", "ekf_gated", "pf_topk", "naviloc_yaw", "mh_ekf")}
info = {"window": meta[i], "scenario": sc, "p95": err,
        "title": f"Flight {meta[i][0][11:]}, window +{meta[i][1]:.0f} s, {sc.upper() if sc != 'imu' else 'IMU only'}"}
np.savez(os.path.join(HERE, "traj_example.npz"), extent=np.array([x0, x1, y0, y1]), bg=bg, info=json.dumps(info), **out)
print(json.dumps(info, indent=1))

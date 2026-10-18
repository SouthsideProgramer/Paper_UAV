# -*- coding: utf-8 -*-
"""
footprint_scan.py — F5-00: estimate the ground footprint of AerialVL frames by NCC template matching
(gradient-magnitude images) of the north-up frame against the map, over a range of assumed footprints.
The right footprint gives high NCC peaks that land close to the GNSS fix across many frames.
"""
import glob, os, sys
import numpy as np
import cv2
from aerialvl_io import load_map, list_frames, lonlat_to_px, crop

if __name__ != "__main__":
    raise SystemExit
root = sys.argv[1]
n_per = int(sys.argv[2]) if len(sys.argv) > 2 else 10
mp = load_map(root, "large")
R = 600


def grad(g):
    g = cv2.GaussianBlur(g.astype(np.float32), (0, 0), 1.0)
    return cv2.magnitude(cv2.Sobel(g, cv2.CV_32F, 1, 0), cv2.Sobel(g, cv2.CV_32F, 0, 1))


widths = np.arange(150, 701, 25)          # assumed E-W ground width of the north-up frame (m)
res = {w: [] for w in widths}
for seq in sorted(glob.glob(os.path.join(root, "*_trajtr", "*"))):
    fr = list_frames(seq)
    for f in fr[:: max(1, len(fr) // n_per)][:n_per]:
        x, y = lonlat_to_px(mp, f["lon"], f["lat"])
        G = grad(cv2.cvtColor(crop(mp, x, y, R), cv2.COLOR_RGB2GRAY))
        im = cv2.rotate(cv2.imread(f["path"], cv2.IMREAD_GRAYSCALE), cv2.ROTATE_90_CLOCKWISE)
        for w in widths:
            s = w / mp["gsd"] / im.shape[1]
            t = grad(cv2.resize(im, None, fx=s, fy=s, interpolation=cv2.INTER_AREA))
            r = cv2.matchTemplate(G, t, cv2.TM_CCOEFF_NORMED)
            _, mx, _, loc = cv2.minMaxLoc(r)
            cx, cy = loc[0] + t.shape[1] / 2, loc[1] + t.shape[0] / 2
            res[w].append((mx, np.hypot(cx - R, cy - R) * mp["gsd"]))
print("width_m  n  mean_peakNCC  median_dist_to_GNSS_m  frac_within_30m")
for w in widths:
    a = np.array(res[w])
    print(f"{w:6d} {len(a):3d}  {a[:,0].mean():.3f}  {np.median(a[:,1]):7.1f}  {(a[:,1] < 30).mean():.2f}")

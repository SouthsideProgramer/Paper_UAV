# -*- coding: utf-8 -*-
"""
register_frames.py — F5-00: measure AerialVL frame footprint (m/px), rotation vs north-up map and
the offset between image centre and the GNSS fix, by SIFT + RANSAC similarity against the map.
usage: python register_frames.py <extracted_dir> [frames_per_seq]
"""
import glob, os, sys
import numpy as np
import cv2
from aerialvl_io import load_map, list_frames, lonlat_to_px, crop as crop_map

root = sys.argv[1]
n_per = int(sys.argv[2]) if len(sys.argv) > 2 else 15
mp = load_map(root, "large")
sift = cv2.SIFT_create(4000)
R = 700  # map crop half-size (px ~ m)
rows = []
for seq in sorted(glob.glob(os.path.join(root, "*_trajtr", "*"))):
    fr = list_frames(seq)
    for f in fr[:: max(1, len(fr) // n_per)][:n_per]:
        x, y = lonlat_to_px(mp, f["lon"], f["lat"])
        crop = cv2.cvtColor(crop_map(mp, x, y, R), cv2.COLOR_RGB2GRAY)
        im0 = cv2.rotate(cv2.imread(f["path"], cv2.IMREAD_GRAYSCALE), cv2.ROTATE_90_CLOCKWISE)  # east-up -> north-up
        k2, d2 = sift.detectAndCompute(cv2.createCLAHE(2.0, (8, 8)).apply(crop), None)
        best = None
        for ds in (0.12, 0.18, 0.25, 0.35):
            im = cv2.createCLAHE(2.0, (8, 8)).apply(cv2.resize(im0, None, fx=ds, fy=ds, interpolation=cv2.INTER_AREA))
            k1, d1 = sift.detectAndCompute(im, None)
            if d1 is None or d2 is None or len(k1) < 10:
                continue
            m = cv2.BFMatcher().knnMatch(d1, d2, k=2)
            good = [a for a, b in (p for p in m if len(p) == 2) if a.distance < 0.8 * b.distance]
            if len(good) < 12:
                continue
            A, inl = cv2.estimateAffinePartial2D(np.float32([k1[g.queryIdx].pt for g in good]),
                                                 np.float32([k2[g.trainIdx].pt for g in good]),
                                                 method=cv2.RANSAC, ransacReprojThreshold=4.0)
            if A is not None and (best is None or inl.sum() > best[2].sum()):
                best = (ds, A, inl, im.shape)
        if best is None or best[2].sum() < 20:
            continue
        ds, A, inl, (h, w) = best
        s = np.hypot(A[0, 0], A[1, 0]) * ds          # map px per original frame px
        rot = np.degrees(np.arctan2(A[1, 0], A[0, 0]))
        cx, cy = A @ np.array([w / 2, h / 2, 1.0])
        off = np.hypot(cx - R, cy - R) * mp["gsd"]
        rows.append((os.path.basename(seq), s, rot, off, int(inl.sum())))
        print(f"{rows[-1][0]} scale {s:.3f} map-px/frame-px  rot {rot:+7.1f} deg  centre-GNSS {off:6.1f} m  inliers {rows[-1][4]}")
if rows:
    a = np.array([r[1:4] for r in rows])
    print(f"\nregistered {len(rows)} frames | scale median {np.median(a[:,0]):.3f} "
          f"(footprint {np.median(a[:,0])*1536*mp['gsd']:.0f} (E-W) x {np.median(a[:,0])*2048*mp['gsd']:.0f} m) "
          f"| rot median {np.median(a[:,1]):+.1f} IQR {np.percentile(a[:,1],25):+.1f}..{np.percentile(a[:,1],75):+.1f} "
          f"| centre offset median {np.median(a[:,2]):.1f} m")

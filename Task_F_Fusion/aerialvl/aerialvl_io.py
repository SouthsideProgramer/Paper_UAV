# -*- coding: utf-8 -*-
"""aerialvl_io.py — AerialVL VAL part: geo-referenced maps and frame sequences.

Map files: @<name>@<LeftTopLon>@<LeftTopLat>@<RightBottomLon>@<RightBottomLat>@.tif (north-up).
Frames:    <seq>/@<UTC ms>@<lon>@<lat>@.png (2 Hz, GNSS 1.5 m RMS).
"""
import glob, math, os
import numpy as np

EARTH_R = 6371000.0


def load_map(root, name="large", with_img=True):
    p = glob.glob(os.path.join(root, "geo_referenced_map", f"@{name}_map@*.tif"))[0]
    lon0, lat0, lon1, lat1 = map(float, os.path.basename(p).split("@")[2:6])
    m = {"path": p, "lon0": lon0, "lat0": lat0, "lon1": lon1, "lat1": lat1}
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(p)
    m["W"], m["H"] = im.size
    if with_img:
        m["img"] = np.asarray(im.convert("RGB"))
    m["gsd"] = (lon1 - lon0) * math.radians(1) * EARTH_R * math.cos(math.radians((lat0 + lat1) / 2)) / m["W"]
    return m


def lonlat_to_px(m, lon, lat):
    return ((lon - m["lon0"]) / (m["lon1"] - m["lon0"]) * m["W"],
            (m["lat0"] - lat) / (m["lat0"] - m["lat1"]) * m["H"])


def px_to_lonlat(m, x, y):
    return (m["lon0"] + x / m["W"] * (m["lon1"] - m["lon0"]),
            m["lat0"] - y / m["H"] * (m["lat0"] - m["lat1"]))


def lonlat_to_xy(m, lon, lat):
    """Local metres east/north of the map's top-left corner (y grows north, so it is negative)."""
    lat_c = (m["lat0"] + m["lat1"]) / 2
    return (np.radians(np.asarray(lon) - m["lon0"]) * EARTH_R * math.cos(math.radians(lat_c)),
            np.radians(np.asarray(lat) - m["lat0"]) * EARTH_R)


def list_frames(seq_dir):
    out = []
    for p in glob.glob(os.path.join(seq_dir, "@*@.png")):
        _, t, lon, lat, _ = os.path.basename(p).split("@")
        out.append({"path": p, "t": int(t) / 1000.0, "lon": float(lon), "lat": float(lat)})
    return sorted(out, key=lambda f: f["t"])


def crop(m, x, y, r):
    """Square crop of half-size r px centred at (x, y), zero-padded outside the map."""
    img = m["img"]
    out = np.zeros((2 * r, 2 * r, 3), img.dtype)
    x0, y0 = int(round(x)) - r, int(round(y)) - r
    a, b = max(0, y0), min(img.shape[0], y0 + 2 * r)
    c, d = max(0, x0), min(img.shape[1], x0 + 2 * r)
    if a < b and c < d:
        out[a - y0:b - y0, c - x0:d - x0] = img[a:b, c:d]
    return out

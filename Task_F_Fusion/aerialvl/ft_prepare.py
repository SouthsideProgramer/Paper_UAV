# -*- coding: utf-8 -*-
"""
ft_prepare.py — F7: cache the query crops of the NON-test flights for retrieval fine-tuning.

Same query geometry as aerialvl_extract.py (rotate 90 deg CW to north-up, centre square of tile_m metres),
stored at --px pixels so the fine-tuning loader does not re-read the 4 MB PNGs. Only flights of 2023-03-11
and 2023-03-16 are allowed (the 2023-03-18 flights are the F5 test set and must never be touched here).
usage: python ft_prepare.py --root <AerialVL/extracted> --seqs short_trajtr/2023-03-16-16-58-43 ... --out ft/x.npz
"""
import argparse, os
import numpy as np
from PIL import Image
from aerialvl_io import load_map, list_frames, lonlat_to_xy

p = argparse.ArgumentParser()
p.add_argument("--root", required=True)
p.add_argument("--seqs", nargs="+", required=True)
p.add_argument("--tile_m", default=200.0, type=float)
p.add_argument("--frame_w_m", default=200.0, type=float)
p.add_argument("--px", default=256, type=int)
p.add_argument("--out", required=True)
opt = p.parse_args()
assert not any("2023-03-18" in s for s in opt.seqs), "test-day flights are not allowed for fine-tuning"

mp = load_map(opt.root, "large", with_img=False)
ims, xy, t, seq = [], [], [], []
for s in opt.seqs:
    fr = list_frames(os.path.join(opt.root, s))
    for f in fr:
        im = Image.open(f["path"]).convert("RGB").transpose(Image.ROTATE_270)
        w, h = im.size
        c = int(round(w * min(1.0, opt.tile_m / opt.frame_w_m)))
        l, tp = (w - c) // 2, (h - c) // 2
        ims.append(np.asarray(im.crop((l, tp, l + c, tp + c)).resize((opt.px, opt.px), Image.BICUBIC)))
        xy.append(lonlat_to_xy(mp, f["lon"], f["lat"]))
        t.append(f["t"])
        seq.append(os.path.basename(s))
    print(f"[INFO] {s}: {len(fr)} frames")
np.savez(opt.out, img=np.stack(ims), xy=np.array(xy, float), t=np.array(t), seq=np.array(seq))
print(f"[INFO] wrote {opt.out}: {len(ims)} crops")

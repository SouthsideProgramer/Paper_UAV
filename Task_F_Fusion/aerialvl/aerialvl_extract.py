# -*- coding: utf-8 -*-
"""
aerialvl_extract.py — F5: DenseUAV-trained retrieval features on AerialVL (zero-shot).

Query  = every frame of the chosen sequences, rotated 90 deg CW (frames are east-up -> north-up)
         and centre-cropped to a square of --tile_m metres (F5-00: frame E-W width ~200 m).
Gallery = square tiles of --tile_m metres cut from the north-up map on a --stride metre grid.
Features follow DenseUAV test.py: 224x224, ImageNet norm, feature(img) + feature(flip(img)), L2 norm.

Run with the DenseUAV venv; --ckpt_dir is a trained checkpoint folder (opts.yaml + net_119.pth + code copy).
usage: python aerialvl_extract.py --ckpt_dir <.../checkpoints/lpn> --root <AerialVL/extracted> --out <file.npz>
"""
import argparse, glob, os, sys, time
import numpy as np
import torch
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from aerialvl_io import load_map, list_frames, px_to_lonlat, lonlat_to_xy  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--ckpt_dir", required=True)
p.add_argument("--root", required=True)
p.add_argument("--seqs", default="*_trajtr/*")
p.add_argument("--map", default="large")
p.add_argument("--tile_m", default=200.0, type=float)
p.add_argument("--frame_w_m", default=200.0, type=float, help="E-W ground width of a north-up frame (F5-00)")
p.add_argument("--stride", default=25.0, type=float)
p.add_argument("--out", required=True)
p.add_argument("--batch", default=64, type=int)
p.add_argument("--workers", default=8, type=int)
p.add_argument("--gallery_from", default="", help="reuse gallery features of an earlier run of the SAME checkpoint")
opt = p.parse_args()
opt.root = os.path.abspath(opt.root)
opt.out = os.path.abspath(opt.out)
opt.gallery_from = os.path.abspath(opt.gallery_from) if opt.gallery_from else ""

# ---- model, exactly as test.py builds it (run from inside the checkpoint folder)
os.chdir(opt.ckpt_dir)
sys.path.insert(0, opt.ckpt_dir)
import yaml  # noqa: E402
from tool.utils import load_network  # noqa: E402

cfg = argparse.Namespace(checkpoint="net_119.pth")
for k, v in yaml.safe_load(open("opts.yaml")).items():
    setattr(cfg, k, v)
model = load_network(cfg).eval().cuda()
H, W = cfg.h, cfg.w

MEAN = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
STD = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)


def to_tensor(im):
    im = im.resize((W, H), Image.BICUBIC)
    t = torch.from_numpy(np.asarray(im, np.float32) / 255.0).permute(2, 0, 1)
    return (t - MEAN) / STD


mp = load_map(opt.root, opt.map)
side_px = opt.tile_m / mp["gsd"]


class Tiles(torch.utils.data.Dataset):
    def __init__(self):
        step = opt.stride / mp["gsd"]
        xs = np.arange(side_px / 2, mp["W"] - side_px / 2, step)
        ys = np.arange(side_px / 2, mp["H"] - side_px / 2, step)
        self.c = np.array([(x, y) for y in ys for x in xs])

    def __len__(self):
        return len(self.c)

    def __getitem__(self, i):
        x, y = self.c[i]
        r = side_px / 2
        a = mp["img"][int(round(y - r)):int(round(y + r)), int(round(x - r)):int(round(x + r))]
        return to_tensor(Image.fromarray(np.ascontiguousarray(a)))


class Frames(torch.utils.data.Dataset):
    def __init__(self):
        self.f = []
        for s in sorted(glob.glob(os.path.join(opt.root, opt.seqs))):
            for f in list_frames(s):
                f["seq"] = os.path.basename(s)
                self.f.append(f)

    def __len__(self):
        return len(self.f)

    def __getitem__(self, i):
        im = Image.open(self.f[i]["path"]).convert("RGB").transpose(Image.ROTATE_270)  # 90 deg CW
        w, h = im.size                                    # north-up: w spans frame_w_m metres E-W
        s = int(round(w * min(1.0, opt.tile_m / opt.frame_w_m)))
        l, t = (w - s) // 2, (h - s) // 2
        return to_tensor(im.crop((l, t, l + s, t + s)))


@torch.no_grad()
def extract(ds, view):
    dl = torch.utils.data.DataLoader(ds, batch_size=opt.batch, num_workers=opt.workers)
    out = []
    for x in dl:
        ff = 0
        for flip in (False, True):
            xi = (torch.flip(x, [3]) if flip else x).cuda()
            o = model(xi, None)[0] if view == "sat" else model(None, xi)[1]
            ff = ff + o[1].float()
        if ff.dim() == 3:
            ff = ff / (ff.norm(dim=1, keepdim=True) * np.sqrt(ff.shape[2]))
            ff = ff.flatten(1)
        else:
            ff = ff / ff.norm(dim=1, keepdim=True)
        out.append(ff.cpu().numpy().astype(np.float16))
    return np.concatenate(out)


t0 = time.time()
tiles, frames = Tiles(), Frames()
print(f"[INFO] {len(tiles)} tiles ({opt.tile_m:.0f} m, stride {opt.stride:.0f} m), {len(frames)} frames")
if opt.gallery_from:
    old = np.load(opt.gallery_from)
    assert len(old["gallery_f"]) == len(tiles), "gallery grid differs from the cached one"
    gf = old["gallery_f"]
else:
    gf = extract(tiles, "sat")
print(f"[INFO] gallery done ({time.time() - t0:.0f}s)")
qf = extract(frames, "drone")
print(f"[INFO] query done ({time.time() - t0:.0f}s)")

g_lon, g_lat = px_to_lonlat(mp, tiles.c[:, 0], tiles.c[:, 1])
gx, gy = lonlat_to_xy(mp, g_lon, g_lat)
qx, qy = lonlat_to_xy(mp, np.array([f["lon"] for f in frames.f]), np.array([f["lat"] for f in frames.f]))
np.savez_compressed(opt.out, gallery_f=gf, gallery_xy=np.stack([gx, gy], 1), query_f=qf,
                    query_xy=np.stack([qx, qy], 1), query_t=np.array([f["t"] for f in frames.f]),
                    query_seq=np.array([f["seq"] for f in frames.f]),
                    meta=np.array(str(vars(opt))))
print(f"[INFO] wrote {opt.out} ({time.time() - t0:.0f}s)")

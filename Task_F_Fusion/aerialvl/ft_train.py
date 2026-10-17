# -*- coding: utf-8 -*-
"""
ft_train.py — F7: fine-tune a DenseUAV retrieval checkpoint on AerialVL NON-test flights.

Pairs: query crop of a frame (ft_prepare.py) <-> map tile of tile_m metres centred at GNSS + calibration offset
(tile - GNSS bias of the camera, F5-02). Loss: symmetric InfoNCE on the SAME L2-normalised descriptor that
aerialvl_extract.py uses at test time. Negatives: the other pairs of the batch plus --n_extra random tiles
around the training area; pairs whose GNSS are closer than --pos_m are masked (2 Hz frames overlap heavily).
The model stays in eval mode (frozen BatchNorm statistics, no dropout) while its weights are trained.
Model selection: after every epoch, top-1 <= 50 m on the --val_seqs flights against the FULL gallery (28 340 tiles).
Output: --out_dir laid out like a checkpoint folder (opts.yaml, code, net_119.pth = best epoch), so
aerialvl_extract.py runs on it unchanged.
usage (DenseUAV venv): python ft_train.py --ckpt_dir <.../checkpoints/lpn> --out_dir ft/lpn_s666 --tag dev
"""
import argparse, json, math, os, shutil, sys, time
import numpy as np
import torch
import torch.nn.functional as Fn
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from aerialvl_io import load_map, lonlat_to_px, crop, EARTH_R  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--ckpt_dir", required=True)
p.add_argument("--out_dir", required=True)
p.add_argument("--data", default=os.path.join(HERE, "ft", "nontest_crops.npz"))
p.add_argument("--root", default=os.path.join(HERE, "..", "..", "datasets", "AerialVL", "extracted"))
p.add_argument("--train_seqs", default="2023-03-16")
p.add_argument("--val_seqs", default="2023-03-11")
p.add_argument("--offset", default="-2.47,-23.41", help="tile - GNSS (east, north) metres, measured on val (F5-02)")
p.add_argument("--tile_m", default=200.0, type=float)
p.add_argument("--stride", default=25.0, type=float)
p.add_argument("--epochs", default=8, type=int)
p.add_argument("--iters", default=150, type=int, help="iterations per epoch")
p.add_argument("--batch", default=24, type=int)
p.add_argument("--n_extra", default=24, type=int)
p.add_argument("--lr", default=1e-5, type=float)
p.add_argument("--wd", default=0.01, type=float)
p.add_argument("--tau", default=0.05, type=float)
p.add_argument("--pos_m", default=60.0, type=float)
p.add_argument("--jitter_m", default=5.0, type=float)
p.add_argument("--seed", default=0, type=int)
opt = p.parse_args()
for k in ("out_dir", "data", "root", "ckpt_dir"):
    setattr(opt, k, os.path.abspath(getattr(opt, k)))
assert "2023-03-18" not in opt.train_seqs + opt.val_seqs, "test-day flights are not allowed"
torch.manual_seed(opt.seed)
rng = np.random.default_rng(opt.seed)

# ---- checkpoint folder copy (code + opts; weights written later)
os.makedirs(opt.out_dir, exist_ok=True)
for f in os.listdir(opt.ckpt_dir):
    s, d = os.path.join(opt.ckpt_dir, f), os.path.join(opt.out_dir, f)
    if f.endswith((".pth", ".mat", ".log", ".txt")) or os.path.exists(d):
        continue
    (shutil.copytree if os.path.isdir(s) else shutil.copy)(s, d)
os.chdir(opt.ckpt_dir)
sys.path.insert(0, opt.ckpt_dir)
import yaml  # noqa: E402
from tool.utils import load_network  # noqa: E402

cfg = argparse.Namespace(checkpoint="net_119.pth")
for k, v in yaml.safe_load(open("opts.yaml")).items():
    setattr(cfg, k, v)
model = load_network(cfg).cuda().eval()
H, W = cfg.h, cfg.w
MEAN = torch.tensor([0.485, 0.456, 0.406], device="cuda").view(1, 3, 1, 1)
STD = torch.tensor([0.229, 0.224, 0.225], device="cuda").view(1, 3, 1, 1)


def norm_desc(o):
    """Exactly aerialvl_extract.py: LPN-style (B, C, blocks) -> per-block norm / sqrt(blocks), flatten."""
    if o.dim() == 3:
        return (o / (o.norm(dim=1, keepdim=True) * math.sqrt(o.shape[2]))).flatten(1)
    return o / o.norm(dim=1, keepdim=True)


def desc(x):  # x uint8 (B, H, W, 3) on gpu
    x = (x.permute(0, 3, 1, 2).float() / 255.0 - MEAN) / STD
    return norm_desc(model(x, None)[0][1].float())


# ---- data
mp = load_map(opt.root, "large")
lat_c = (mp["lat0"] + mp["lat1"]) / 2


def xy_to_px(xy):
    lon = mp["lon0"] + np.degrees(xy[..., 0] / (EARTH_R * math.cos(math.radians(lat_c))))
    lat = mp["lat0"] + np.degrees(xy[..., 1] / EARTH_R)
    return np.stack(lonlat_to_px(mp, lon, lat), -1)


def tile_at(xy, side_m):
    x, y = xy_to_px(np.asarray(xy, float))
    r = int(round(side_m / mp["gsd"] / 2))
    return np.asarray(Image.fromarray(crop(mp, x, y, r)).resize((W, H), Image.BICUBIC))


D = np.load(opt.data)
seq = D["seq"]
tr = np.flatnonzero(np.char.startswith(seq.astype(str), tuple(opt.train_seqs.split(","))))
va = np.flatnonzero(np.char.startswith(seq.astype(str), tuple(opt.val_seqs.split(","))))
off = np.array([float(v) for v in opt.offset.split(",")])
qxy, qimg = D["xy"], D["img"]
lo, hi = qxy[tr].min(0) - 1000, qxy[tr].max(0) + 1000
print(f"[INFO] train {len(tr)} frames ({opt.train_seqs}), val {len(va)} frames ({opt.val_seqs})")


def aug_query(im):
    pil = Image.fromarray(im)
    s = rng.uniform(0.8, 1.0) * pil.size[0]
    x0, y0 = rng.uniform(0, pil.size[0] - s, 2)
    pil = pil.crop((x0, y0, x0 + s, y0 + s)).resize((W, H), Image.BICUBIC)
    a = np.asarray(pil, np.float32)
    a = (a - a.mean()) * rng.uniform(0.7, 1.3) + a.mean() * rng.uniform(0.7, 1.3)  # contrast, brightness
    g = a.mean(2, keepdims=True)
    a = g + (a - g) * rng.uniform(0.7, 1.3)                                         # saturation
    return np.clip(a, 0, 255).astype(np.uint8)


def batch():
    i = rng.choice(tr, opt.batch, replace=False)
    q = np.stack([aug_query(qimg[k]) for k in i])
    pos = qxy[i] + off + rng.normal(0, opt.jitter_m, (len(i), 2))
    ex = rng.uniform(lo, hi, (opt.n_extra, 2))
    s = np.stack([tile_at(c, opt.tile_m * rng.uniform(0.9, 1.1)) for c in pos]
                 + [tile_at(c, opt.tile_m) for c in ex])
    cxy = np.concatenate([qxy[i] + off, ex])
    neg_ok = np.hypot(*(qxy[i][:, None] + off - cxy[None]).transpose(2, 0, 1)) >= opt.pos_m  # (B, B + extra)
    np.fill_diagonal(neg_ok[:, :opt.batch], False)
    return torch.from_numpy(q).cuda(), torch.from_numpy(s).cuda(), torch.from_numpy(neg_ok).cuda()


# ---- validation: full gallery, same grid as aerialvl_extract.py
side_px = opt.tile_m / mp["gsd"]
step = opt.stride / mp["gsd"]
gc = np.array([(x, y) for y in np.arange(side_px / 2, mp["H"] - side_px / 2, step)
               for x in np.arange(side_px / 2, mp["W"] - side_px / 2, step)])
gl = mp["lon0"] + gc[:, 0] / mp["W"] * (mp["lon1"] - mp["lon0"])
gt = mp["lat0"] - gc[:, 1] / mp["H"] * (mp["lat0"] - mp["lat1"])
gxy = np.stack([np.radians(gl - mp["lon0"]) * EARTH_R * math.cos(math.radians(lat_c)),
                np.radians(gt - mp["lat0"]) * EARTH_R], 1)


@torch.no_grad()
def feats(imgs_fn, n, bs=64):
    out = []
    for a in range(0, n, bs):
        x = torch.from_numpy(np.stack([imgs_fn(k) for k in range(a, min(n, a + bs))])).cuda()
        x = (x.permute(0, 3, 1, 2).float() / 255.0 - MEAN) / STD
        with torch.autocast("cuda", dtype=torch.float16):   # feature(img) + feature(hflip(img)), as at test time
            f = norm_desc(model(x, None)[0][1].float() + model(torch.flip(x, [3]), None)[0][1].float())
        out.append(f.half())
    return torch.cat(out)


def gallery_tile(k):
    x, y = gc[k]
    r = side_px / 2
    a = mp["img"][int(round(y - r)):int(round(y + r)), int(round(x - r)):int(round(x + r))]
    return np.asarray(Image.fromarray(np.ascontiguousarray(a)).resize((W, H), Image.BICUBIC))


def evaluate():
    model.eval()
    gf = feats(gallery_tile, len(gc))
    qf = feats(lambda k: np.asarray(Image.fromarray(qimg[va[k]]).resize((W, H), Image.BICUBIC)), len(va))
    S = (qf.float() @ gf.float().T)
    top = S.topk(10, 1).indices.cpu().numpy()
    e1 = np.hypot(*(gxy[top[:, 0]] - qxy[va]).T)
    e1c = np.hypot(*(gxy[top[:, 0]] - off - qxy[va]).T)
    ek = np.hypot(*(gxy[top] - qxy[va][:, None]).transpose(2, 0, 1)).min(1)
    return {"top1_50": float((e1 <= 50).mean()), "top1_50_calib": float((e1c <= 50).mean()),
            "top10_50": float((ek <= 50).mean()), "median": float(np.median(e1)), "p95": float(np.percentile(e1, 95))}


params = [q for q in model.parameters() if q.requires_grad]
optim = torch.optim.AdamW(params, lr=opt.lr, weight_decay=opt.wd)
sched = torch.optim.lr_scheduler.CosineAnnealingLR(optim, opt.epochs * opt.iters)
scaler = torch.cuda.amp.GradScaler()
log = {"opt": vars(opt), "epochs": []}
t0 = time.time()
r = evaluate()
log["epochs"].append({"epoch": 0, "loss": None, **r})
best, best_ep = r["top1_50"], 0
torch.save(model.state_dict(), os.path.join(opt.out_dir, "net_119.pth"))
print(f"[EP 0] zero-shot val {json.dumps(r)} ({time.time() - t0:.0f}s)", flush=True)
for ep in range(1, opt.epochs + 1):
    losses = []
    for it in range(opt.iters):
        q, s, ok = batch()
        with torch.autocast("cuda", dtype=torch.float16):
            fq, fs = desc(q), desc(s)
        logits = (fq.float() @ fs.float().T) / opt.tau                     # (B, B + extra)
        lab = torch.arange(len(fq), device="cuda")
        keep = ok.clone()
        keep[lab, lab] = True
        lq = logits.masked_fill(~keep, -1e4)
        ls = logits[:, :len(fq)].T.masked_fill(~keep[:, :len(fq)].T, -1e4)
        loss = 0.5 * (Fn.cross_entropy(lq, lab) + Fn.cross_entropy(ls, lab))
        optim.zero_grad(set_to_none=True)
        scaler.scale(loss).backward()
        scaler.step(optim)
        scaler.update()
        sched.step()
        losses.append(loss.item())
    r = evaluate()
    log["epochs"].append({"epoch": ep, "loss": float(np.mean(losses)), **r})
    if r["top1_50"] > best:
        best, best_ep = r["top1_50"], ep
        torch.save(model.state_dict(), os.path.join(opt.out_dir, "net_119.pth"))
    print(f"[EP {ep}] loss {np.mean(losses):.3f} val {json.dumps(r)} ({time.time() - t0:.0f}s)", flush=True)
log["best_epoch"], log["best_top1_50"] = best_ep, best
json.dump(log, open(os.path.join(opt.out_dir, "ft_log.json"), "w"), indent=1)
print(f"[INFO] best epoch {best_ep}: val top-1 <= 50 m {best:.3f} -> {opt.out_dir}/net_119.pth")

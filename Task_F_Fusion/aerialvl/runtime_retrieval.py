# -*- coding: utf-8 -*-
"""
runtime_retrieval.py — F8-02: retrieval cost per query frame (DenseUAV venv, GPU).
- descriptor: batch 2 (some heads squeeze a batch of 1; the batch-2 latency is an upper bound for one frame), 224 x 224, feature(img) + feature(hflip(img)) exactly as aerialvl_extract.py, fp32, CUDA synced
- Top-K search: one query against the 28 340-tile gallery (numpy fp32 matmul + argpartition, 1 CPU thread)
- parameter count of each head
usage: python runtime_retrieval.py   (writes ../paper_tables/runtime_retrieval.json)
"""
import argparse, json, os, sys, time
import numpy as np
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
C = "/home/aclab_pc/Desktop/Paper_UAV/Paper_UAV/Task_F_Fusion/aerialvl/ft"
out = {}
for head in ("baseline", "lpn", "fsra"):
    d = os.path.join(C, f"{head}_s666")
    os.chdir(d)
    sys.path.insert(0, d)
    for m in [k for k in list(sys.modules) if k.split(".")[0] in ("tool", "models", "losses", "datasets", "optimizers")]:
        del sys.modules[m]
    import yaml
    from tool.utils import load_network
    cfg = argparse.Namespace(checkpoint="net_119.pth")
    for k, v in yaml.safe_load(open("opts.yaml")).items():
        setattr(cfg, k, v)
    model = load_network(cfg).eval().cuda()
    sys.path.remove(d)
    x = torch.randn(2, 3, cfg.h, cfg.w, device="cuda")
    with torch.no_grad():
        for _ in range(20):
            model(x, None); model(torch.flip(x, [3]), None)
        torch.cuda.synchronize()
        ts = []
        for _ in range(200):
            t0 = time.perf_counter()
            f = model(x, None)[0][1] + model(torch.flip(x, [3]), None)[0][1]
            torch.cuda.synchronize()
            ts.append((time.perf_counter() - t0) * 1e3)
    dim = int(np.prod(f.shape[1:]))
    out[head] = {"batch": 2, "gpu_busy_other_process": False, "desc_ms_mean": float(np.mean(ts)), "desc_ms_p95": float(np.percentile(ts, 95)),
                 "params_M": sum(p.numel() for p in model.parameters()) / 1e6, "dim": dim}
    print(head, out[head], flush=True)
    del model
    torch.cuda.empty_cache()

torch.set_num_threads(1)
os.environ["OMP_NUM_THREADS"] = "1"
for dim in sorted({v["dim"] for v in out.values()}):
    G = np.random.randn(28340, dim).astype(np.float32)
    q = np.random.randn(dim).astype(np.float32)
    ts = []
    for _ in range(50):
        t0 = time.perf_counter()
        s = G @ q
        p = np.argpartition(-s, 10)[:10]
        p[np.argsort(-s[p])]
        ts.append((time.perf_counter() - t0) * 1e3)
    out[f"topk_search_dim{dim}"] = {"ms_mean": float(np.mean(ts)), "ms_p95": float(np.percentile(ts, 95)), "gallery": 28340}
    print(f"top-K search dim {dim}: {np.mean(ts):.2f} ms", flush=True)
json.dump(out, open(os.path.join(HERE, "..", "paper_tables", "runtime_retrieval.json"), "w"), indent=1)

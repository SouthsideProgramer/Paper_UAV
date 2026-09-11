"""
Muc 5.1: giai ma trong tam co trong so (weighted centroid), hau xu ly
tren pytorch_result_1.mat da co san -- khong can train lai.

So sanh sai so (met) giua:
  - top-1 (nhu evaluateMA.py goc)
  - trong tam co trong so cua top-K gallery (K, tau la sieu tham so)

Ground truth cua query = tra theo id lop cua chinh no trong Dense_GPS_ALL.txt
(giong het evaluateMA.py, de so sanh cong bang -- xem Muc 4/5 cua report ve
han che cua ground truth nay).
"""
import argparse
import json
import math
import os

import numpy as np
import scipy.io
import torch
from torchvision import datasets


def latlog2meter(lata, loga, latb, logb):
    EARTH_RADIUS = 6378.137
    PI = math.pi
    lat_a = lata * PI / 180
    lat_b = latb * PI / 180
    a = lat_a - lat_b
    b = loga * PI / 180 - logb * PI / 180
    dis = 2 * math.asin(math.sqrt(math.sin(a / 2) ** 2 + math.cos(lat_a) * math.cos(lat_b) * math.sin(b / 2) ** 2))
    return EARTH_RADIUS * dis * 1000


def load_config(root_dir):
    config = {}
    with open(os.path.join(root_dir, "Dense_GPS_ALL.txt")) as f:
        for line in f:
            parts = line.split(" ")
            key = parts[0].split("/")[-2]
            E = float(parts[1].split("E")[-1])
            N = float(parts[2].split("N")[-1])
            config[key] = (E, N)
    return config


def evaluate_checkpoint(ckpt_dir, root_dir, Ks=(1, 3, 5, 10), tau=0.05):
    config = load_config(root_dir)
    test_dir = os.path.join(root_dir, "test")
    image_datasets = {
        x: datasets.ImageFolder(os.path.join(test_dir, x))
        for x in ["gallery_satellite", "query_drone"]
    }
    gallery_paths = [p for p, _ in image_datasets["gallery_satellite"].imgs]
    query_paths = [p for p, _ in image_datasets["query_drone"].imgs]
    gallery_class = [p.split("/")[-2] for p in gallery_paths]
    query_class = [p.split("/")[-2] for p in query_paths]
    gallery_pos = np.array([config[c] for c in gallery_class])  # (Ng, 2) = (E, N)

    result = scipy.io.loadmat(os.path.join(ckpt_dir, "pytorch_result_1.mat"))
    query_f = torch.FloatTensor(result["query_f"])
    query_label = result["query_label"][0]
    gallery_f = torch.FloatTensor(result["gallery_f"])
    gallery_label = result["gallery_label"][0]

    scores_all = torch.mm(query_f, gallery_f.t()).numpy()  # (Nq, Ng), cosine-like (features normalized upstream?)

    out = {"top1_median": None, "top1_p90": None}
    n = len(query_paths)

    errs_top1 = np.zeros(n)
    errs_centroid = {K: np.zeros(n) for K in Ks}

    for i in range(n):
        gt_E, gt_N = config[query_class[i]]
        scores = scores_all[i]
        order = np.argsort(scores)[::-1]  # lon -> nho

        # top-1
        top1_idx = order[0]
        errs_top1[i] = latlog2meter(gt_N, gt_E, gallery_pos[top1_idx][1], gallery_pos[top1_idx][0])

        for K in Ks:
            idxK = order[:K]
            sK = scores[idxK]
            # softmax trong so theo score/tau (chi tren top-K, khong phai toan bo gallery)
            w = np.exp((sK - sK.max()) / tau)
            w = w / w.sum()
            pred_E = np.sum(w * gallery_pos[idxK, 0])
            pred_N = np.sum(w * gallery_pos[idxK, 1])
            errs_centroid[K][i] = latlog2meter(gt_N, gt_E, pred_N, pred_E)

    def stats(errs):
        return {
            "median": float(np.median(errs)),
            "p90": float(np.percentile(errs, 90)),
            "p95": float(np.percentile(errs, 95)),
            "mean": float(np.mean(errs)),
        }

    out["top1"] = stats(errs_top1)
    out["centroid"] = {K: stats(errs_centroid[K]) for K in Ks}
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root_dir", default="/home/internship/thang2/DenseUAV")
    ap.add_argument("--tau", type=float, default=0.05)
    args = ap.parse_args()

    ckpt_root = os.path.join(args.root_dir, "checkpoints")
    configs = ["baseline_vits_single", "vits_lpn", "vits_fsra", "resnet50_single"]

    all_results = {}
    for name in configs:
        ckpt_dir = os.path.join(ckpt_root, name)
        mat_path = os.path.join(ckpt_dir, "pytorch_result_1.mat")
        if not os.path.exists(mat_path):
            print(f"[skip] {name}: chua co pytorch_result_1.mat")
            continue
        print(f"=== {name} ===")
        res = evaluate_checkpoint(ckpt_dir, args.root_dir, tau=args.tau)
        all_results[name] = res
        print("  top-1        : median={median:.2f}m p90={p90:.2f}m p95={p95:.2f}m".format(**res["top1"]))
        for K, s in res["centroid"].items():
            print(f"  centroid K={K:<2}: median={s['median']:.2f}m p90={s['p90']:.2f}m p95={s['p95']:.2f}m")

    with open(os.path.join(args.root_dir, "weighted_centroid_results.json"), "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print("\nsaved weighted_centroid_results.json")

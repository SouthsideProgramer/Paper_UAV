# -*- coding: utf-8 -*-
"""
spatial_confidence_gating.py — Spatial Confidence Gating (Task K5 / Section 8.1)

Addresses the fundamental failure of unconstrained top-K centroid decoding:
Feature-space neighbours are often NOT geographic neighbours.

Spatial Confidence Gating Algorithm:
1. Spatial Anchor & Radius Filtering:
   Anchor on top-1 candidate g(1). Discard any candidate i in top-K with
   dist(g(i), g(1)) > rho_gate (e.g. rho_gate = 3s ~ 60m).
2. Margin Confidence Check:
   If margin (s1 - s2) >= tau_margin (model is highly decisive), return top-1 directly.
3. Fallback Safety ("Never Worse Than Top-1"):
   If only g(1) survives the spatial gate, return top-1.
   If multiple geographically close candidates survive, blend their coordinates using softmax weights.

Evaluation across all 4 baseline checkpoints:
- Plain Top-1 decoding
- Unconstrained Weighted Centroid (K=3, 5, 10)
- Spatially Gated Centroid (rho_gate in {40, 60, 100}m)
"""

from __future__ import print_function, division
import os
import sys
import math
import json
import argparse
import numpy as np
import scipy.io

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def latlog2meter(lata, loga, latb, logb):
    EARTH_RADIUS = 6378.137
    PI = math.pi
    lat_a = lata * PI / 180.0
    lat_b = latb * PI / 180.0
    a = lat_a - lat_b
    b = (loga - logb) * PI / 180.0
    dis = 2.0 * math.asin(
        math.sqrt(
            math.pow(math.sin(a / 2.0), 2) +
            math.cos(lat_a) * math.cos(lat_b) * math.pow(math.sin(b / 2.0), 2)
        )
    )
    return EARTH_RADIUS * dis * 1000.0


def load_gps_config(gps_path):
    if not os.path.exists(gps_path):
        candidates = [
            os.path.join(CURRENT_DIR, 'datasets', 'DenseUAV', 'Dense_GPS_ALL.txt'),
            os.path.join(CURRENT_DIR, 'Dense_GPS_ALL.txt'),
            os.path.join('datasets', 'DenseUAV', 'Dense_GPS_ALL.txt'),
        ]
        for c in candidates:
            if os.path.exists(c):
                gps_path = c
                break

    gps_dict = {}
    with open(gps_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                class_key = parts[0].replace('\\', '/').split('/')[-2]
                lon = float(parts[1].split('E')[-1])
                lat = float(parts[2].split('N')[-1])
                gps_dict[class_key] = (lon, lat)
                try:
                    gps_dict[int(class_key)] = (lon, lat)
                except ValueError:
                    pass
    return gps_dict


def compute_metrics(errs):
    return {
        'median': float(np.median(errs)),
        'mean': float(np.mean(errs)),
        'p90': float(np.percentile(errs, 90)),
        'p95': float(np.percentile(errs, 95)),
        'gfr100': float(np.mean(errs > 100.0) * 100.0)
    }


def evaluate_spatial_gating(mat_path, gps_dict, Ks=[3, 5, 10], rho_gates=[40.0, 60.0, 100.0], tau_softmax=0.05, tau_margin=0.05):
    mat = scipy.io.loadmat(mat_path)
    query_f = mat['query_f']
    gallery_f = mat['gallery_f']
    query_label = mat['query_label'].reshape(-1)
    gallery_label = mat['gallery_label'].reshape(-1)

    # Normalize features
    q_norm = np.linalg.norm(query_f, axis=1, keepdims=True)
    q_norm[q_norm == 0] = 1.0
    query_f = query_f / q_norm

    g_norm = np.linalg.norm(gallery_f, axis=1, keepdims=True)
    g_norm[g_norm == 0] = 1.0
    gallery_f = gallery_f / g_norm

    # Pre-extract gallery coordinates
    gallery_coords = np.array([gps_dict.get(lbl, (0.0, 0.0)) for lbl in gallery_label])  # (N_gallery, 2) -> (lon, lat)

    num_queries = len(query_label)
    max_K = max(Ks)

    # Results containers
    errs_top1 = np.zeros(num_queries)
    errs_unconstrained = {K: np.zeros(num_queries) for K in Ks}
    errs_gated = {f"K{K}_rho{int(rho)}": np.zeros(num_queries) for K in Ks for rho in rho_gates}

    batch_size = 256
    for start_idx in range(0, num_queries, batch_size):
        end_idx = min(start_idx + batch_size, num_queries)
        q_batch = query_f[start_idx:end_idx]
        sim_batch = np.dot(q_batch, gallery_f.T)

        for b in range(end_idx - start_idx):
            q_i = start_idx + b
            sims = sim_batch[b]
            order = np.argsort(sims)[::-1]

            q_lbl = query_label[q_i]
            q_lon, q_lat = gps_dict.get(q_lbl, (0.0, 0.0))

            # 1. Plain Top-1
            top1_idx = order[0]
            top1_lon, top1_lat = gallery_coords[top1_idx]
            errs_top1[q_i] = latlog2meter(q_lat, q_lon, top1_lat, top1_lon)

            top1_score = sims[top1_idx]
            top2_score = sims[order[1]] if len(order) > 1 else top1_score
            margin = float(top1_score - top2_score)

            # 2. Unconstrained Weighted Centroid (as in Section 5.1)
            for K in Ks:
                idx_K = order[:K]
                scores_K = sims[idx_K]
                w = np.exp((scores_K - np.max(scores_K)) / tau_softmax)
                w = w / np.sum(w)
                pred_lon = np.sum(w * gallery_coords[idx_K, 0])
                pred_lat = np.sum(w * gallery_coords[idx_K, 1])
                errs_unconstrained[K][q_i] = latlog2meter(q_lat, q_lon, pred_lat, pred_lon)

            # 3. Spatial Confidence Gating (Section 8.1)
            for K in Ks:
                idx_K = order[:K]
                scores_K = sims[idx_K]
                coords_K = gallery_coords[idx_K]

                for rho in rho_gates:
                    gate_key = f"K{K}_rho{int(rho)}"

                    # If model is already very decisive (high margin), directly use top-1
                    if margin >= tau_margin:
                        errs_gated[gate_key][q_i] = errs_top1[q_i]
                        continue

                    # Filter candidates: keep only those within rho_gate meters of top-1 anchor
                    survived_indices = []
                    for i_cand in range(K):
                        c_lon, c_lat = coords_K[i_cand]
                        dist_to_anchor = latlog2meter(top1_lat, top1_lon, c_lat, c_lon)
                        if dist_to_anchor <= rho:
                            survived_indices.append(i_cand)

                    if len(survived_indices) <= 1:
                        # Fallback to top-1 (Never Worse Than Top-1)
                        errs_gated[gate_key][q_i] = errs_top1[q_i]
                    else:
                        sub_scores = scores_K[survived_indices]
                        sub_coords = coords_K[survived_indices]
                        w = np.exp((sub_scores - np.max(sub_scores)) / tau_softmax)
                        w = w / np.sum(w)
                        pred_lon = np.sum(w * sub_coords[:, 0])
                        pred_lat = np.sum(w * sub_coords[:, 1])
                        errs_gated[gate_key][q_i] = latlog2meter(q_lat, q_lon, pred_lat, pred_lon)

    results = {
        'top1': compute_metrics(errs_top1),
        'unconstrained_centroid': {f"K={K}": compute_metrics(errs_unconstrained[K]) for K in Ks},
        'spatial_confidence_gated': {k: compute_metrics(errs_gated[k]) for k in errs_gated}
    }
    return results


def main():
    parser = argparse.ArgumentParser(description='Task K5: Spatial Confidence Gating Evaluation')
    parser.add_argument('--checkpoints_dir', default='', type=str, help='Path to checkpoints directory')
    parser.add_argument('--gps_path', default='', type=str, help='Path to Dense_GPS_ALL.txt')
    parser.add_argument('--output_json', default='spatial_gating_results.json', type=str, help='Output JSON path')
    args = parser.parse_args()

    ckpt_dir = args.checkpoints_dir if args.checkpoints_dir else os.path.join(CURRENT_DIR, 'checkpoints')
    gps_path = args.gps_path if args.gps_path else os.path.join(CURRENT_DIR, 'datasets', 'DenseUAV', 'Dense_GPS_ALL.txt')
    gps_dict = load_gps_config(gps_path)

    models = [
        ('vits_lpn', 'ViTS-224 + LPN'),
        ('vits_fsra', 'ViTS-224 + FSRA'),
        ('baseline_vits_single', 'ViTS-224 + SingleBranch'),
        ('resnet50_single', 'ResNet-50 + SingleBranchCNN'),
    ]

    all_results = {}
    print("\n" + "=" * 90)
    print("        SPATIAL CONFIDENCE GATING EVALUATION (Task K5 / Section 8.1)        ")
    print("=" * 90)

    for m_key, m_name in models:
        mat_path = os.path.join(ckpt_dir, m_key, 'pytorch_result_1.mat')
        if not os.path.exists(mat_path):
            print(f"[SKIP] {m_key}: pytorch_result_1.mat not found")
            continue

        print(f"\n>>> Evaluating: {m_name} ({m_key})")
        res = evaluate_spatial_gating(mat_path, gps_dict)
        all_results[m_key] = res

        t1 = res['top1']
        print(f"  * [Plain Top-1]:          Median = {t1['median']:>5.2f}m | Mean = {t1['mean']:>6.2f}m | p90 = {t1['p90']:>6.2f}m | p95 = {t1['p95']:>6.2f}m | GFR@100 = {t1['gfr100']:>5.2f}%")

        # Unconstrained centroid vs Spatial Gated centroid
        for K in [3, 5, 10]:
            unc = res['unconstrained_centroid'][f'K={K}']
            gated = res['spatial_confidence_gated'][f'K{K}_rho60']
            print(f"  * [K={K:<2} Centroid Unconstrained]: Median = {unc['median']:>5.2f}m | Mean = {unc['mean']:>6.2f}m | p90 = {unc['p90']:>6.2f}m | p95 = {unc['p95']:>6.2f}m | GFR@100 = {unc['gfr100']:>5.2f}%")
            print(f"  * [K={K:<2} Gated (rho=60m, tau=0.05)]: Median = {gated['median']:>5.2f}m | Mean = {gated['mean']:>6.2f}m | p90 = {gated['p90']:>6.2f}m | p95 = {gated['p95']:>6.2f}m | GFR@100 = {gated['gfr100']:>5.2f}%")

    # Save output JSON
    with open(args.output_json, 'w') as f:
        json.dump(all_results, f, indent=4)
    print("\n" + "=" * 90)
    print(f"[SUCCESS] Saved Spatial Confidence Gating results to: {args.output_json}")
    print("=" * 90 + "\n")


if __name__ == '__main__':
    main()

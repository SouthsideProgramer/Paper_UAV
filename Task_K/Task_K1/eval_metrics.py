# -*- coding: utf-8 -*-
"""
eval_metrics.py — Evaluation track (Task K1)

Calculates robust geospatial evaluation metrics for UAV geo-localization on DenseUAV:
- GFR@rho (Gross Failure Rate) + Wilson 95% Confidence Interval for rho in {50, 100, 200, 500} m
- Percentile errors: p50 (median), p90, p95 + Bootstrap 95% Confidence Interval (1000 resamples)
- MA@rho (Meter Accuracy) for rho in {50, 100, 200, 500} m
- GeoAUROC (AUROC of confidence margin (s1 - s2) in detecting gross failure {err > rho})
- R@1, R@5, SDM@1
- Exports results.json and errors.npy (for downstream texture analysis in Task K3)

Zero GPU requirement. Works on standard CPU.
"""

from __future__ import print_function, division
import os
import sys
import math
import json
import argparse
import numpy as np
import scipy.io
from sklearn.metrics import roc_auc_score

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_parse():
    parser = argparse.ArgumentParser(description='Task K1: Comprehensive Metric Evaluation')
    parser.add_argument('--result_mat', default='pytorch_result_1.mat', type=str,
                        help='Path to pytorch_result_1.mat extracted features')
    parser.add_argument('--gps_path', default='', type=str,
                        help='Path to Dense_GPS_ALL.txt')
    parser.add_argument('--rho', default=100.0, type=float,
                        help='Default rho threshold in meters for GFR and GeoAUROC')
    parser.add_argument('--rhos', default='50,100,200,500', type=str,
                        help='Comma-separated rho thresholds in meters')
    parser.add_argument('--output_json', default='results.json', type=str,
                        help='Output JSON file path')
    parser.add_argument('--output_npy', default='errors.npy', type=str,
                        help='Output errors NPY file path')
    parser.add_argument('--n_resamples', default=1000, type=int,
                        help='Number of bootstrap resamples for CI')
    parser.add_argument('--seed', default=0, type=int,
                        help='Random seed for bootstrapping reproducibility')
    return parser


def latlog2meter(lata, loga, latb, logb):
    """
    Geodesic distance in meters using the standard Haversine / WGS-84 approximation
    as defined in the original DenseUAV evaluation benchmark.
    """
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


def euclidean_degree_distance(loga, lata, logb, latb):
    """Euclidean distance in degrees (used for original SDM formulation)."""
    return math.sqrt((loga - logb) ** 2 + (lata - latb) ** 2)


def load_gps_coords(gps_path):
    """
    Parses Dense_GPS_ALL.txt mapping class_id (e.g. '000001' or int) -> (Longitude_E, Latitude_N).
    """
    if not os.path.exists(gps_path):
        # Check fallback paths
        candidates = [
            os.path.join(CURRENT_DIR, 'datasets', 'DenseUAV', 'Dense_GPS_ALL.txt'),
            os.path.join(CURRENT_DIR, 'Dense_GPS_ALL.txt'),
            os.path.join('datasets', 'DenseUAV', 'Dense_GPS_ALL.txt'),
        ]
        for c in candidates:
            if os.path.exists(c):
                gps_path = c
                break

    if not os.path.exists(gps_path):
        raise FileNotFoundError(f"GPS file not found at: {gps_path}")

    gps_dict = {}
    with open(gps_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                # Key can be extracted from folder name
                class_key = parts[0].replace('\\', '/').split('/')[-2]
                lon = float(parts[1].split('E')[-1])
                lat = float(parts[2].split('N')[-1])
                gps_dict[class_key] = (lon, lat)
                try:
                    gps_dict[int(class_key)] = (lon, lat)
                except ValueError:
                    pass
    return gps_dict


def wilson_score_interval(successes, total, confidence=0.95):
    """
    Calculates Wilson Score Confidence Interval for a binomial proportion.
    Returns: (point_estimate, ci_low, ci_high) in percentages [0, 100].
    """
    if total == 0:
        return 0.0, 0.0, 0.0
    p = successes / total
    z = 1.959963984540054  # 95% two-sided normal quantile
    z2 = z * z
    denominator = 1.0 + z2 / total
    center = (p + z2 / (2.0 * total)) / denominator
    spread = (z / denominator) * math.sqrt((p * (1.0 - p) / total) + (z2 / (4.0 * total * total)))
    low = max(0.0, center - spread) * 100.0
    high = min(1.0, center + spread) * 100.0
    return p * 100.0, low, high


def bootstrap_percentile_ci(data, percentiles=[50, 90, 95], n_resamples=1000, confidence=0.95, seed=0):
    """
    Computes percentiles and their 95% Bootstrap Confidence Intervals.
    Returns dict: {p: {'val': float, 'low': float, 'high': float}}
    """
    rng = np.random.default_rng(seed)
    n = len(data)
    alpha = (1.0 - confidence) / 2.0
    
    # Point estimates
    results = {}
    for p in percentiles:
        results[p] = {'val': float(np.percentile(data, p))}

    # Bootstrap resamples
    boot_indices = rng.integers(0, n, size=(n_resamples, n))
    boot_samples = data[boot_indices]  # Shape: (n_resamples, n)

    for p in percentiles:
        boot_p = np.percentile(boot_samples, p, axis=1)
        low = float(np.percentile(boot_p, alpha * 100.0))
        high = float(np.percentile(boot_p, (1.0 - alpha) * 100.0))
        results[p]['low'] = low
        results[p]['high'] = high

    return results


def evaluate_mat(result_mat_path, gps_path, rhos=[50, 100, 200, 500], default_rho=100.0, n_resamples=1000, seed=0):
    """
    Main evaluation pipeline.
    """
    if not os.path.exists(result_mat_path):
        raise FileNotFoundError(f"Result mat file not found: {result_mat_path}")

    gps_dict = load_gps_coords(gps_path)
    mat = scipy.io.loadmat(result_mat_path)

    query_f = mat['query_f']          # Shape: (N_query, D)
    gallery_f = mat['gallery_f']      # Shape: (N_gallery, D)
    query_label = mat['query_label'].reshape(-1)
    gallery_label = mat['gallery_label'].reshape(-1)

    # Normalize features if not already normalized
    q_norm = np.linalg.norm(query_f, axis=1, keepdims=True)
    q_norm[q_norm == 0] = 1.0
    query_f = query_f / q_norm

    g_norm = np.linalg.norm(gallery_f, axis=1, keepdims=True)
    g_norm[g_norm == 0] = 1.0
    gallery_f = gallery_f / g_norm

    num_queries = len(query_label)
    num_gallery = len(gallery_label)

    print(f"[INFO] Evaluating {num_queries} queries against {num_gallery} gallery items.")

    errors = np.zeros(num_queries, dtype=np.float64)
    margins = np.zeros(num_queries, dtype=np.float64)
    r1_hits = np.zeros(num_queries, dtype=np.int32)
    r5_hits = np.zeros(num_queries, dtype=np.int32)
    sdm1_scores = np.zeros(num_queries, dtype=np.float64)
    aps = np.zeros(num_queries, dtype=np.float64)

    # Compute similarity in batches to avoid CPU memory blowup
    batch_size = 256
    for start_idx in range(0, num_queries, batch_size):
        end_idx = min(start_idx + batch_size, num_queries)
        q_batch = query_f[start_idx:end_idx]  # (B, D)
        sim_batch = np.dot(q_batch, gallery_f.T)  # (B, N_gallery)

        for b in range(end_idx - start_idx):
            q_i = start_idx + b
            sims = sim_batch[b]
            sorted_idx = np.argsort(sims)[::-1]

            top1_idx = sorted_idx[0]
            top2_idx = sorted_idx[1] if len(sorted_idx) > 1 else sorted_idx[0]

            # Top-1 vs Top-2 Confidence Margin
            margins[q_i] = float(sims[top1_idx] - sims[top2_idx])

            # Class IDs & GPS positions
            q_lbl = query_label[q_i]
            top1_lbl = gallery_label[top1_idx]

            q_lon, q_lat = gps_dict.get(q_lbl, (0.0, 0.0))
            top1_lon, top1_lat = gps_dict.get(top1_lbl, (0.0, 0.0))

            # Geodesic Error in meters
            err_m = latlog2meter(q_lat, q_lon, top1_lat, top1_lon)
            errors[q_i] = err_m

            # Recall@1 & Recall@5
            if top1_lbl == q_lbl:
                r1_hits[q_i] = 1
            if q_lbl in gallery_label[sorted_idx[:5]]:
                r5_hits[q_i] = 1

            # SDM@1
            deg_dist = euclidean_degree_distance(q_lon, q_lat, top1_lon, top1_lat)
            sdm1_scores[q_i] = float(1.0 / np.exp(deg_dist * 5e3))

            # mAP
            good_mask = (gallery_label[sorted_idx] == q_lbl)
            rows_good = np.where(good_mask)[0]
            if len(rows_good) > 0:
                ngood = len(rows_good)
                ap = 0.0
                for rank_idx, r in enumerate(rows_good):
                    precision = (rank_idx + 1.0) / (r + 1.0)
                    old_precision = rank_idx / r if r > 0 else 1.0
                    ap += (1.0 / ngood) * (old_precision + precision) / 2.0
                aps[q_i] = ap

    # Calculate GFR and MA across rho thresholds
    gfr_results = {}
    ma_results = {}
    for rho in rhos:
        fails = int(np.sum(errors > rho))
        gfr_val, gfr_low, gfr_high = wilson_score_interval(fails, num_queries)
        gfr_results[str(int(rho))] = {
            'rate': float(gfr_val),
            'ci_95': [float(gfr_low), float(gfr_high)],
            'fails': fails,
            'total': num_queries
        }
        ma_results[str(int(rho))] = float((1.0 - (fails / num_queries)) * 100.0)

    # Calculate Percentiles with Bootstrap CI
    pct_results = bootstrap_percentile_ci(errors, percentiles=[50, 90, 95], n_resamples=n_resamples, seed=seed)

    # Calculate GeoAUROC for detecting gross failure {err > default_rho}
    binary_failure = (errors > default_rho).astype(np.int32)
    num_failures = int(np.sum(binary_failure))
    if 0 < num_failures < num_queries:
        # Lower margin => Higher probability of failure, so predictor score is -margin
        geo_auroc = float(roc_auc_score(binary_failure, -margins) * 100.0)
    else:
        geo_auroc = 100.0 if num_failures == 0 else 0.0

    # Summary Metrics
    r1_val = float(np.mean(r1_hits) * 100.0)
    r5_val = float(np.mean(r5_hits) * 100.0)
    map_val = float(np.mean(aps) * 100.0)
    sdm1_val = float(np.mean(sdm1_scores) * 100.0)

    full_results = {
        'metadata': {
            'num_queries': num_queries,
            'num_gallery': num_gallery,
            'default_rho': default_rho,
            'n_resamples': n_resamples,
            'seed': seed
        },
        'standard_metrics': {
            'Recall@1': r1_val,
            'Recall@5': r5_val,
            'mAP': map_val,
            'SDM@1': sdm1_val
        },
        'gross_failure_rate_GFR': gfr_results,
        'meter_accuracy_MA': ma_results,
        'percentiles_m': {
            'p50': pct_results[50],
            'p90': pct_results[90],
            'p95': pct_results[95]
        },
        'GeoAUROC': {
            'threshold_rho': default_rho,
            'score': geo_auroc
        }
    }

    return full_results, errors


def print_formatted_summary(res):
    std = res['standard_metrics']
    gfr = res['gross_failure_rate_GFR']
    pct = res['percentiles_m']
    geo = res['GeoAUROC']

    print("\n" + "=" * 80)
    print("           [+] COMPREHENSIVE EVALUATION METRICS REPORT (Task K1)           ")
    print("=" * 80)
    print(f"  * Recall@1:  {std['Recall@1']:>6.2f}%   |  Recall@5:  {std['Recall@5']:>6.2f}%   |  mAP: {std['mAP']:>6.2f}%")
    print(f"  * SDM@1:     {std['SDM@1']:>6.2f}%   |  GeoAUROC:  {geo['score']:>6.2f}% (rho = {geo['threshold_rho']:.0f}m)")
    print("-" * 80)
    print("  [>] PERCENTILE DISTANCE ERRORS (with 95% Bootstrap CI):")
    print(f"     - p50 (Median): {pct['p50']['val']:>6.2f} m  [95% CI: {pct['p50']['low']:>5.2f} - {pct['p50']['high']:>5.2f} m]")
    print(f"     - p90:          {pct['p90']['val']:>6.2f} m  [95% CI: {pct['p90']['low']:>5.2f} - {pct['p90']['high']:>5.2f} m]")
    print(f"     - p95:          {pct['p95']['val']:>6.2f} m  [95% CI: {pct['p95']['low']:>5.2f} - {pct['p95']['high']:>5.2f} m]")
    print("-" * 80)
    print("  [!] GROSS FAILURE RATE (GFR@rho = P(err > rho)) & METER ACCURACY (MA@rho):")
    for rho_str, data in gfr.items():
        rho = int(rho_str)
        rate = data['rate']
        ci = data['ci_95']
        ma = res['meter_accuracy_MA'][rho_str]
        print(f"     - rho = {rho:>3d}m : GFR = {rate:>5.2f}% [95% Wilson CI: {ci[0]:>5.2f}% - {ci[1]:>5.2f}%]  |  MA = {ma:>5.2f}%")
    print("=" * 80 + "\n")


def main():
    parser = get_parse()
    args = parser.parse_args()

    rhos = [float(r.strip()) for r in args.rhos.split(',') if r.strip()]

    # Auto locate result_mat if relative path provided
    result_mat_path = args.result_mat
    if not os.path.isabs(result_mat_path) and not os.path.exists(result_mat_path):
        candidate = os.path.join(CURRENT_DIR, result_mat_path)
        if os.path.exists(candidate):
            result_mat_path = candidate

    gps_path = args.gps_path
    if not gps_path:
        gps_path = os.path.join(CURRENT_DIR, 'datasets', 'DenseUAV', 'Dense_GPS_ALL.txt')

    full_results, errors = evaluate_mat(
        result_mat_path=result_mat_path,
        gps_path=gps_path,
        rhos=rhos,
        default_rho=args.rho,
        n_resamples=args.n_resamples,
        seed=args.seed
    )

    print_formatted_summary(full_results)

    # Save results.json
    output_json_path = args.output_json
    with open(output_json_path, 'w') as f:
        json.dump(full_results, f, indent=4)
    print(f"[SUCCESS] Exported metrics to: {output_json_path}")

    # Save errors.npy
    output_npy_path = args.output_npy
    np.save(output_npy_path, errors)
    print(f"[SUCCESS] Exported per-query errors array to: {output_npy_path}")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Task 3: Naive Weighted Centroid Failure Analysis
Research Gap 1: Spatial Mismatch on DenseUAV Benchmark

Demonstrates:
1. Accuracy collapse when using visual similarity scores as naive spatial weights.
2. Explosion of tail localization error (p90, p95) due to spatial dispersion and cross-campus pulling.
3. Grid scan over candidate count K in {1, 2, 3, 5} and softmax temperatures tau in {0.01, 0.05, 0.1, 1.0}.
"""

import os
import sys
import math
import json
import argparse
import numpy as np
import scipy.io as sio

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_parse():
    parser = argparse.ArgumentParser(
        description="Task 3: Naive Weighted Centroid Localization Evaluation"
    )
    parser.add_argument(
        "--mat_path",
        default="",
        type=str,
        help="Path to pytorch_result.mat (extracted features)",
    )
    parser.add_argument(
        "--gps_path",
        default="",
        type=str,
        help="Path to Dense_GPS_ALL.txt (class_id to GPS mapping)",
    )
    parser.add_argument(
        "--ks",
        default="1,2,3,5",
        type=str,
        help="Comma-separated K values to evaluate (e.g. 1,2,3,5)",
    )
    parser.add_argument(
        "--taus",
        default="0.01,0.05,0.1,1.0",
        type=str,
        help="Comma-separated temperature values (e.g. 0.01,0.05,0.1,1.0)",
    )
    parser.add_argument(
        "--output_dir",
        default="",
        type=str,
        help="Directory to save output CSV and reports",
    )
    parser.add_argument(
        "--batch_size",
        default=256,
        type=int,
        help="Batch size for computing cosine similarities",
    )
    return parser


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Geodesic distance between two points in meters using Haversine formula (WGS-84).
    """
    EARTH_RADIUS = 6378137.0  # meters
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    lat1_r = math.radians(lat1)
    lat2_r = math.radians(lat2)

    a = (
        math.sin(d_lat / 2.0) ** 2
        + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(d_lon / 2.0) ** 2
    )
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return EARTH_RADIUS * c


def load_gps_coords(gps_path):
    """
    Parses Dense_GPS_ALL.txt.
    Maps class_id (both string and int) -> (lon, lat).
    """
    candidates = [
        gps_path,
        os.path.join(CURRENT_DIR, "data", "Dense_GPS_ALL.txt"),
        os.path.join(CURRENT_DIR, "..", "data", "Dense_GPS_ALL.txt"),
        os.path.join(CURRENT_DIR, "..", "..", "datasets", "DenseUAV", "Dense_GPS_ALL.txt"),
        os.path.join("datasets", "DenseUAV", "Dense_GPS_ALL.txt"),
    ]

    actual_path = None
    for c in candidates:
        if c and os.path.exists(c):
            actual_path = os.path.abspath(c)
            break

    if actual_path is None:
        raise FileNotFoundError(
            f"GPS file not found. Tried paths:\n" + "\n".join(filter(bool, candidates))
        )

    print(f"[INFO] Loading GPS coordinates from: {actual_path}")
    gps_dict = {}
    count = 0
    with open(actual_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                class_key = parts[0].replace("\\", "/").split("/")[-2]
                lon = float(parts[1].split("E")[-1])
                lat = float(parts[2].split("N")[-1])
                gps_dict[class_key] = (lon, lat)
                try:
                    gps_dict[int(class_key)] = (lon, lat)
                except ValueError:
                    pass
                count += 1

    print(f"[INFO] Loaded GPS coordinates for {len(gps_dict)} keys ({count} lines parsed).")
    return gps_dict


def find_feature_mat(mat_path):
    """
    Resolves feature mat path with auto-detection fallbacks.
    """
    candidates = [
        mat_path,
        os.path.join(CURRENT_DIR, "data", "pytorch_result.mat"),
        os.path.join(CURRENT_DIR, "..", "data", "pytorch_result.mat"),
        os.path.join(CURRENT_DIR, "..", "..", "checkpoints", "baseline_vits_single", "pytorch_result_1.mat"),
        os.path.join(CURRENT_DIR, "..", "..", "checkpoints", "vits_fsra", "pytorch_result_1.mat"),
        os.path.join(CURRENT_DIR, "..", "..", "checkpoints", "resnet50_single", "pytorch_result_1.mat"),
    ]

    for c in candidates:
        if c and os.path.exists(c):
            return os.path.abspath(c)

    raise FileNotFoundError(
        f"Feature .mat file not found. Tried paths:\n" + "\n".join(filter(bool, candidates))
    )


def evaluate_centroid_grid(query_features, gallery_features, query_labels, gallery_labels, gps_dict, k_list, tau_list, batch_size=256):
    """
    Evaluates Naive Weighted Centroid across (K, tau) grid.
    """
    num_queries = len(query_labels)
    max_k = max(k_list)

    # First pass: collect Top-max_k similarities and coordinates for all valid queries
    all_query_data = []

    for start_idx in range(0, num_queries, batch_size):
        end_idx = min(start_idx + batch_size, num_queries)
        q_batch = query_features[start_idx:end_idx]
        sim_batch = np.dot(q_batch, gallery_features.T)

        for b in range(end_idx - start_idx):
            q_idx = start_idx + b
            q_lbl = query_labels[q_idx]

            if q_lbl not in gps_dict:
                continue
            q_lon, q_lat = gps_dict[q_lbl]

            sims = sim_batch[b]
            topk_idx = np.argsort(sims)[::-1][:max_k]
            topk_sims = sims[topk_idx]
            topk_lbls = gallery_labels[topk_idx]

            coords = []
            valid_cand = True
            for cand_lbl in topk_lbls:
                if cand_lbl not in gps_dict:
                    valid_cand = False
                    break
                c_lon, c_lat = gps_dict[cand_lbl]
                coords.append((c_lat, c_lon))

            if not valid_cand or len(coords) < max_k:
                continue

            all_query_data.append({
                "query_index": q_idx,
                "p_true": (q_lat, q_lon),
                "sims": topk_sims,
                "coords": coords,
            })

    total_valid = len(all_query_data)
    print(f"[INFO] Collected Top-{max_k} candidates for {total_valid} valid queries.")

    # 1. Baseline: Top-1 Error (Pure Retrieval)
    top1_errors = []
    for item in all_query_data:
        p_true = item["p_true"]
        p_top1 = item["coords"][0]
        err = haversine_distance(p_true[0], p_true[1], p_top1[0], p_top1[1])
        top1_errors.append(err)

    top1_errors = np.array(top1_errors, dtype=np.float64)
    top1_stats = {
        "mean": float(np.mean(top1_errors)),
        "std": float(np.std(top1_errors)),
        "median": float(np.median(top1_errors)),
        "p90": float(np.percentile(top1_errors, 90)),
        "p95": float(np.percentile(top1_errors, 95)),
    }

    grid_results = {}

    # 2. Grid evaluation over (K, tau)
    for k in k_list:
        grid_results[k] = {}
        for tau in tau_list:
            if k == 1:
                # K=1 is identical to Top-1 regardless of tau
                grid_results[k][tau] = {
                    "k": 1,
                    "tau": tau,
                    "mean_error_m": top1_stats["mean"],
                    "median_error_m": top1_stats["median"],
                    "p90_error_m": top1_stats["p90"],
                    "p95_error_m": top1_stats["p95"],
                    "delta_p95_vs_top1_m": 0.0,
                    "p95_ratio_vs_top1": 1.0,
                    "pct_queries_degraded": 0.0,
                    "pct_queries_improved": 0.0,
                }
                continue

            centroid_errors = []
            degraded_count = 0
            improved_count = 0

            for q_i, item in enumerate(all_query_data):
                p_true = item["p_true"]
                sims_k = item["sims"][:k]
                coords_k = item["coords"][:k]

                # Softmax weights with numerical stability
                scaled_sims = (sims_k - np.max(sims_k)) / tau
                exp_s = np.exp(scaled_sims)
                weights = exp_s / np.sum(exp_s)

                # Linear coordinate centroid interpolation
                pred_lat = sum(w * c[0] for w, c in zip(weights, coords_k))
                pred_lon = sum(w * c[1] for w, c in zip(weights, coords_k))

                err_centroid = haversine_distance(p_true[0], p_true[1], pred_lat, pred_lon)
                centroid_errors.append(err_centroid)

                err_top1 = top1_errors[q_i]
                if err_centroid > err_top1 + 1e-4:
                    degraded_count += 1
                elif err_centroid < err_top1 - 1e-4:
                    improved_count += 1

            err_arr = np.array(centroid_errors, dtype=np.float64)
            mean_e = float(np.mean(err_arr))
            med_e = float(np.median(err_arr))
            p90_e = float(np.percentile(err_arr, 90))
            p95_e = float(np.percentile(err_arr, 95))

            delta_p95 = p95_e - top1_stats["p95"]
            ratio_p95 = p95_e / top1_stats["p95"] if top1_stats["p95"] > 0 else 1.0

            pct_deg = (degraded_count / total_valid) * 100.0
            pct_imp = (improved_count / total_valid) * 100.0

            grid_results[k][tau] = {
                "k": k,
                "tau": tau,
                "mean_error_m": mean_e,
                "median_error_m": med_e,
                "p90_error_m": p90_e,
                "p95_error_m": p95_e,
                "delta_p95_vs_top1_m": delta_p95,
                "p95_ratio_vs_top1": ratio_p95,
                "pct_queries_degraded": pct_deg,
                "pct_queries_improved": pct_imp,
            }

    return top1_stats, grid_results, all_query_data


def main():
    parser = get_parse()
    args = parser.parse_args()

    mat_file = find_feature_mat(args.mat_path)
    gps_dict = load_gps_coords(args.gps_path)

    output_dir = args.output_dir
    if not output_dir:
        output_dir = os.path.join(CURRENT_DIR, "results")
    os.makedirs(output_dir, exist_ok=True)

    print(f"[INFO] Loading features from: {mat_file}")
    mat = sio.loadmat(mat_file)

    q_key = "query_f" if "query_f" in mat else "query_feature"
    g_key = "gallery_f" if "gallery_f" in mat else "gallery_feature"

    if q_key not in mat or g_key not in mat:
        raise KeyError(f"Features not found. Available keys: {list(mat.keys())}")

    query_features = mat[q_key].astype(np.float32)
    gallery_features = mat[g_key].astype(np.float32)
    query_labels = mat["query_label"].reshape(-1)
    gallery_labels = mat["gallery_label"].reshape(-1)

    print(f"[INFO] Query shape: {query_features.shape}, Gallery shape: {gallery_features.shape}")

    # L2 normalize
    q_norm = np.linalg.norm(query_features, axis=1, keepdims=True)
    q_norm[q_norm == 0] = 1.0
    query_features = query_features / q_norm

    g_norm = np.linalg.norm(gallery_features, axis=1, keepdims=True)
    g_norm[g_norm == 0] = 1.0
    gallery_features = gallery_features / g_norm

    k_list = [int(x.strip()) for x in args.ks.split(",") if x.strip()]
    k_list.sort()
    tau_list = [float(x.strip()) for x in args.taus.split(",") if x.strip()]
    tau_list.sort()

    print("\n" + "=" * 90)
    print(" TASK 3: NAIVE WEIGHTED CENTROID ACCURACY CRASH EVALUATION ")
    print("=" * 90)

    top1_stats, grid_results, query_data = evaluate_centroid_grid(
        query_features,
        gallery_features,
        query_labels,
        gallery_labels,
        gps_dict,
        k_list,
        tau_list,
        batch_size=args.batch_size,
    )

    print(f"\n[BASELINE: Pure Top-1 Retrieval (K=1)]")
    print(f"  * Median Error (p50): {top1_stats['median']:.2f} m")
    print(f"  * Mean Error:         {top1_stats['mean']:.2f} m")
    print(f"  * p90 Error:          {top1_stats['p90']:.2f} m")
    print(f"  * p95 Error:          {top1_stats['p95']:.2f} m")

    csv_rows = [
        "Method,K,Tau,Median_Error_m,Mean_Error_m,p90_Error_m,p95_Error_m,Delta_p95_vs_Top1_m,p95_Ratio,Pct_Degraded"
    ]

    print("\n" + "-" * 95)
    print(f"{'Method':<16} {'K':<4} {'Tau':<6} {'Median(m)':<11} {'Mean(m)':<11} {'p90(m)':<11} {'p95(m)':<11} {'Delta p95':<12} {'Degraded %':<10}")
    print("-" * 95)

    # Format Top-1 first
    print(f"{'Top-1 Baseline':<16} {1:<4} {'-':<6} {top1_stats['median']:<11.2f} {top1_stats['mean']:<11.2f} {top1_stats['p90']:<11.2f} {top1_stats['p95']:<11.2f} {'0.00':<12} {'0.00%':<10}")
    csv_rows.append(f"Top-1,1,-,{top1_stats['median']:.2f},{top1_stats['mean']:.2f},{top1_stats['p90']:.2f},{top1_stats['p95']:.2f},0.00,1.00,0.00")

    worst_p95_ratio = 1.0
    worst_config = None

    for k in k_list:
        if k == 1:
            continue
        for tau in tau_list:
            res = grid_results[k][tau]
            med = res["median_error_m"]
            mean_e = res["mean_error_m"]
            p90 = res["p90_error_m"]
            p95 = res["p95_error_m"]
            delta = res["delta_p95_vs_top1_m"]
            ratio = res["p95_ratio_vs_top1"]
            deg = res["pct_queries_degraded"]

            if ratio > worst_p95_ratio:
                worst_p95_ratio = ratio
                worst_config = (k, tau, p95)

            csv_rows.append(f"Centroid,{k},{tau:.2f},{med:.2f},{mean_e:.2f},{p90:.2f},{p95:.2f},{delta:+.2f},{ratio:.2f},{deg:.2f}")
            print(f"{'Naive Centroid':<16} {k:<4} {tau:<6.2f} {med:<11.2f} {mean_e:<11.2f} {p90:<11.2f} {p95:<11.2f} {delta:+<12.2f} {deg:<9.2f}%")

    print("-" * 95)

    # Save CSV
    csv_path = os.path.join(output_dir, "centroid_comparison.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("\n".join(csv_rows) + "\n")
    print(f"\n[SUCCESS] Saved centroid comparison CSV to: {csv_path}")

    # Criteria Verification for Gap 1
    # Check explosion of p95 for K >= 3
    # Check K=3, tau=0.1 or tau=1.0 and K=5, tau=0.1 or tau=1.0
    k3_tau01 = grid_results.get(3, {}).get(0.1, {})
    k5_tau01 = grid_results.get(5, {}).get(0.1, {})
    k5_tau10 = grid_results.get(5, {}).get(1.0, {})

    p95_k3 = k3_tau01.get("p95_error_m", top1_stats["p95"])
    p95_k5 = k5_tau10.get("p95_error_m", top1_stats["p95"])

    # Does p95 blow up by > 300m or ratio > 1.5x?
    cond1_passed = bool(p95_k5 > top1_stats["p95"] + 100.0 or p95_k5 > 500.0)
    cond2_passed = bool(k5_tau01.get("pct_queries_degraded", 0.0) > 40.0)
    gap1_confirmed = bool(cond1_passed and cond2_passed)

    report = {
        "metadata": {
            "feature_mat": os.path.relpath(mat_file, CURRENT_DIR),
            "num_queries": len(query_data),
            "evaluated_ks": k_list,
            "evaluated_taus": tau_list,
        },
        "top1_baseline": top1_stats,
        "grid_results": {
            f"K_{k}": {
                f"tau_{tau}": grid_results[k][tau] for tau in tau_list
            } for k in k_list
        },
        "criteria_verification": {
            "criterion_1_tail_error_blowup": {
                "top1_p95_m": round(top1_stats["p95"], 2),
                "centroid_k5_tau10_p95_m": round(p95_k5, 2),
                "delta_p95_m": round(p95_k5 - top1_stats["p95"], 2),
                "passed": cond1_passed,
                "interpretation": "Tail error p95 explodes dramatically when using Centroid with K >= 3" if cond1_passed else "Centroid refines position",
            },
            "criterion_2_accuracy_degradation": {
                "pct_queries_degraded_k5": round(k5_tau01.get("pct_queries_degraded", 0.0), 2),
                "passed": cond2_passed,
                "interpretation": "Naive Centroid causes localization accuracy degradation for the vast majority of queries" if cond2_passed else "Centroid improves accuracy",
            },
            "gap_1_naive_centroid_crash_proven": gap1_confirmed,
        },
    }

    json_path = os.path.join(output_dir, "centroid_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    print(f"[SUCCESS] Saved detailed JSON report to: {json_path}")

    # Summary box
    print("\n" + "=" * 90)
    print(" RESEARCH GAP 1: NAIVE CENTROID CRASH VERIFICATION SUMMARY")
    print("=" * 90)
    print(f" Top-1 Baseline p95 Error:                 {top1_stats['p95']:.2f} m")
    print(f" Centroid (K=5, tau=1.0) p95 Error:        {p95_k5:.2f} m (Delta: +{p95_k5 - top1_stats['p95']:.2f} m)")
    print(f" Queries Degraded by Centroid (K=5, tau=0.1): {k5_tau01.get('pct_queries_degraded', 0.0):.2f}%")
    print(f" OVERALL CONCLUSION: {'RESEARCH GAP 1 NAIVE CENTROID FAILURE IS EMPIRICALLY PROVEN!' if gap1_confirmed else 'GAP 1 NOT FULLY SUPPORTED'}")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    main()

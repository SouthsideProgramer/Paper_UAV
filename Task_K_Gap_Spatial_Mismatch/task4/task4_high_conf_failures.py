# -*- coding: utf-8 -*-
"""
Task 4: High-Confidence Visual Mismatch Identification
Research Gap 1: Spatial Mismatch on DenseUAV Benchmark

Identifies, quantifies, and extracts extreme Spatial Mismatch failure cases:
- High visual confidence (s_1 >= 0.85 or s_1 >= 0.90)
- Catastrophic geographic error (d_1 >= 200m, d_1 >= 500m, d_1 >= 1000m)
Exports visual_mismatch_cases.json and summary CSV for paper heatmap and visual figure generation.
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
        description="Task 4: High-Confidence Visual Mismatch Identification"
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
        "--sim_thresh",
        default=0.85,
        type=float,
        help="Cosine similarity threshold for high-confidence classification (e.g. 0.85 or 0.90)",
    )
    parser.add_argument(
        "--dist_thresh",
        default=200.0,
        type=float,
        help="Distance threshold in meters for localization failure (e.g. 200.0m)",
    )
    parser.add_argument(
        "--output_dir",
        default="",
        type=str,
        help="Directory to save output JSON and summary CSV",
    )
    parser.add_argument(
        "--top_cases",
        default=50,
        type=int,
        help="Number of most severe mismatch cases to export in detail",
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
        os.path.join(CURRENT_DIR, "..", "..", "checkpoints", "vits_fsra", "pytorch_result_1.mat"),
        os.path.join(CURRENT_DIR, "..", "..", "checkpoints", "baseline_vits_single", "pytorch_result_1.mat"),
        os.path.join(CURRENT_DIR, "..", "..", "checkpoints", "resnet50_single", "pytorch_result_1.mat"),
    ]

    for c in candidates:
        if c and os.path.exists(c):
            return os.path.abspath(c)

    raise FileNotFoundError(
        f"Feature .mat file not found. Tried paths:\n" + "\n".join(filter(bool, candidates))
    )


def extract_path_str(val):
    """
    Safely extracts string from numpy object or array.
    """
    if isinstance(val, (np.ndarray, list)):
        if len(val) > 0:
            val = val[0]
    if isinstance(val, (bytes, np.bytes_)):
        return val.decode("utf-8", errors="ignore").strip()
    return str(val).strip()


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

    query_paths = mat.get("query_path", None)
    gallery_paths = mat.get("gallery_path", None)

    num_queries = len(query_labels)
    num_gallery = len(gallery_labels)
    print(f"[INFO] Evaluating {num_queries} queries against {num_gallery} gallery tiles.")

    # L2 normalize
    q_norm = np.linalg.norm(query_features, axis=1, keepdims=True)
    q_norm[q_norm == 0] = 1.0
    query_features = query_features / q_norm

    g_norm = np.linalg.norm(gallery_features, axis=1, keepdims=True)
    g_norm[g_norm == 0] = 1.0
    gallery_features = gallery_features / g_norm

    print("\n" + "=" * 90)
    print(" TASK 4: HIGH-CONFIDENCE VISUAL MISMATCH IDENTIFICATION ")
    print("=" * 90)

    # First pass: Compute Top-1 similarity s_1, geodesic distance d_1, and metadata
    all_cases = []

    for start_idx in range(0, num_queries, args.batch_size):
        end_idx = min(start_idx + args.batch_size, num_queries)
        q_batch = query_features[start_idx:end_idx]
        sim_batch = np.dot(q_batch, gallery_features.T)

        for b in range(end_idx - start_idx):
            q_i = start_idx + b
            q_lbl = query_labels[q_i]

            if q_lbl not in gps_dict:
                continue
            q_lon, q_lat = gps_dict[q_lbl]

            sims = sim_batch[b]
            top1_idx = int(np.argmax(sims))
            s1 = float(sims[top1_idx])
            top1_lbl = gallery_labels[top1_idx]

            if top1_lbl not in gps_dict:
                continue
            top1_lon, top1_lat = gps_dict[top1_lbl]

            d1 = haversine_distance(q_lat, q_lon, top1_lat, top1_lon)

            # Resolve paths
            q_path_str = ""
            if query_paths is not None and len(query_paths) > q_i:
                q_path_str = extract_path_str(query_paths[q_i])

            g_path_str = ""
            if gallery_paths is not None and len(gallery_paths) > top1_idx:
                g_path_str = extract_path_str(gallery_paths[top1_idx])

            all_cases.append({
                "query_index": int(q_i),
                "query_label": str(q_lbl),
                "query_gps": [float(q_lon), float(q_lat)],
                "query_path": q_path_str,
                "top1_gallery_index": int(top1_idx),
                "top1_gallery_label": str(top1_lbl),
                "top1_gallery_gps": [float(top1_lon), float(top1_lat)],
                "top1_gallery_path": g_path_str,
                "s1_cosine_similarity": float(s1),
                "d1_geodesic_distance_m": float(d1),
                "is_label_match": bool(q_lbl == top1_lbl),
            })

    total_valid = len(all_cases)
    print(f"[INFO] Analyzed Top-1 results for {total_valid} valid queries.")

    # 4 Quadrants Partitioning
    sim_th = args.sim_thresh
    dist_th = args.dist_thresh

    quad_high_conf_correct = []
    quad_high_conf_mismatch = []
    quad_low_conf_error = []
    quad_low_conf_correct = []

    # Severe mismatch subsets
    mismatch_gt_500m = []
    mismatch_gt_1000m = []
    mismatch_sim_gt_90_dist_gt_500 = []
    mismatch_sim_gt_90_dist_gt_1000 = []

    for c in all_cases:
        s1 = c["s1_cosine_similarity"]
        d1 = c["d1_geodesic_distance_m"]

        if s1 >= sim_th and d1 < dist_th:
            quad_high_conf_correct.append(c)
        elif s1 >= sim_th and d1 >= dist_th:
            quad_high_conf_mismatch.append(c)
            if d1 >= 500.0:
                mismatch_gt_500m.append(c)
            if d1 >= 1000.0:
                mismatch_gt_1000m.append(c)
        elif s1 < sim_th and d1 >= dist_th:
            quad_low_conf_error.append(c)
        else:
            quad_low_conf_correct.append(c)

        if s1 >= 0.90 and d1 >= 500.0:
            mismatch_sim_gt_90_dist_gt_500.append(c)
        if s1 >= 0.90 and d1 >= 1000.0:
            mismatch_sim_gt_90_dist_gt_1000.append(c)

    n_high_correct = len(quad_high_conf_correct)
    n_high_mismatch = len(quad_high_conf_mismatch)
    n_low_error = len(quad_low_conf_error)
    n_low_correct = len(quad_low_conf_correct)

    pct_high_correct = (n_high_correct / total_valid) * 100.0
    pct_high_mismatch = (n_high_mismatch / total_valid) * 100.0
    pct_low_error = (n_low_error / total_valid) * 100.0
    pct_low_correct = (n_low_correct / total_valid) * 100.0

    print(f"\n[QUADRANT ANALYSIS (sim_thresh >= {sim_th}, dist_thresh >= {dist_th}m)]")
    print(f"  1. High-Confidence Correct (s1 >= {sim_th}, d1 < {dist_th}m):     {n_high_correct:4d} ({pct_high_correct:5.2f}%)")
    print(f"  2. High-Confidence Mismatch (s1 >= {sim_th}, d1 >= {dist_th}m):    {n_high_mismatch:4d} ({pct_high_mismatch:5.2f}%)  <-- SPATIAL MISMATCH")
    print(f"  3. Low-Confidence Error    (s1 <  {sim_th}, d1 >= {dist_th}m):    {n_low_error:4d} ({pct_low_error:5.2f}%)")
    print(f"  4. Low-Confidence Correct  (s1 <  {sim_th}, d1 <  {dist_th}m):    {n_low_correct:4d} ({pct_low_correct:5.2f}%)")

    print(f"\n[SEVERE SPATIAL MISMATCH SUBSETS]")
    print(f"  * High Confidence (s1 >= {sim_th}) with d1 >= 500m:               {len(mismatch_gt_500m):4d} ({len(mismatch_gt_500m)/total_valid*100:5.2f}%)")
    print(f"  * High Confidence (s1 >= {sim_th}) with d1 >= 1000m (Cross-Campus):{len(mismatch_gt_1000m):4d} ({len(mismatch_gt_1000m)/total_valid*100:5.2f}%)")
    print(f"  * Extreme Confidence (s1 >= 0.90) with d1 >= 500m:               {len(mismatch_sim_gt_90_dist_gt_500):4d}")
    print(f"  * Extreme Confidence (s1 >= 0.90) with d1 >= 1000m:              {len(mismatch_sim_gt_90_dist_gt_1000):4d}")

    # Sort mismatch cases by error distance d1 in descending order
    quad_high_conf_mismatch.sort(key=lambda x: (x["s1_cosine_similarity"] * x["d1_geodesic_distance_m"]), reverse=True)
    top_severe_cases = quad_high_conf_mismatch[:args.top_cases]

    # Check criteria for Gap 1
    cond_gap1_exists = len(mismatch_sim_gt_90_dist_gt_500) > 0 or len(mismatch_gt_1000m) > 0

    report = {
        "metadata": {
            "feature_mat": os.path.relpath(mat_file, CURRENT_DIR),
            "num_queries_evaluated": total_valid,
            "thresholds": {
                "similarity_threshold": sim_th,
                "distance_threshold_meters": dist_th,
            },
        },
        "quadrant_distribution": {
            "high_confidence_correct": {
                "count": n_high_correct,
                "percent": round(pct_high_correct, 2),
                "condition": f"s1 >= {sim_th} and d1 < {dist_th}m",
            },
            "high_confidence_mismatch_spatial_gap": {
                "count": n_high_mismatch,
                "percent": round(pct_high_mismatch, 2),
                "condition": f"s1 >= {sim_th} and d1 >= {dist_th}m",
            },
            "low_confidence_error": {
                "count": n_low_error,
                "percent": round(pct_low_error, 2),
                "condition": f"s1 < {sim_th} and d1 >= {dist_th}m",
            },
            "low_confidence_correct": {
                "count": n_low_correct,
                "percent": round(pct_low_correct, 2),
                "condition": f"s1 < {sim_th} and d1 < {dist_th}m",
            },
        },
        "severe_mismatch_statistics": {
            "s1_gt_thresh_and_d1_gt_500m_count": len(mismatch_gt_500m),
            "s1_gt_thresh_and_d1_gt_1000m_count": len(mismatch_gt_1000m),
            "s1_gt_090_and_d1_gt_500m_count": len(mismatch_sim_gt_90_dist_gt_500),
            "s1_gt_090_and_d1_gt_1000m_count": len(mismatch_sim_gt_90_dist_gt_1000),
        },
        "criteria_verification": {
            "criterion_extreme_mismatch_exists": {
                "condition": "Existence of cases where s1 > 0.90 (or >= 0.85) with d1 > 500m / > 1000m",
                "observed_cases_count": len(mismatch_gt_1000m),
                "passed": cond_gap1_exists,
                "interpretation": "Discovered high-confidence visual mismatch cases where model is extremely confident in visual match but drone is located in a completely different campus" if cond_gap1_exists else "No extreme mismatch found",
            },
            "gap_1_high_confidence_mismatch_proven": cond_gap1_exists,
        },
        "top_severe_mismatch_cases": top_severe_cases,
    }

    # Save JSON
    json_path = os.path.join(output_dir, "visual_mismatch_cases.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    print(f"\n[SUCCESS] Saved visual mismatch report to: {json_path}")

    # Save summary CSV
    csv_rows = [
        "Category,Condition,Count,Percent_of_Total",
        f"High_Conf_Correct,s1>={sim_th} and d1<{dist_th}m,{n_high_correct},{pct_high_correct:.2f}",
        f"High_Conf_Mismatch_SPATIAL_GAP,s1>={sim_th} and d1>={dist_th}m,{n_high_mismatch},{pct_high_mismatch:.2f}",
        f"Low_Conf_Error,s1<{sim_th} and d1>={dist_th}m,{n_low_error},{pct_low_error:.2f}",
        f"Low_Conf_Correct,s1<{sim_th} and d1<{dist_th}m,{n_low_correct},{pct_low_correct:.2f}",
        f"Severe_Mismatch_CrossCampus,s1>={sim_th} and d1>=1000m,{len(mismatch_gt_1000m)},{(len(mismatch_gt_1000m)/total_valid)*100:.2f}",
    ]
    csv_path = os.path.join(output_dir, "mismatch_quadrant_summary.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("\n".join(csv_rows) + "\n")
    print(f"[SUCCESS] Saved quadrant summary CSV to: {csv_path}")

    # Summary box
    print("\n" + "=" * 90)
    print(" RESEARCH GAP 1: HIGH-CONFIDENCE SPATIAL MISMATCH SUMMARY")
    print("=" * 90)
    print(f" Total Queries Evaluated:               {total_valid}")
    print(f" High-Confidence Mismatch (s1 >= {sim_th}, d1 >= {dist_th}m): {n_high_mismatch} ({pct_high_mismatch:.2f}%)")
    print(f" Severe Cross-Campus Mismatches (d1 >= 1000m):     {len(mismatch_gt_1000m)} cases")
    print(f" OVERALL CONCLUSION: {'RESEARCH GAP 1 HIGH-CONFIDENCE MISMATCH EMPIRICALLY CONFIRMED!' if cond_gap1_exists else 'NOT FULLY CONFIRMED'}")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    main()

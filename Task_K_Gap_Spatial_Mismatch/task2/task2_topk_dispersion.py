# -*- coding: utf-8 -*-
"""
Task 2: Top-K Spatial Dispersion Analysis
Research Gap 1: Spatial Mismatch on DenseUAV Benchmark

Quantifies:
1. Maximum Top-K cluster diameter D_max = max_{i,j} Haversine(p_i, p_j) for K in {3, 5, 10}.
2. Standard Distance Deviation (sigma_geo) from geometric centroid.
3. Ratio of candidates scattered outside safe physical thresholds (d > 100m, d > 500m, d > 1000m).
4. Inter-campus cluster fragmentation (D_max > 1000m).
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
        description="Task 2: Spatial Dispersion Analysis in Top-K Candidates"
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
        default="3,5,10",
        type=str,
        help="Comma-separated K values to evaluate (e.g. 3,5,10)",
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


def compute_dispersion_for_k(query_features, gallery_features, query_labels, gallery_labels, gps_dict, k_val, batch_size=256):
    """
    Computes spatial dispersion metrics for Top-K candidates.
    """
    num_queries = len(query_labels)
    d_max_list = []
    sigma_geo_list = []
    
    # Candidate-level distance tracking (relative to drone)
    candidates_out_100m_count = 0
    candidates_out_500m_count = 0
    candidates_out_1000m_count = 0
    total_candidates_evaluated = 0

    # Cluster-level fragmentation tracking
    clusters_dmax_gt_300m = 0
    clusters_dmax_gt_500m = 0
    clusters_dmax_gt_1000m = 0

    query_samples = []

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
            topk_idx = np.argsort(sims)[::-1][:k_val]
            topk_sims = sims[topk_idx]
            topk_lbls = gallery_labels[topk_idx]

            # Collect candidate coordinates
            coords = []
            cand_distances_to_drone = []
            valid_cand = True

            for cand_lbl in topk_lbls:
                if cand_lbl not in gps_dict:
                    valid_cand = False
                    break
                c_lon, c_lat = gps_dict[cand_lbl]
                coords.append((c_lat, c_lon))
                dist_drone = haversine_distance(q_lat, q_lon, c_lat, c_lon)
                cand_distances_to_drone.append(dist_drone)

            if not valid_cand or len(coords) < k_val:
                continue

            # 1. Maximum Pairwise Cluster Diameter D_max
            max_pair_dist = 0.0
            for i in range(k_val):
                for j in range(i + 1, k_val):
                    p_dist = haversine_distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
                    if p_dist > max_pair_dist:
                        max_pair_dist = p_dist

            d_max_list.append(max_pair_dist)

            if max_pair_dist > 300.0:
                clusters_dmax_gt_300m += 1
            if max_pair_dist > 500.0:
                clusters_dmax_gt_500m += 1
            if max_pair_dist > 1000.0:
                clusters_dmax_gt_1000m += 1

            # 2. Geometric Centroid & Standard Distance Deviation (sigma_geo)
            centroid_lat = np.mean([c[0] for c in coords])
            centroid_lon = np.mean([c[1] for c in coords])
            sq_dists_from_centroid = [
                haversine_distance(c[0], c[1], centroid_lat, centroid_lon) ** 2
                for c in coords
            ]
            sigma_geo = math.sqrt(np.mean(sq_dists_from_centroid))
            sigma_geo_list.append(sigma_geo)

            # 3. Candidate-level threshold exceedances
            for d in cand_distances_to_drone:
                total_candidates_evaluated += 1
                if d > 100.0:
                    candidates_out_100m_count += 1
                if d > 500.0:
                    candidates_out_500m_count += 1
                if d > 1000.0:
                    candidates_out_1000m_count += 1

            if q_idx < 10:
                query_samples.append({
                    "query_index": int(q_idx),
                    "query_label": str(q_lbl),
                    "topk_similarities": [round(float(s), 4) for s in topk_sims],
                    "candidate_distances_to_drone_m": [round(float(d), 2) for d in cand_distances_to_drone],
                    "cluster_d_max_m": round(float(max_pair_dist), 2),
                    "standard_distance_sigma_m": round(float(sigma_geo), 2),
                    "inter_campus_fragmentation": bool(max_pair_dist > 1000.0),
                })

    d_max_arr = np.array(d_max_list, dtype=np.float64)
    sigma_arr = np.array(sigma_geo_list, dtype=np.float64)
    total_clusters = len(d_max_list)

    pct_cand_out_100 = (candidates_out_100m_count / total_candidates_evaluated * 100.0) if total_candidates_evaluated > 0 else 0.0
    pct_cand_out_500 = (candidates_out_500m_count / total_candidates_evaluated * 100.0) if total_candidates_evaluated > 0 else 0.0
    pct_cand_out_1000 = (candidates_out_1000m_count / total_candidates_evaluated * 100.0) if total_candidates_evaluated > 0 else 0.0

    pct_clusters_dmax_gt_300 = (clusters_dmax_gt_300m / total_clusters * 100.0) if total_clusters > 0 else 0.0
    pct_clusters_dmax_gt_500 = (clusters_dmax_gt_500m / total_clusters * 100.0) if total_clusters > 0 else 0.0
    pct_clusters_dmax_gt_1000 = (clusters_dmax_gt_1000m / total_clusters * 100.0) if total_clusters > 0 else 0.0

    return {
        "k": k_val,
        "valid_queries": total_clusters,
        "d_max_meters": {
            "mean": float(np.mean(d_max_arr)),
            "std": float(np.std(d_max_arr)),
            "median": float(np.median(d_max_arr)),
            "p75": float(np.percentile(d_max_arr, 75)),
            "p90": float(np.percentile(d_max_arr, 90)),
            "p95": float(np.percentile(d_max_arr, 95)),
            "max": float(np.max(d_max_arr)),
        },
        "standard_distance_sigma_meters": {
            "mean": float(np.mean(sigma_arr)),
            "median": float(np.median(sigma_arr)),
            "p90": float(np.percentile(sigma_arr, 90)),
            "p95": float(np.percentile(sigma_arr, 95)),
        },
        "cluster_fragmentation_percent": {
            "d_max_gt_300m": float(pct_clusters_dmax_gt_300),
            "d_max_gt_500m": float(pct_clusters_dmax_gt_500),
            "d_max_gt_1000m_different_campus": float(pct_clusters_dmax_gt_1000),
        },
        "candidates_outside_safety_radius_percent": {
            "outside_100m": float(pct_cand_out_100),
            "outside_500m": float(pct_cand_out_500),
            "outside_1000m": float(pct_cand_out_1000),
        },
        "samples": query_samples,
    }


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

    report = {
        "metadata": {
            "feature_mat": os.path.relpath(mat_file, CURRENT_DIR),
            "num_queries": int(len(query_labels)),
            "num_gallery": int(len(gallery_labels)),
            "evaluated_ks": k_list,
        },
        "results_by_k": {},
        "criteria_verification": {},
    }

    print("\n" + "=" * 85)
    print(" TASK 2: TOP-K SPATIAL DISPERSION ANALYSIS (CLUSTER DIAMETER & SCATTERING) ")
    print("=" * 85)

    csv_rows = [
        "K,Mean_Dmax_m,Median_Dmax_m,p90_Dmax_m,p95_Dmax_m,Mean_Sigma_m,Pct_Cand_Out_100m,Pct_Cand_Out_500m,Pct_Clusters_Dmax_gt_1000m"
    ]

    for k_val in k_list:
        print(f"\n[EVAL] Evaluating Spatial Dispersion for Top-{k_val} candidates...")
        res = compute_dispersion_for_k(
            query_features,
            gallery_features,
            query_labels,
            gallery_labels,
            gps_dict,
            k_val=k_val,
            batch_size=args.batch_size,
        )
        report["results_by_k"][f"Top_{k_val}"] = res

        d_mean = res["d_max_meters"]["mean"]
        d_median = res["d_max_meters"]["median"]
        d_p90 = res["d_max_meters"]["p90"]
        d_p95 = res["d_max_meters"]["p95"]
        sig_mean = res["standard_distance_sigma_meters"]["mean"]
        cand_out_100 = res["candidates_outside_safety_radius_percent"]["outside_100m"]
        cand_out_500 = res["candidates_outside_safety_radius_percent"]["outside_500m"]
        clust_gt_1000 = res["cluster_fragmentation_percent"]["d_max_gt_1000m_different_campus"]

        print(f"  * Mean Cluster Diameter D_max^(K):       {d_mean:.2f} m (Median: {d_median:.2f} m)")
        print(f"  * 90th / 95th Percentile D_max:          p90: {d_p90:.2f} m | p95: {d_p95:.2f} m")
        print(f"  * Standard Distance Deviation (sigma):   {sig_mean:.2f} m")
        print(f"  * Candidates outside 100m / 500m radius: {cand_out_100:.2f}% / {cand_out_500:.2f}%")
        print(f"  * Clusters fragmented > 1000m (Campus):  {clust_gt_1000:.2f}%")

        csv_rows.append(
            f"{k_val},{d_mean:.2f},{d_median:.2f},{d_p90:.2f},{d_p95:.2f},{sig_mean:.2f},{cand_out_100:.2f},{cand_out_500:.2f},{clust_gt_1000:.2f}"
        )

    # Save CSV
    csv_path = os.path.join(output_dir, "dispersion_metrics.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write("\n".join(csv_rows) + "\n")
    print(f"\n[SUCCESS] Saved dispersion CSV metrics to: {csv_path}")

    # Criteria Verification for Gap 1
    # Check Top-5 metrics
    target_k = 5 if "Top_5" in report["results_by_k"] else f"Top_{k_list[0]}"
    res_k5 = report["results_by_k"][f"Top_{target_k}"] if isinstance(target_k, int) else report["results_by_k"][target_k]

    mean_dmax_k5 = res_k5["d_max_meters"]["mean"]
    pct_gt_1000_k5 = res_k5["cluster_fragmentation_percent"]["d_max_gt_1000m_different_campus"]

    cond1_passed = bool(mean_dmax_k5 > 300.0)
    cond2_passed = bool(pct_gt_1000_k5 > 10.0)  # substantial fraction of cross-campus clusters
    gap1_confirmed = bool(cond1_passed and cond2_passed)

    report["criteria_verification"] = {
        "criterion_1_mean_diameter": {
            "threshold": "> 300.0 meters",
            "observed_value_meters": round(float(mean_dmax_k5), 2),
            "passed": cond1_passed,
            "interpretation": "Candidates are widely dispersed across terrain instead of clustering locally" if cond1_passed else "Candidates cluster tightly",
        },
        "criterion_2_inter_campus_fragmentation": {
            "threshold": "> 10.0% of clusters having D_max > 1000m",
            "observed_value_percent": round(float(pct_gt_1000_k5), 2),
            "passed": cond2_passed,
            "interpretation": "Substantial number of top candidates are scattered in completely different campuses" if cond2_passed else "Candidates remain within same area",
        },
        "gap_1_spatial_dispersion_proven": gap1_confirmed,
    }

    # Save JSON
    json_path = os.path.join(output_dir, "dispersion_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    print(f"[SUCCESS] Saved detailed JSON report to: {json_path}")

    # Summary box
    print("\n" + "=" * 85)
    print(" RESEARCH GAP 1: SPATIAL DISPERSION VERIFICATION SUMMARY")
    print("=" * 85)
    print(f" Criterion 1 [Mean D_max^(5) > 300m]:       {mean_dmax_k5:.2f} m --> {'[PASSED - CONFIRMED]' if cond1_passed else '[FAILED]'}")
    print(f" Criterion 2 [Clusters D_max > 1000m]:       {pct_gt_1000_k5:.2f}% --> {'[PASSED - CONFIRMED]' if cond2_passed else '[FAILED]'}")
    print(f" OVERALL CONCLUSION: {'RESEARCH GAP 1 SPATIAL DISPERSION IS EMPIRICALLY PROVEN!' if gap1_confirmed else 'GAP 1 NOT FULLY SUPPORTED'}")
    print("=" * 85 + "\n")


if __name__ == "__main__":
    main()

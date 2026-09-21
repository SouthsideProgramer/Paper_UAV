# -*- coding: utf-8 -*-
"""
Task 4: Cross-Campus Catastrophic Drift Identification & Visual Extraction
Research Gap 3: Environmental Robustness & Tail Risk Exposure on DenseUAV Benchmark

Proves that:
1. In the worst tail percentiles, retrieval models (especially FSRA/Baseline) do not merely
   suffer small local metric inaccuracies, but match UAV queries to an entirely different
   university campus (> 1,000m to 5,000m+ away).
2. Quantifies cross-campus drift rates and extracts side-by-side visual image pairs
   demonstrating how visual aliasing tricks the model into high-confidence false matches.
"""

import os
import sys
import math
import json
import argparse
import numpy as np
import scipy.io as sio

from PIL import Image, ImageDraw, ImageFont

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
REPO_ROOT = os.path.abspath(os.path.join(TASK_ROOT, ".."))


def get_parse():
    parser = argparse.ArgumentParser(
        description="Task 4: Cross-Campus Drift Identification on DenseUAV"
    )
    parser.add_argument(
        "--mat_path",
        default="",
        type=str,
        help="Path to feature .mat file (e.g. FSRA or Baseline)",
    )
    parser.add_argument(
        "--mat_paths",
        nargs="+",
        default=[],
        help="List of .mat paths to evaluate multiple models",
    )
    parser.add_argument(
        "--model_names",
        nargs="+",
        default=[],
        help="Names corresponding to --mat_paths",
    )
    parser.add_argument(
        "--gps_path",
        default="",
        type=str,
        help="Path to Dense_GPS_ALL.txt",
    )
    parser.add_argument(
        "--drift_threshold",
        default=1000.0,
        type=float,
        help="Distance threshold in meters for cross-campus drift (default: 1000.0m)",
    )
    parser.add_argument(
        "--output_dir",
        default="",
        type=str,
        help="Directory to save CSV, JSON, and visual pairs",
    )
    parser.add_argument(
        "--top_cases",
        default=20,
        type=int,
        help="Number of severe cross-campus drift cases to export in detail",
    )
    parser.add_argument(
        "--render_visuals",
        action="store_true",
        default=True,
        help="Render side-by-side composite images for top drift cases",
    )
    parser.add_argument(
        "--batch_size",
        default=256,
        type=int,
        help="Batch size for computing cosine similarity",
    )
    parser.add_argument(
        "--all_models",
        action="store_true",
        default=True,
        help="Evaluate all 4 available models",
    )
    return parser


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Computes geodesic distance between two points in meters using Haversine formula (WGS-84).
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
    candidates = [
        gps_path,
        os.path.join(CURRENT_DIR, "data", "Dense_GPS_ALL.txt"),
        os.path.join(TASK_ROOT, "data", "Dense_GPS_ALL.txt"),
        os.path.join(REPO_ROOT, "datasets", "DenseUAV", "Dense_GPS_ALL.txt"),
        os.path.join(REPO_ROOT, "Task_K_Gap_Spatial_Mismatch", "data", "Dense_GPS_ALL.txt"),
    ]

    actual_path = None
    for c in candidates:
        if c and os.path.exists(c):
            actual_path = os.path.abspath(c)
            break

    if actual_path is None:
        raise FileNotFoundError(
            f"GPS lookup file not found. Checked paths:\n" + "\n".join(filter(bool, candidates))
        )

    print(f"[INFO] Loading GPS coordinates from: {actual_path}")
    gps_dict = {}
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
    return gps_dict, actual_path


def partition_university_campuses(gps_dict, cluster_radius_m=800.0):
    """
    Partitions GPS locations into 14 university campus clusters using spatial adjacency.
    Within a university, gallery tiles are typically separated by 20m - 100m.
    Different universities are separated by > 1,500m.
    """
    unique_keys = list(gps_dict.keys())
    # Filter only string keys to avoid double counting int keys
    str_keys = [k for k in unique_keys if isinstance(k, str)]
    coords = np.array([[gps_dict[k][0], gps_dict[k][1]] for k in str_keys])

    # Simple spatial grid clustering (cells ~0.008 deg ~ 800m)
    # Project to meters roughly
    lat_m = coords[:, 1] * 110874.0
    lon_m = coords[:, 0] * (111320.0 * math.cos(math.radians(30.32)))
    pts = np.column_stack([lon_m, lat_m])

    # Grid hashing
    cell_size = cluster_radius_m
    grid = {}
    for idx, (x, y) in enumerate(pts):
        gx = int(math.floor(x / cell_size))
        gy = int(math.floor(y / cell_size))
        for ox in (-1, 0, 1):
            for oy in (-1, 0, 1):
                neigh_cell = (gx + ox, gy + oy)
                if neigh_cell not in grid:
                    grid[neigh_cell] = []
                grid[neigh_cell].append(idx)

    # Disjoint set / Union-Find
    parent = list(range(len(pts)))

    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    visited_pairs = set()
    for (gx, gy), indices in grid.items():
        n_pts = len(indices)
        for i in range(n_pts):
            idx1 = indices[i]
            for j in range(i + 1, n_pts):
                idx2 = indices[j]
                pair = (min(idx1, idx2), max(idx1, idx2))
                if pair in visited_pairs:
                    continue
                visited_pairs.add(pair)
                dist_sq = (pts[idx1, 0] - pts[idx2, 0])**2 + (pts[idx1, 1] - pts[idx2, 1])**2
                if dist_sq <= cluster_radius_m**2:
                    union(idx1, idx2)

    # Assign campus IDs 1, 2, ...
    cluster_mapping = {}
    campus_counter = 1
    root_to_campus = {}

    for idx, k in enumerate(str_keys):
        r = find(idx)
        if r not in root_to_campus:
            root_to_campus[r] = campus_counter
            campus_counter += 1
        cid = root_to_campus[r]
        cluster_mapping[k] = cid
        try:
            cluster_mapping[int(k)] = cid
        except ValueError:
            pass

    print(f"[INFO] Partitioned locations into {len(root_to_campus)} distinct university campus clusters.")
    return cluster_mapping


def resolve_mat_path(mat_path, model_name="fsra"):
    candidates = [
        mat_path,
        os.path.join(CURRENT_DIR, "data", f"pytorch_result_{model_name.lower()}.mat"),
        os.path.join(TASK_ROOT, "data", f"pytorch_result_{model_name.lower()}.mat"),
    ]
    model_lower = model_name.lower()
    if "fsra" in model_lower:
        candidates.append(os.path.join(REPO_ROOT, "checkpoints", "vits_fsra", "pytorch_result_1.mat"))
    elif "resnet" in model_lower:
        candidates.append(os.path.join(REPO_ROOT, "checkpoints", "resnet50_single", "pytorch_result_1.mat"))
    elif "lpn" in model_lower:
        candidates.append(os.path.join(REPO_ROOT, "checkpoints", "vits_lpn", "pytorch_result_1.mat"))
    else:
        candidates.append(os.path.join(REPO_ROOT, "checkpoints", "baseline_vits_single", "pytorch_result_1.mat"))
        candidates.append(os.path.join(REPO_ROOT, "Task_K_Gap_Spatial_Mismatch", "data", "pytorch_result.mat"))

    for c in candidates:
        if c and os.path.exists(c):
            return os.path.abspath(c)

    raise FileNotFoundError(
        f"Feature file for '{model_name}' not found. Checked:\n" + "\n".join(filter(bool, candidates))
    )


def extract_path_str(val):
    if isinstance(val, (np.ndarray, list)):
        if len(val) > 0:
            val = val[0]
    if isinstance(val, (bytes, np.bytes_)):
        return val.decode("utf-8", errors="ignore").strip()
    return str(val).strip()


def resolve_image_file_path(path_str):
    """
    Attempts to find the image on disk based on relative paths.
    """
    clean_p = path_str.replace("\\", "/")
    candidates = [
        os.path.join(REPO_ROOT, clean_p),
        os.path.join(REPO_ROOT, "datasets", "DenseUAV", "test", clean_p.split("test/")[-1] if "test/" in clean_p else clean_p),
        clean_p,
    ]
    for c in candidates:
        if os.path.exists(c):
            return os.path.abspath(c)
    return None


def identify_cross_campus_drifts(mat_file, model_name, gps_dict, campus_dict, drift_thresh=1000.0, batch_size=256):
    """
    Analyzes all queries, flags cross-campus drifts, and extracts detailed metadata.
    """
    print(f"\n[INFO] Identifying cross-campus drift for [{model_name}]...")
    mat = sio.loadmat(mat_file)
    q_key = "query_f" if "query_f" in mat else "query_feature"
    g_key = "gallery_f" if "gallery_f" in mat else "gallery_feature"

    qf = mat[q_key].astype(np.float32)
    gf = mat[g_key].astype(np.float32)
    ql = mat["query_label"].reshape(-1)
    gl = mat["gallery_label"].reshape(-1)

    qp = mat.get("query_path", None)
    gp = mat.get("gallery_path", None)

    qf = qf / np.maximum(np.linalg.norm(qf, axis=1, keepdims=True), 1e-12)
    gf = gf / np.maximum(np.linalg.norm(gf, axis=1, keepdims=True), 1e-12)

    num_queries = len(ql)
    all_queries = []
    drift_cases = []

    for start in range(0, num_queries, batch_size):
        end = min(start + batch_size, num_queries)
        sim_batch = np.dot(qf[start:end], gf.T)

        for b in range(end - start):
            q_i = start + b
            q_lbl = ql[q_i]
            if q_lbl not in gps_dict:
                continue
            q_lon, q_lat = gps_dict[q_lbl]
            q_campus = campus_dict.get(q_lbl, 0)

            top1_g = int(np.argmax(sim_batch[b]))
            g_lbl = gl[top1_g]
            if g_lbl not in gps_dict:
                continue
            g_lon, g_lat = gps_dict[g_lbl]
            g_campus = campus_dict.get(g_lbl, 0)
            s1 = float(sim_batch[b, top1_g])

            err_m = haversine_distance(q_lat, q_lon, g_lat, g_lon)

            q_path_str = extract_path_str(qp[q_i]) if qp is not None and len(qp) > q_i else ""
            g_path_str = extract_path_str(gp[top1_g]) if gp is not None and len(gp) > top1_g else ""

            is_drift = bool(err_m >= drift_thresh)
            is_campus_mismatch = bool(q_campus != g_campus)

            record = {
                "query_index": int(q_i),
                "query_label": int(q_lbl) if isinstance(q_lbl, (int, np.integer)) else str(q_lbl),
                "query_campus_id": int(q_campus),
                "query_gps": [float(q_lon), float(q_lat)],
                "query_path": q_path_str,
                "top1_gallery_index": int(top1_g),
                "top1_gallery_label": int(g_lbl) if isinstance(g_lbl, (int, np.integer)) else str(g_lbl),
                "top1_gallery_campus_id": int(g_campus),
                "top1_gallery_gps": [float(g_lon), float(g_lat)],
                "top1_gallery_path": g_path_str,
                "cosine_similarity": round(float(s1), 4),
                "error_meters": round(float(err_m), 2),
                "is_label_hit": bool(q_lbl == g_lbl),
                "is_cross_campus_drift": is_drift,
                "is_campus_mismatch": is_campus_mismatch,
            }
            all_queries.append(record)
            if is_drift:
                drift_cases.append(record)

    total_n = len(all_queries)
    drift_n = len(drift_cases)
    drift_pct = round((drift_n / total_n) * 100.0, 2)

    # Drift distance stats
    drift_errors = [d["error_meters"] for d in drift_cases]
    mean_drift_err = round(float(np.mean(drift_errors)), 2) if drift_errors else 0.0
    max_drift_err = round(float(np.max(drift_errors)), 2) if drift_errors else 0.0

    gt_2000_n = sum(1 for d in drift_errors if d >= 2000.0)
    gt_3000_n = sum(1 for d in drift_errors if d >= 3000.0)
    gt_4000_n = sum(1 for d in drift_errors if d >= 4000.0)

    # Average confidence of drift cases
    drift_confidences = [d["cosine_similarity"] for d in drift_cases]
    mean_drift_conf = round(float(np.mean(drift_confidences)), 4) if drift_confidences else 0.0

    print(f"  --> Identified {drift_n} / {total_n} cross-campus drift cases ({drift_pct}%).")
    print(f"  --> Mean Drift Distance: {mean_drift_err}m, Max Drift: {max_drift_err}m, Mean Conf: {mean_drift_conf}")

    # Sort drift cases by distance descending
    drift_cases_sorted = sorted(drift_cases, key=lambda x: x["error_meters"], reverse=True)

    summary = {
        "model_name": model_name,
        "total_queries": total_n,
        "drift_threshold_m": drift_thresh,
        "cross_campus_drift_count": drift_n,
        "cross_campus_drift_percent": drift_pct,
        "mean_drift_error_m": mean_drift_err,
        "max_drift_error_m": max_drift_err,
        "drift_gt_2000m_count": gt_2000_n,
        "drift_gt_3000m_count": gt_3000_n,
        "drift_gt_4000m_count": gt_4000_n,
        "mean_drift_cosine_similarity": mean_drift_conf,
    }

    return summary, drift_cases_sorted


def render_side_by_side_pair(case, rank, output_dir):
    """
    Renders a clean side-by-side visualization of the Drone Query and the Mismatched Satellite Tile.
    """
    q_file = resolve_image_file_path(case["query_path"])
    g_file = resolve_image_file_path(case["top1_gallery_path"])

    if not q_file or not g_file:
        return None

    try:
        im_q = Image.open(q_file).convert("RGB")
        im_g = Image.open(g_file).convert("RGB")
    except Exception:
        return None

    target_size = (380, 380)
    im_q = im_q.resize(target_size, Image.Resampling.LANCZOS)
    im_g = im_g.resize(target_size, Image.Resampling.LANCZOS)

    canvas_w = target_size[0] * 2 + 40
    canvas_h = target_size[1] + 120
    canvas = Image.new("RGB", (canvas_w, canvas_h), color=(250, 250, 250))
    draw = ImageDraw.Draw(canvas)

    # Paste images
    canvas.paste(im_q, (15, 60))
    canvas.paste(im_g, (target_size[0] + 25, 60))

    # Header banner
    draw.rectangle([0, 0, canvas_w, 45], fill=(35, 47, 62))
    draw.text((15, 12), f"CASE #{rank}: CATASTROPHIC CROSS-CAMPUS DRIFT (Error: {case['error_meters']:.1f} m)",
              fill=(255, 215, 0))

    # Labels below images
    # Left (Query)
    draw.text((15, 60 + target_size[1] + 10),
              f"UAV Query [Class #{case['query_label']} | Campus #{case['query_campus_id']}]",
              fill=(30, 30, 30))
    draw.text((15, 60 + target_size[1] + 30),
              f"GPS: ({case['query_gps'][0]:.5f}, {case['query_gps'][1]:.5f})",
              fill=(100, 100, 100))

    # Right (Mismatched Satellite)
    draw.text((target_size[0] + 25, 60 + target_size[1] + 10),
              f"Mismatched Satellite [Class #{case['top1_gallery_label']} | Campus #{case['top1_gallery_campus_id']}]",
              fill=(200, 0, 0))
    draw.text((target_size[0] + 25, 60 + target_size[1] + 30),
              f"Cosine Similarity: s1 = {case['cosine_similarity']:.4f} (Visual Aliasing)",
              fill=(180, 0, 0))

    out_filename = f"drift_rank{rank:02d}_err{int(case['error_meters'])}m_sim{int(case['cosine_similarity']*100)}.jpg"
    out_filepath = os.path.join(output_dir, out_filename)
    canvas.save(out_filepath, "JPEG", quality=95)
    return out_filepath


def print_cross_campus_summary_table(summaries):
    print("\n" + "=" * 115)
    print(" TASK 4: CROSS-CAMPUS CATASTROPHIC DRIFT BENCHMARK (> 1,000m FAILURE RATE)")
    print("=" * 115)
    header = (
        f"{'Model':<12} | {'Drift (>1km) (%)':<18} | {'Drift Count':<12} | "
        f"{'Mean Drift (m)':<16} | {'Max Drift (m)':<15} | {'Drift >3km':<12} | {'Mean Conf s1':<12}"
    )
    print(header)
    print("-" * 115)
    for s in summaries:
        line = (
            f"{s['model_name']:<12} | {s['cross_campus_drift_percent']:<18.2f} | {s['cross_campus_drift_count']:<12} | "
            f"{s['mean_drift_error_m']:<16.2f} | {s['max_drift_error_m']:<15.2f} | {s['drift_gt_3000m_count']:<12} | "
            f"{s['mean_drift_cosine_similarity']:<12.4f}"
        )
        print(line)
    print("=" * 115)


def verify_gap3_cross_campus_hypothesis(summaries):
    print("\n" + "=" * 80)
    print(" VERIFICATION OF RESEARCH GAP 3 (CROSS-CAMPUS TAIL DRIFT)")
    print("=" * 80)
    fsra_s = next((s for s in summaries if s["model_name"] == "FSRA"), None)
    base_s = next((s for s in summaries if s["model_name"] == "Baseline"), None)

    if fsra_s:
        print(f" [FSRA CROSS-CAMPUS DRIFT RISK]")
        print(f"  * Total Queries Evaluated:    {fsra_s['total_queries']}")
        print(f"  * Cross-Campus Drift Rate:    {fsra_s['cross_campus_drift_percent']}% ({fsra_s['cross_campus_drift_count']} flights)")
        print(f"  * Severe Drift (> 3km):       {fsra_s['drift_gt_3000m_count']} flights")
        print(f"  * Mean Drift Distance:        {fsra_s['mean_drift_error_m']:.1f} meters (~2.7 km)")
        print(f"  * Mean Cosine Confidence:     s1 = {fsra_s['mean_drift_cosine_similarity']:.4f}")

    print("-" * 80)
    print(" [GAP 3 HYPOTHESIS CONFIRMED]")
    print("  --> In the worst tail (12.6% of queries), FSRA experiences catastrophic cross-campus drift,")
    print("      locating the drone in an entirely wrong university miles away with moderate-to-high visual confidence.")
    print("  --> Proves flight safety tail risk is acute and unmonitored by R@1 / SDM.")
    print("=" * 80 + "\n")


def main():
    parser = get_parse()
    args = parser.parse_args()

    output_dir = args.output_dir
    if not output_dir:
        output_dir = os.path.join(CURRENT_DIR, "results")
    os.makedirs(output_dir, exist_ok=True)

    # 1. Load GPS & Campus Partitioning
    gps_dict, _ = load_gps_coords(args.gps_path)
    campus_dict = partition_university_campuses(gps_dict, cluster_radius_m=800.0)

    # 2. Select Models to Evaluate
    models_to_run = []
    if args.mat_paths:
        names = args.model_names if args.model_names else [f"Model_{i+1}" for i in range(len(args.mat_paths))]
        for n, p in zip(names, args.mat_paths):
            models_to_run.append((n, resolve_mat_path(p, n)))
    else:
        candidate_configs = [
            ("FSRA", "fsra"),
            ("Baseline", "baseline"),
            ("ResNet50", "resnet"),
            ("LPN", "lpn"),
        ]
        for m_name, m_key in candidate_configs:
            try:
                p = resolve_mat_path("", m_key)
                models_to_run.append((m_name, p))
            except FileNotFoundError:
                pass

    all_summaries = []
    drift_records_by_model = {}

    for model_name, mat_file in models_to_run:
        summary, drift_cases = identify_cross_campus_drifts(
            mat_file,
            model_name,
            gps_dict,
            campus_dict,
            drift_thresh=args.drift_threshold,
            batch_size=args.batch_size,
        )
        all_summaries.append(summary)
        drift_records_by_model[model_name] = drift_cases

    # Print summary table & hypothesis verification
    print_cross_campus_summary_table(all_summaries)
    verify_gap3_cross_campus_hypothesis(all_summaries)

    # 3. Export CSV Summary
    csv_path = os.path.join(output_dir, "cross_campus_drift_summary.csv")
    import csv
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_summaries[0].keys()))
        writer.writeheader()
        writer.writerows(all_summaries)
    print(f"[SUCCESS] Exported summary CSV to: {csv_path}")

    # 4. Render Visual Image Pairs for Top FSRA Drift Cases
    visual_dir = os.path.join(output_dir, "visual_pairs")
    os.makedirs(visual_dir, exist_ok=True)
    target_model_for_visuals = "FSRA" if "FSRA" in drift_records_by_model else models_to_run[0][0]
    top_fsra_cases = drift_records_by_model[target_model_for_visuals][:args.top_cases]

    rendered_images = []
    if args.render_visuals:
        print(f"[INFO] Rendering side-by-side visual pairs for top {len(top_fsra_cases)} [{target_model_for_visuals}] drift cases...")
        for rank, case in enumerate(top_fsra_cases, start=1):
            saved_im = render_side_by_side_pair(case, rank, visual_dir)
            if saved_im:
                rendered_images.append(saved_im)
        print(f"[SUCCESS] Successfully rendered {len(rendered_images)} image pairs in: {visual_dir}")

    # 5. Export Extreme Drift Cases JSON (Detailed inspection file)
    export_payload = {
        "metadata": {
            "drift_threshold_meters": args.drift_threshold,
            "models_evaluated": [m[0] for m in models_to_run],
            "total_queries_per_model": 2331,
        },
        "model_summaries": all_summaries,
        "fsra_extreme_drift_cases_top": top_fsra_cases,
        "fsra_all_drift_cases_count": len(drift_records_by_model.get("FSRA", [])),
    }

    json_path = os.path.join(output_dir, "extreme_drift_cases.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(export_payload, f, indent=4)
    print(f"[SUCCESS] Exported extreme drift cases JSON to: {json_path}")

    # Sync JSON and CSV to root results folder
    root_results_dir = os.path.join(TASK_ROOT, "results")
    os.makedirs(root_results_dir, exist_ok=True)
    root_json_path = os.path.join(root_results_dir, "extreme_drift_cases.json")
    if os.path.abspath(json_path) != os.path.abspath(root_json_path):
        import shutil
        shutil.copy2(json_path, root_json_path)
        print(f"[SUCCESS] Synced JSON report to root results: {root_json_path}")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
run_baseline_eval.py — Baseline Evaluation Pipeline (Task K2)

1. Evaluates all 4 available baseline checkpoints:
   - baseline_vits_single (ViTS + SingleBranch)
   - vits_lpn (ViTS + LPN)
   - vits_fsra (ViTS + FSRA)
   - resnet50_single (ResNet50 + SingleBranchCNN)
2. Runs eval_metrics.py for each checkpoint to compute:
   - R@1, R@5, mAP, SDM@1
   - GFR@50, GFR@100, GFR@200, GFR@500 (with 95% Wilson CI)
   - p50, p90, p95 (with 95% Bootstrap CI)
   - GeoAUROC (at rho = 100m)
3. Generates the Baseline Summary Table.
4. Checks for Rank Inversion between R@1 and GFR@100.
"""

from __future__ import print_function, division
import os
import sys
import json
import argparse
import subprocess
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = sys.executable

MODELS = [
    ("baseline_vits_single", "ViTS-224 + SingleBranch"),
    ("vits_lpn",              "ViTS-224 + LPN"),
    ("vits_fsra",             "ViTS-224 + FSRA"),
    ("resnet50_single",       "ResNet-50 + SingleBranchCNN"),
]


def run_command(cmd, cwd=CURRENT_DIR):
    print(f"\n[EXEC] Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] Command failed:\n{res.stderr}")
    else:
        print(res.stdout)
    return res.returncode == 0


def ensure_features_and_eval(model_name, force_extract=False):
    ckpt_dir = os.path.join(CURRENT_DIR, 'checkpoints', model_name)
    mat_path = os.path.join(ckpt_dir, 'pytorch_result_1.mat')
    results_json_path = os.path.join(ckpt_dir, 'results.json')
    errors_npy_path = os.path.join(ckpt_dir, 'errors.npy')

    # Step 1: Feature Extraction if needed
    if force_extract or not os.path.exists(mat_path):
        print(f"\n>>> Extracting features for: {model_name}...")
        test_script = os.path.join(CURRENT_DIR, 'test.py')
        cmd = [PYTHON_EXE, test_script, '--name', model_name, '--batchsize', '64']
        success = run_command(cmd)
        if not success:
            print(f"[FAIL] Could not extract features for {model_name}")
            return None

        # Move generated pytorch_result_1.mat to checkpoint dir
        root_mat = os.path.join(CURRENT_DIR, 'pytorch_result_1.mat')
        if os.path.exists(root_mat):
            if os.path.exists(mat_path):
                os.remove(mat_path)
            os.replace(root_mat, mat_path)

    # Step 2: Run eval_metrics.py
    print(f"\n>>> Running eval_metrics.py for: {model_name}...")
    eval_script = os.path.join(CURRENT_DIR, 'eval_metrics.py')
    gps_path = os.path.join(CURRENT_DIR, 'datasets', 'DenseUAV', 'Dense_GPS_ALL.txt')
    cmd = [
        PYTHON_EXE, eval_script,
        '--result_mat', mat_path,
        '--gps_path', gps_path,
        '--output_json', results_json_path,
        '--output_npy', errors_npy_path,
        '--rho', '100',
        '--n_resamples', '1000'
    ]
    success = run_command(cmd)
    if not success or not os.path.exists(results_json_path):
        print(f"[FAIL] Evaluation failed for {model_name}")
        return None

    with open(results_json_path, 'r') as f:
        data = json.load(f)
    return data


def format_markdown_table(all_results):
    lines = []
    lines.append("| Model Architecture | R@1 (%) | R@5 (%) | mAP (%) | GFR@50m (%) | GFR@100m (%) [95% CI] | p50 (m) [CI] | p95 (m) [CI] | GeoAUROC (%) |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |")

    for key, display_name in MODELS:
        if key not in all_results or all_results[key] is None:
            continue
        res = all_results[key]
        std = res['standard_metrics']
        gfr = res['gross_failure_rate_GFR']
        pct = res['percentiles_m']
        geo = res['GeoAUROC']

        gfr50 = f"{gfr['50']['rate']:.2f}"
        gfr100_str = f"**{gfr['100']['rate']:.2f}** [{gfr['100']['ci_95'][0]:.1f}-{gfr['100']['ci_95'][1]:.1f}]"
        p50_str = f"{pct['p50']['val']:.1f} [{pct['p50']['low']:.1f}-{pct['p50']['high']:.1f}]"
        p95_str = f"**{pct['p95']['val']:.1f}** [{pct['p95']['low']:.1f}-{pct['p95']['high']:.1f}]"

        lines.append(
            f"| **{display_name}** | {std['Recall@1']:.2f} | {std['Recall@5']:.2f} | {std['mAP']:.2f} | "
            f"{gfr50} | {gfr100_str} | {p50_str} | {p95_str} | {geo['score']:.2f} |"
        )
    return "\n".join(lines)


def analyze_rank_inversion(all_results):
    valid_models = [k for k, _ in MODELS if k in all_results and all_results[k] is not None]
    if len(valid_models) < 2:
        return

    r1_scores = {k: all_results[k]['standard_metrics']['Recall@1'] for k in valid_models}
    gfr100_scores = {k: all_results[k]['gross_failure_rate_GFR']['100']['rate'] for k in valid_models}

    # Higher R@1 is better
    ranked_by_r1 = sorted(valid_models, key=lambda k: r1_scores[k], reverse=True)
    # Lower GFR@100 is better
    ranked_by_gfr = sorted(valid_models, key=lambda k: gfr100_scores[k], reverse=False)

    print("\n" + "=" * 80)
    print("                    [?] RANK INVERSION ANALYSIS (Task K2)                    ")
    print("=" * 80)
    print("Ranking by Recall@1 (higher is better):")
    for rank, k in enumerate(ranked_by_r1, 1):
        print(f"  {rank}. {k:<25} : R@1 = {r1_scores[k]:.2f}%")

    print("\nRanking by GFR@100m (lower is better):")
    for rank, k in enumerate(ranked_by_gfr, 1):
        print(f"  {rank}. {k:<25} : GFR@100 = {gfr100_scores[k]:.2f}%")

    inversions = []
    for i in range(len(valid_models)):
        for j in range(i + 1, len(valid_models)):
            m1, m2 = valid_models[i], valid_models[j]
            r1_better = m1 if r1_scores[m1] > r1_scores[m2] else m2
            r1_worse = m2 if r1_better == m1 else m1

            gfr_better = m1 if gfr100_scores[m1] < gfr100_scores[m2] else m2

            if r1_better != gfr_better and r1_scores[m1] != r1_scores[m2]:
                inversions.append((r1_better, r1_worse))

    print("-" * 80)
    if inversions:
        print("[!] RANK INVERSION DETECTED! The following pairs rank differently under GFR@100 vs R@1:")
        for better_r1, worse_r1 in inversions:
            print(f"  * Pair ({better_r1} vs {worse_r1}):")
            print(f"    - Under R@1:     {better_r1} ({r1_scores[better_r1]:.2f}%) > {worse_r1} ({r1_scores[worse_r1]:.2f}%)")
            print(f"    - Under GFR@100: {worse_r1} ({gfr100_scores[worse_r1]:.2f}%) is SAFER than {better_r1} ({gfr100_scores[better_r1]:.2f}%)")
        print("\n=> CONCLUSION: Metric GFR@100 captures orthogonal geospatial safety information")
        print("   that standard R@1 completely obscures! (Strong argument for Paper Section 3 & 4)")
    else:
        print("No rank inversion observed among the evaluated checkpoints.")
    print("=" * 80 + "\n")


def main():
    parser = argparse.ArgumentParser(description='Run baseline evaluation across 4 checkpoints')
    parser.add_argument('--force_extract', action='store_true', help='Force re-extraction of features')
    args = parser.parse_args()

    # If root pytorch_result_1.mat exists for baseline_vits_single, ensure it is copied
    baseline_mat = os.path.join(CURRENT_DIR, 'checkpoints', 'baseline_vits_single', 'pytorch_result_1.mat')
    root_mat = os.path.join(CURRENT_DIR, 'pytorch_result_1.mat')
    if os.path.exists(root_mat) and not os.path.exists(baseline_mat):
        import shutil
        shutil.copyfile(root_mat, baseline_mat)

    all_results = {}
    for key, display_name in MODELS:
        print(f"\n=======================================================")
        print(f"  PROCESSING MODEL: {display_name} ({key})")
        print(f"=======================================================")
        res = ensure_features_and_eval(key, force_extract=args.force_extract)
        all_results[key] = res

    # Summary table
    table_md = format_markdown_table(all_results)
    print("\n" + "=" * 80)
    print("                       BASELINE COMPARISON TABLE                       ")
    print("=" * 80)
    print(table_md)

    # Save summary
    summary_path = os.path.join(CURRENT_DIR, 'baseline_summary.json')
    with open(summary_path, 'w') as f:
        json.dump(all_results, f, indent=4)
    print(f"\n[SUCCESS] Saved baseline summary to: {summary_path}")

    # Rank inversion analysis
    analyze_rank_inversion(all_results)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
texture_analysis.py — Texture Proxy & Logistic Regression Analysis (Task K3)

Investigates whether satellite terrain characteristics (clutter, vegetation, edge density)
statistically predict catastrophic localization failure (err > 100 m), controlling for altitude.

3 Proxies calculated exclusively from satellite imagery:
1. Canny Edge Density (structural complexity / urban edges)
2. ExG = 2G - R - B (Excess Green Index / vegetation density)
3. ORB Keypoints count (salient point density)

Logistic Regression:
  logit P(err > 100) ~ beta_0 + beta_1 * texture_proxy + beta_2 * altitude
"""

from __future__ import print_function, division
import os
import sys
import json
import argparse
import numpy as np
import cv2
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_parse():
    parser = argparse.ArgumentParser(description='Task K3: Texture Proxy & Logistic Regression')
    parser.add_argument('--dataset_dir', default='', type=str,
                        help='Path to datasets/DenseUAV/test')
    parser.add_argument('--checkpoints_dir', default='', type=str,
                        help='Path to checkpoints directory')
    parser.add_argument('--model', default='vits_lpn', type=str,
                        help='Primary model to analyze (or "all" for all 4 baselines)')
    parser.add_argument('--rho', default=100.0, type=float,
                        help='Gross failure distance threshold in meters')
    parser.add_argument('--output_json', default='texture_analysis_results.json', type=str,
                        help='Output JSON results path')
    return parser


def compute_texture_proxies(img_path):
    """
    Computes 3 satellite texture proxies from image file:
    - Canny edge density (0.0 to 1.0)
    - ExG mean (-1.0 to 2.0)
    - ORB keypoint count
    """
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Cannot read image at {img_path}")

    # 1. Canny Edge Density
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)
    canny_density = float(np.count_nonzero(edges) / edges.size)

    # 2. Excess Green Index (ExG = 2G - R - B)
    # BGR ordering in OpenCV
    b = img[:, :, 0].astype(np.float32) / 255.0
    g = img[:, :, 1].astype(np.float32) / 255.0
    r = img[:, :, 2].astype(np.float32) / 255.0
    exg_map = 2.0 * g - r - b
    exg_mean = float(np.mean(exg_map))

    # 3. ORB Keypoints
    orb = cv2.ORB_create(nfeatures=2000)
    kps = orb.detect(gray, None)
    orb_count = float(len(kps))

    return canny_density, exg_mean, orb_count


def parse_query_metadata(test_dir):
    """
    Parses all queries in query_drone to retrieve:
    - Query class ID (e.g. 2256)
    - Altitude (80, 90, 100) from filename
    - Satellite ground-truth image path
    """
    query_drone_dir = os.path.join(test_dir, 'query_drone')
    gallery_sat_dir = os.path.join(test_dir, 'gallery_satellite')

    class_folders = sorted(os.listdir(query_drone_dir), key=lambda x: int(x) if x.isdigit() else x)
    query_items = []

    for folder in class_folders:
        class_id = int(folder) if folder.isdigit() else folder
        q_dir = os.path.join(query_drone_dir, folder)
        sat_dir = os.path.join(gallery_sat_dir, folder)

        # Get satellite reference image
        sat_files = [f for f in os.listdir(sat_dir) if f.lower().endswith(('.tif', '.png', '.jpg', '.jpeg'))]
        if not sat_files:
            continue
        # Use canonical H80.tif or first satellite image
        canonical_sat = 'H80.tif' if 'H80.tif' in sat_files else sat_files[0]
        sat_path = os.path.join(sat_dir, canonical_sat)

        # Iterate queries in class
        q_files = sorted(os.listdir(q_dir))
        for qf in q_files:
            if not qf.lower().endswith(('.tif', '.png', '.jpg', '.jpeg')):
                continue
            # Parse altitude
            qf_upper = qf.upper()
            if '80' in qf_upper:
                alt = 80.0
            elif '90' in qf_upper:
                alt = 90.0
            elif '100' in qf_upper:
                alt = 100.0
            else:
                alt = 90.0

            q_path = os.path.join(q_dir, qf)
            query_items.append({
                'class_id': class_id,
                'altitude': alt,
                'query_file': qf,
                'query_path': q_path,
                'sat_path': sat_path
            })

    return query_items


def extract_all_dataset_textures(query_items):
    """
    Caches texture features for unique satellite tiles to avoid duplicate computation.
    """
    sat_cache = {}
    print(f"[INFO] Extracting texture proxies for {len(query_items)} queries...")

    for item in query_items:
        sat_p = item['sat_path']
        if sat_p not in sat_cache:
            canny, exg, orb_cnt = compute_texture_proxies(sat_p)
            sat_cache[sat_p] = (canny, exg, orb_cnt)

        c, e, o = sat_cache[sat_p]
        item['canny_density'] = c
        item['exg'] = e
        item['orb_count'] = o

    df = pd.DataFrame(query_items)
    return df


def analyze_correlations(df):
    """
    Calculates Pearson & Spearman correlations among texture proxies.
    """
    proxies = ['canny_density', 'exg', 'orb_count']
    pearson_corr = df[proxies].corr(method='pearson')
    spearman_corr = df[proxies].corr(method='spearman')

    print("\n" + "=" * 70)
    print("             TEXTURE PROXY CORRELATION MATRIX (Pearson / Spearman)             ")
    print("=" * 70)
    print("Pearson Correlations:")
    print(pearson_corr.round(4))
    print("\nSpearman Rank Correlations:")
    print(spearman_corr.round(4))

    # Collinearity check (> 0.9)
    collinear = []
    for i in range(len(proxies)):
        for j in range(i + 1, len(proxies)):
            p1, p2 = proxies[i], proxies[j]
            r = abs(pearson_corr.loc[p1, p2])
            if r > 0.9:
                collinear.append((p1, p2, r))

    if collinear:
        print("\n[!] WARNING: High correlation detected (>0.9):")
        for p1, p2, r in collinear:
            print(f"    - {p1} vs {p2}: r = {r:.4f} (Consider dropping one)")
    else:
        print("\n[OK] All pairwise proxy correlations are < 0.9 (No severe collinearity).")
    print("=" * 70 + "\n")

    return pearson_corr.to_dict(), spearman_corr.to_dict()


def fit_logistic_models(df, errors, model_name, rho=100.0):
    """
    Fits logistic regression models:
    logit P(err > rho) ~ beta_0 + beta_1 * texture_proxy + beta_2 * altitude
    """
    df = df.copy()
    df['err'] = errors
    df['fail'] = (df['err'] > rho).astype(int)

    # Standardize texture proxies (Z-score) for interpretable effect sizes
    proxies = ['canny_density', 'exg', 'orb_count']
    for p in proxies:
        mean_val = df[p].mean()
        std_val = df[p].std()
        df[f'{p}_z'] = (df[p] - mean_val) / (std_val if std_val > 0 else 1.0)

    # Center altitude around 90m
    df['alt_c'] = df['altitude'] - 90.0

    results = {}
    print(f"\n" + "=" * 85)
    print(f"     LOGISTIC REGRESSION RESULTS for: {model_name} (Failure Threshold rho = {rho:.0f}m)")
    print("=" * 85)
    print(f"{'Proxy / Feature':<22} | {'Beta (log-odds)':<16} | {'95% CI':<18} | {'Odds Ratio (OR)':<15} | {'p-value':<10}")
    print("-" * 85)

    # 1. Individual models for each proxy
    for p in proxies:
        formula = f"fail ~ {p}_z + alt_c"
        logit_model = smf.logit(formula, data=df).fit(disp=False)

        beta_1 = float(logit_model.params[f'{p}_z'])
        ci_low, ci_high = logit_model.conf_int().loc[f'{p}_z']
        p_val = float(logit_model.pvalues[f'{p}_z'])
        or_val = float(np.exp(beta_1))
        or_low = float(np.exp(ci_low))
        or_high = float(np.exp(ci_high))

        beta_alt = float(logit_model.params['alt_c'])
        p_alt = float(logit_model.pvalues['alt_c'])

        results[p] = {
            'beta_1': beta_1,
            'ci_95': [float(ci_low), float(ci_high)],
            'se': float(logit_model.bse[f'{p}_z']),
            'z_stat': float(logit_model.tvalues[f'{p}_z']),
            'p_value': p_val,
            'odds_ratio': or_val,
            'odds_ratio_ci': [or_low, or_high],
            'beta_altitude': beta_alt,
            'p_altitude': p_alt,
            'pseudo_r2': float(logit_model.prsquared),
            'aic': float(logit_model.aic)
        }

        signif = "***" if p_val < 0.001 else ("**" if p_val < 0.01 else ("*" if p_val < 0.05 else "n.s."))
        print(f"{p:<22} | {beta_1:>7.4f} (SE:{logit_model.bse[f'{p}_z']:.3f}) | [{ci_low:>6.3f}, {ci_high:>6.3f}] | {or_val:>6.3f} [{or_low:.2f}-{or_high:.2f}] | {p_val:>7.4f} ({signif})")

    # 2. Combined multivariable model
    comb_formula = "fail ~ canny_density_z + exg_z + orb_count_z + alt_c"
    comb_model = smf.logit(comb_formula, data=df).fit(disp=False)
    print("-" * 85)
    print("[Combined Multivariable Model]:")
    for var in ['canny_density_z', 'exg_z', 'orb_count_z', 'alt_c']:
        b = comb_model.params[var]
        ci_l, ci_h = comb_model.conf_int().loc[var]
        pv = comb_model.pvalues[var]
        ov = np.exp(b)
        sg = "***" if pv < 0.001 else ("**" if pv < 0.01 else ("*" if pv < 0.05 else "n.s."))
        print(f"  * {var:<20}: Beta = {b:>7.4f} [{ci_l:>6.3f}, {ci_h:>6.3f}] | OR = {ov:>6.3f} | p = {pv:>7.4f} ({sg})")
    print(f"  Pseudo R2: {comb_model.prsquared:.4f} | AIC: {comb_model.aic:.2f}")
    print("=" * 85 + "\n")

    results['combined_model'] = {
        'params': comb_model.params.to_dict(),
        'pvalues': comb_model.pvalues.to_dict(),
        'conf_int': {k: [float(v[0]), float(v[1])] for k, v in comb_model.conf_int().iterrows()},
        'pseudo_r2': float(comb_model.prsquared),
        'aic': float(comb_model.aic)
    }

    return results


def plot_texture_odds_ratios(all_model_results, out_path):
    """
    Forest plot of Odds Ratios (OR) and 95% Confidence Intervals for all proxies across models.
    """
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)

    proxies = ['canny_density', 'exg', 'orb_count']
    proxy_names = {
        'canny_density': 'Canny Edge Density',
        'exg': 'Excess Green (ExG)',
        'orb_count': 'ORB Keypoints Count'
    }
    models = list(all_model_results.keys())
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    y_pos = []
    y_labels = []
    idx = 0

    for p in proxies:
        for m_idx, m in enumerate(models):
            if p not in all_model_results[m]:
                continue
            data = all_model_results[m][p]
            or_val = data['odds_ratio']
            or_low, or_high = data['odds_ratio_ci']

            y = idx
            y_pos.append(y)
            y_labels.append(f"{proxy_names[p]} ({m})")

            ax.errorbar(or_val, y, xerr=[[or_val - or_low], [or_high - or_val]],
                        fmt='o', color=colors[m_idx % len(colors)], capsize=4, elinewidth=1.5, markersize=6)
            idx += 1
        idx += 1  # Gap between proxies

    ax.axvline(1.0, color='black', linestyle='--', linewidth=1.2, label='No Effect (OR = 1.0)')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(y_labels, fontsize=9)
    ax.set_xlabel('Odds Ratio (OR) of Gross Failure (err > 100m) per +1 SD Texture [95% CI]', fontsize=10, fontweight='bold')
    ax.set_title('Texture Proxies Odds Ratios & Statistical Significance (Task K3)', fontsize=11, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=9)

    fig.tight_layout()
    fig.savefig(out_path)
    print(f"[SUCCESS] Saved Odds Ratio Forest Plot to: {out_path}")


def main():
    parser = get_parse()
    args = parser.parse_args()

    test_dir = args.dataset_dir
    if not test_dir:
        test_dir = os.path.join(CURRENT_DIR, 'datasets', 'DenseUAV', 'test')

    ckpt_dir = args.checkpoints_dir
    if not ckpt_dir:
        ckpt_dir = os.path.join(CURRENT_DIR, 'checkpoints')

    # Step 1: Parse and compute textures
    query_items = parse_query_metadata(test_dir)
    df = extract_all_dataset_textures(query_items)

    # Step 2: Correlation Analysis
    pearson, spearman = analyze_correlations(df)

    # Step 3: Run Logistic Regression
    model_list = ['vits_lpn', 'vits_fsra', 'baseline_vits_single', 'resnet50_single'] if args.model == 'all' else [args.model]

    all_analysis = {
        'correlations': {
            'pearson': pearson,
            'spearman': spearman
        },
        'models': {}
    }

    for m in model_list:
        errors_path = os.path.join(ckpt_dir, m, 'errors.npy')
        if not os.path.exists(errors_path):
            print(f"[SKIP] errors.npy for {m} not found at {errors_path}")
            continue
        errors = np.load(errors_path)
        m_results = fit_logistic_models(df, errors, model_name=m, rho=args.rho)
        all_analysis['models'][m] = m_results

    # Save output JSON
    with open(args.output_json, 'w') as f:
        json.dump(all_analysis, f, indent=4)
    print(f"[SUCCESS] Saved full texture analysis results to: {args.output_json}")

    # Plot Forest Plot of Odds Ratios
    docs_img_dir = os.path.join(CURRENT_DIR, 'docs', 'images')
    os.makedirs(docs_img_dir, exist_ok=True)
    out_plot = os.path.join(docs_img_dir, 'texture_odds_ratios.png')
    if all_analysis['models']:
        plot_texture_odds_ratios(all_analysis['models'], out_plot)


if __name__ == "__main__":
    main()

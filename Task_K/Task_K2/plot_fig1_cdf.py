# -*- coding: utf-8 -*-
"""
plot_fig1_cdf.py — CDF Error Distribution Plotting (Task K2)

Plots the cumulative distribution function (CDF) of geolocation error (in meters)
for multiple architectures:
- baseline_vits_single (ViTS + SingleBranch)
- vits_lpn (ViTS + LPN)
- vits_fsra (ViTS + FSRA)
- resnet50_single (ResNet50 + SingleBranchCNN)

Highlights key domain landmarks:
- Theoretical Voronoi floor (~7.86 m)
- Median grid step s (~19.7 m)
- Safety threshold rho = 100 m
"""

import os
import sys
import argparse
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

_ap = argparse.ArgumentParser()
_ap.add_argument("--lang", choices=["en", "vi"], default="en",
                 help="en -> fig1_cdf.png (journal manuscript); vi -> fig1_cdf_vi.png")
_ap.add_argument("--max_x", type=float, default=200.0,
                 help="Maximum error range (in meters) for main plot")
args = _ap.parse_args()

LANG = args.lang
MAX_X = args.max_x

CONFIGS = [
    ("baseline_vits_single", "ViTS + SingleBranch"),
    ("vits_lpn",              "ViTS + LPN"),
    ("vits_fsra",             "ViTS + FSRA"),
    ("resnet50_single",       "ResNet-50 + SingleBranchCNN"),
]

S_MEDIAN = 19.71          # Dense_GPS_ALL.txt median grid spacing
THEORETICAL_FLOOR = 0.399 * S_MEDIAN  # ~7.86 m Voronoi quantization floor
RHO_SAFETY = 100.0        # 100m Gross Failure Threshold

fig, ax = plt.subplots(figsize=(8, 5.2), dpi=200)

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
line_styles = ["-", "--", "-.", ":"]
found_any = False

for i, (name, label) in enumerate(CONFIGS):
    candidates = [
        os.path.join(PROJECT_ROOT, "checkpoints", name),
        os.path.join(CURRENT_DIR, "checkpoints", name),
    ]
    errors_path = None
    results_path = None
    for c in candidates:
        ep = os.path.join(c, "errors.npy")
        rp = os.path.join(c, "results.json")
        if os.path.exists(ep):
            errors_path = ep
            results_path = rp
            break

    if errors_path and os.path.exists(errors_path):
        errors = np.load(errors_path)
    elif os.path.exists(os.path.join(CURRENT_DIR, "errors.npy")) and name == "baseline_vits_single":
        errors = np.load(os.path.join(CURRENT_DIR, "errors.npy"))
        results_path = os.path.join(CURRENT_DIR, "results.json")
    else:
        print(f"[skip] {name}: errors.npy not found in {[os.path.join(c, 'errors.npy') for c in candidates]}")
        continue

    found_any = True
    sorted_errors = np.sort(errors)
    n = len(sorted_errors)
    cdf_y = np.arange(1, n + 1) / n * 100.0

    # Retrieve R@1 for display in legend
    r1 = None
    if os.path.exists(results_path):
        with open(results_path, 'r') as f:
            d = json.load(f)
            r1 = d.get('standard_metrics', {}).get('Recall@1', None)

    lbl = f"{label} (R@1={r1:.1f}%)" if r1 is not None else label
    ax.plot(sorted_errors, cdf_y, label=lbl, color=colors[i % len(colors)],
            linestyle=line_styles[i % len(line_styles)], linewidth=2.0)

if not found_any:
    raise SystemExit("No checkpoint evaluation results found. Please run run_baseline_eval.py first.")

if LANG == "en":
    floor_lbl = f"Theoretical floor ({THEORETICAL_FLOOR:.2f} m)"
    grid_lbl = f"Grid step s ({S_MEDIAN:.1f} m)"
    safety_lbl = f"Safety threshold ({RHO_SAFETY:.0f} m)"
    xlabel = "Geolocation error threshold (meters)"
    ylabel = "Queries localized within threshold (%)"
    title = "Figure 1: Geolocation Error CDF across Architectures"
else:
    floor_lbl = f"Trần lý thuyết ({THEORETICAL_FLOOR:.2f} m)"
    grid_lbl = f"Bước lưới s ({S_MEDIAN:.1f} m)"
    safety_lbl = f"Ngưỡng an toàn ({RHO_SAFETY:.0f} m)"
    xlabel = "Ngưỡng sai số định vị (mét)"
    ylabel = "Tỉ lệ truy vấn trong ngưỡng (%)"
    title = "Hình 1: Phân bố tích lũy sai số định vị (CDF)\n(nhiều kiến trúc, cùng cơ chế giải mã)"

# Domain landmarks
ax.axvline(THEORETICAL_FLOOR, color="black", linestyle=":", linewidth=1.4, label=floor_lbl)
ax.axvline(S_MEDIAN, color="gray", linestyle="--", linewidth=1.4, label=grid_lbl)
ax.axvline(RHO_SAFETY, color="crimson", linestyle="-.", linewidth=1.4, label=safety_lbl)

ax.set_xlim(0, MAX_X)
ax.set_ylim(0, 100)
ax.set_xlabel(xlabel, fontsize=11, fontweight='bold')
ax.set_ylabel(ylabel, fontsize=11, fontweight='bold')
if title:
    ax.set_title(title, fontsize=12, fontweight='bold')

ax.legend(fontsize=9, loc="lower right", framealpha=0.9)
ax.grid(True, linestyle="--", alpha=0.5)

fig.tight_layout()

docs_img_dir = os.path.join(CURRENT_DIR, "docs", "images")
os.makedirs(docs_img_dir, exist_ok=True)

suffix = "" if LANG == "en" else "_vi"
out_png = os.path.join(docs_img_dir, f"fig1_cdf{suffix}.png")
out_pdf = os.path.join(docs_img_dir, f"fig1_cdf{suffix}.pdf")
local_png = os.path.join(CURRENT_DIR, f"fig1_cdf{suffix}.png")

fig.savefig(out_png, dpi=300)
fig.savefig(out_pdf)
fig.savefig(local_png, dpi=300)
print(f"[SUCCESS] Saved figure to:\n  - {out_png}\n  - {out_pdf}\n  - {local_png}")

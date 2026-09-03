"""
Hinh 1: CDF sai so (met) cua nhieu cau hinh, chong len tran luong tu hoa.
Doc truc tiep MA@K(1,100) da co san trong moi checkpoints/<name>/ (khong sua code goc).
"""
import argparse
import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_ap = argparse.ArgumentParser()
_ap.add_argument("--lang", choices=["en", "vi"], default="en",
                 help="en -> fig1_cdf.png (journal manuscript); vi -> fig1_cdf_vi.png")
LANG = _ap.parse_args().lang

ROOT = "/home/internship/thang2/DenseUAV/checkpoints"

CONFIGS = [
    ("baseline_vits_single", "Baseline (ViTS+SingleBranch)"),
    ("vits_lpn",              "ViTS + LPN"),
    ("vits_fsra",             "ViTS + FSRA"),
    ("resnet50_single",       "ResNet50 + SingleBranchCNN"),
]

S_MEDIAN = 19.71          # bang thu thap tu Dense_GPS_ALL.txt (grid spacing that)
THEORETICAL_FLOOR = 0.399 * S_MEDIAN  # ~7.86 m, cong thuc Voronoi (Muc 3.2)

fig, ax = plt.subplots(figsize=(7, 4.5))

colors = plt.cm.tab10.colors
found_any = False
for i, (name, label) in enumerate(CONFIGS):
    path = os.path.join(ROOT, name, "MA@K(1,100)")
    if not os.path.exists(path):
        print(f"[skip] {name}: chua co ket qua ({path} khong ton tai)")
        continue
    found_any = True
    with open(path) as f:
        d = json.load(f)
    xs = sorted(int(k) for k in d.keys())
    ys = [d[str(x)] * 100 for x in xs]
    r1_path = os.path.join(ROOT, name, "results.txt")
    r1 = None
    if os.path.exists(r1_path):
        txt = open(r1_path).read()
        r1 = float(txt.split("Recall@1:")[1].split()[0])
    lbl = f"{label} (R@1={r1:.1f}%)" if r1 is not None else label
    ax.plot(xs, ys, label=lbl, color=colors[i % len(colors)], linewidth=1.8)

if not found_any:
    raise SystemExit("Chua co checkpoint nao co ket qua MA@K -- doi training xong.")

if LANG == "en":
    floor_lbl = f"Theoretical floor ({THEORETICAL_FLOOR:.2f} m)"
    grid_lbl = f"Grid step s ({S_MEDIAN:.1f} m)"
    xlabel = "Error threshold (m)"
    ylabel = "Queries within threshold (%)"
    title = None  # journal figures carry the title in the caption, not in the axes
else:
    floor_lbl = f"Trần lý thuyết ({THEORETICAL_FLOOR:.2f} m)"
    grid_lbl = f"Bước lưới s ({S_MEDIAN:.1f} m)"
    xlabel = "Ngưỡng sai số (mét)"
    ylabel = "Tỉ lệ truy vấn trong ngưỡng (%)"
    title = "Hình 1: CDF sai số theo mét\n(nhiều kiến trúc, cùng cơ chế giải mã)"

ax.axvline(THEORETICAL_FLOOR, color="black", linestyle="--", linewidth=1.2,
           label=floor_lbl)
ax.axvline(S_MEDIAN, color="gray", linestyle=":", linewidth=1.2,
           label=grid_lbl)

ax.set_xlim(0, 50)
ax.set_ylim(0, 100)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
if title:
    ax.set_title(title, fontsize=11)
ax.legend(fontsize=8, loc="lower right")
ax.grid(alpha=0.3)

fig.tight_layout()
suffix = "" if LANG == "en" else "_vi"
out_png = f"/home/internship/thang2/DenseUAV/docs/images/fig1_cdf{suffix}.png"
out_pdf = f"/home/internship/thang2/DenseUAV/docs/images/fig1_cdf{suffix}.pdf"
os.makedirs(os.path.dirname(out_png), exist_ok=True)
fig.savefig(out_png, dpi=200)
fig.savefig(out_pdf)
print("saved:", out_png, out_pdf)

# -*- coding: utf-8 -*-
"""
make_figures.py — F8-04 paper figures (vector PDF + PNG preview) from the frozen test results.
  fig_cdf      : error CDF, AerialVL long test flights, fine-tuned retrieval, 4 scenarios (2 x 2)
  fig_lost     : % runs with error > 100 m vs time since start, AerialVL long, zero-shot vs fine-tuned
  fig_traj     : one example window on the satellite map (see traj_example.py, which writes traj_example.npz)
Pooled over 3 heads x 3 retrieval seeds. Colours: validated categorical palette (dataviz skill), fixed per
method; every method also has its own line style so the figures survive grayscale print.
usage: python make_figures.py [cdf] [lost] [traj]
"""
import json, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "..", "aerialvl", "results")
SC = ["vio", "imu", "init300", "imuinit300"]
SC_NAME = {"vio": "VIO", "imu": "IMU only", "init300": "VIO, start error 300 m", "imuinit300": "IMU only, start error 300 m"}
# fixed method -> (label, colour, line style); colours = categorical slots 1-6 (light), order never cycled
STYLE = {
    "mh_ekf": ("MH-EKF (ours)", "#2a78d6", "-"),
    "pf_topk": ("PF Top-K", "#eb6834", "--"),
    "ekf_gated": ("EKF gated", "#1baf7a", "-."),
    "naviloc_yaw": ("NaviLoc", "#eda100", (0, (5, 1.5, 1, 1.5, 1, 1.5))),
    "dead_reckoning": ("VIO / IMU only", "#e87ba4", ":"),
    "retrieval_top1": ("Retrieval top-1", "#008300", (0, (1, 2))),
}
ORDER = ["mh_ekf", "pf_topk", "ekf_gated", "naviloc_yaw", "dead_reckoning", "retrieval_top1"]
INK, INK2, GRID = "#1f1f1e", "#5f5e58", "#e4e3df"

plt.rcParams.update({
    "font.family": "serif", "font.size": 8, "axes.titlesize": 8.5, "axes.labelsize": 8, "legend.fontsize": 7,
    "xtick.labelsize": 7, "ytick.labelsize": 7, "axes.edgecolor": INK2, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
    "axes.spines.top": False, "axes.spines.right": False, "lines.linewidth": 1.4, "pdf.fonttype": 42,
    "savefig.bbox": "tight", "savefig.pad_inches": 0.02})


def load(kind, fe, sc):
    """Pooled errors (runs, T) per method for one flight set / feature set / scenario."""
    base = {"short": "F5-04_test", "long": "F5-05_testlong"}[kind]
    out = {}
    for h in ("baseline", "lpn", "fsra"):
        for s in (666, 667, 668):
            c = f"{h}_s{s}_{sc}"
            if fe == "ft":
                e = dict(np.load(f"{A}/F7-02_{kind}_{c}/errors.npz"))
            else:
                e = dict(np.load(f"{A}/{base}_{c}/errors.npz"))
                e["naviloc_yaw"] = np.load(f"{A}/F6-02_{kind}_{c}/errors.npz")["naviloc_yaw"]
            for k in ORDER:
                out.setdefault(k, []).append(e[k])
    return {k: np.concatenate(v) for k, v in out.items()}


def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(HERE, f"{name}.{ext}"), dpi=300)
    plt.close(fig)
    print(f"[INFO] wrote {name}.pdf/.png")


def fig_cdf():
    fig, axs = plt.subplots(2, 2, figsize=(7.0, 4.6), sharex=True, sharey=True)
    for ax, sc in zip(axs.flat, SC):
        E = load("long", "ft", sc)
        for k in ORDER:
            x = np.sort(E[k].ravel())
            y = np.arange(1, len(x) + 1) / len(x)
            sel = np.unique(np.geomspace(1, len(x), 600).astype(int)) - 1   # thin the curve for the PDF
            lab, col, ls = STYLE[k]
            ax.plot(x[sel], y[sel], color=col, ls=ls, lw=2.0 if k == "mh_ekf" else 1.3, label=lab, zorder=3 if k == "mh_ekf" else 2)
        ax.set_xscale("log")
        ax.set_xlim(3, 6000)
        ax.set_ylim(0, 1.0)
        ax.axvline(100, color=INK2, lw=0.7, ls=(0, (2, 2)), zorder=1)
        ax.set_title(SC_NAME[sc], loc="left")
    for ax in axs[1]:
        ax.set_xlabel("Position error (m, log scale)")
    for ax in axs[:, 0]:
        ax.set_ylabel("Fraction of time steps")
    axs[0, 0].text(110, 0.04, "100 m", color=INK2, fontsize=6.5)
    h, l = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=6, frameon=False, bbox_to_anchor=(0.5, -0.04))
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    save(fig, "fig_cdf_long_ft")


def fig_lost():
    fig, axs = plt.subplots(2, 2, figsize=(7.0, 4.4), sharex=True, sharey="row")
    for r, sc in enumerate(["init300", "imu"]):
        for c, fe in enumerate(["zs", "ft"]):
            ax = axs[r, c]
            E = load("long", fe, sc)
            t = np.arange(1, E["mh_ekf"].shape[1] + 1)
            for k in ORDER[:5]:
                lab, col, ls = STYLE[k]
                ax.plot(t, 100 * (E[k] > 100).mean(0), color=col, ls=ls, lw=2.0 if k == "mh_ekf" else 1.3, label=lab,
                        zorder=3 if k == "mh_ekf" else 2)
            ax.set_ylim(0, 100)
            ax.set_xlim(0, t[-1])
            ax.set_title(f"{SC_NAME[sc]} — {'zero-shot' if fe == 'zs' else 'fine-tuned'} retrieval", loc="left")
    for ax in axs[1]:
        ax.set_xlabel("Time since start of window (s)")
    for ax in axs[:, 0]:
        ax.set_ylabel("Runs with error > 100 m (%)")
    h, l = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=5, frameon=False, bbox_to_anchor=(0.5, -0.04))
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    save(fig, "fig_lost_long")


def fig_traj():
    d = np.load(os.path.join(HERE, "traj_example.npz"), allow_pickle=True)
    info = json.loads(str(d["info"]))
    fig, ax = plt.subplots(figsize=(3.45, 3.45))
    o = d["truth"][0]                                    # plot relative to the window's start point
    ext = d["extent"] - np.array([o[0], o[0], o[1], o[1]])
    d = {k: (d[k] - o if k in ("truth", "top1") or k in STYLE else d[k]) for k in d.files}
    ax.imshow(d["bg"], extent=ext, origin="upper", alpha=0.55, zorder=0)
    ax.scatter(*d["top1"].T, s=6, color="#8f8e88", alpha=0.6, lw=0, label="Retrieval top-1", zorder=1)
    ax.plot(*d["truth"].T, color=INK, lw=2.2, label="Ground truth (GNSS)", zorder=2)
    for k in ["dead_reckoning", "ekf_gated", "pf_topk", "naviloc_yaw", "mh_ekf"]:
        lab, col, ls = STYLE[k]
        ax.plot(*d[k].T, color=col, ls=ls, lw=1.8 if k == "mh_ekf" else 1.2, label=lab, zorder=4 if k == "mh_ekf" else 3)
    ax.plot(*d["truth"][0], "o", color=INK, ms=4, zorder=5)
    ax.set_xlim(ext[0], ext[1])
    ax.set_ylim(ext[2], ext[3])
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_xlabel("East of start (m)")
    ax.set_ylabel("North of start (m)")
    ax.set_title(info["title"], loc="left", fontsize=7.5)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), frameon=False, fontsize=6.5)
    save(fig, "fig_traj_example")


todo = sys.argv[1:] or ["cdf", "lost", "traj"]
for name in todo:
    {"cdf": fig_cdf, "lost": fig_lost, "traj": fig_traj}[name]()

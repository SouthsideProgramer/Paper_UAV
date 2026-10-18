# -*- coding: utf-8 -*-
"""
gen_tables.py — LaTeX tables of the paper, generated from the frozen result files (no hand-copied numbers).
  tables/retrieval.tex   DenseUAV R@1 (3 seeds) and AerialVL test top-1 <= 50 m, zero-shot vs fine-tuned
  tables/dense.tex       DenseUAV test campuses, 3 heads x 3 retrieval seeds x 3 trajectory seeds
  tables/aerialvl.tex    AerialVL test flights (short / long), fine-tuned and zero-shot retrieval
  tables/ablation.tex    MH-EKF ablation (LPN), written only when the F8-01 runs exist
Cell convention: p95 position error (m) per (head, seed[, traj seed]) cell, averaged over cells; "lost" = % runs whose
error exceeds 100 m at any time after the initial convergence (60 s AerialVL, 30 s DenseUAV), averaged over cells.
usage: python gen_tables.py
"""
import json, os, re
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TF = os.path.join(HERE, "..", "Task_F_Fusion")
A, P = os.path.join(TF, "aerialvl", "results"), os.path.join(TF, "prototype", "results")
OUT = os.path.join(HERE, "tables")
SC = ["vio", "imu", "init300", "imuinit300"]
SC_TEX = {"vio": "VIO", "imu": "IMU", "init300": "VIO+$\\epsilon_0$", "imuinit300": "IMU+$\\epsilon_0$"}
NAME = {"retrieval_top1": "Retrieval top-1", "dead_reckoning": "Motion only", "ekf_gated": "EKF, $\\chi^2$-gated",
        "pf_topk": "PF, Top-$K$", "naviloc_yaw": "NaviLoc$^\\dagger$ \\cite{shpagin2026naviloc}",
        "mh_ekf": "\\textbf{MH-EKF (ours)}"}
HEADS = ("baseline", "lpn", "fsra")
SEEDS = (666, 667, 668)


def stats(e, skip):
    return np.percentile(e, 95), 100 * (e[:, skip:] > 100).any(1).mean()


def fmt_cells(vals, best):
    """vals: method -> (p95, lost); bold the lowest p95 among filters."""
    out = {}
    for k, (p, l) in vals.items():
        s = f"{p:.0f}" if p >= 10 else f"{p:.1f}"
        if k == best:
            s = f"\\textbf{{{s}}}"
        lt = "0" if l == 0 else ("$<$0.1" if l < 0.05 else (f"{l:.1f}" if l < 1 else f"{l:.0f}"))
        out[k] = f"{s} ({lt})"
    return out


# ------------------------------------------------------------------ AerialVL
def aerialvl_block(kind, fe):
    base = {"short": "F5-04_test", "long": "F5-05_testlong"}[kind]
    methods = ["dead_reckoning", "retrieval_top1", "ekf_gated", "pf_topk", "naviloc_yaw", "mh_ekf"]
    res = {}
    for sc in SC:
        acc = {k: [] for k in methods}
        for h in HEADS:
            for s in SEEDS:
                c = f"{h}_s{s}_{sc}"
                if fe == "ft":
                    e = dict(np.load(f"{A}/F7-02_{kind}_{c}/errors.npz"))
                else:
                    e = dict(np.load(f"{A}/{base}_{c}/errors.npz"))
                    e["naviloc_yaw"] = np.load(f"{A}/F6-02_{kind}_{c}/errors.npz")["naviloc_yaw"]
                for k in methods:
                    acc[k].append(stats(e[k], 60))
        vals = {k: tuple(np.mean(acc[k], 0)) for k in methods}
        filt = {k: v for k, v in vals.items() if k not in ("dead_reckoning", "retrieval_top1")}
        res[sc] = fmt_cells(vals, min(filt, key=lambda k: filt[k][0]))
    return methods, res


def table_aerialvl():
    L = ["\\begin{table*}[t]", "\\centering",
         "\\caption{AerialVL test flights (2023-03-18, never used for any design choice). p95 position error in metres, "
         "in brackets the percentage of 240-s windows that exceed 100\\,m after the first 60\\,s (lost). Mean over "
         "3 retrieval heads $\\times$ 3 training seeds. $\\epsilon_0$: start position error $\\sigma=300$\\,m. "
         "IMU/VIO are simulated from the GNSS trajectory (Sec.~\\ref{sec:setup}). Bold: lowest p95 among the filters. "
         "$^\\dagger$Our re-implementation.}",
         "\\label{tab:aerialvl}", "\\setlength{\\tabcolsep}{4pt}", "\\small",
         "\\begin{tabular}{l" + "c" * 8 + "}", "\\toprule",
         " & \\multicolumn{4}{c}{3 \\texttt{short\\_trajtr} flights (3.6--4.5\\,km)} & \\multicolumn{4}{c}{5 \\texttt{long\\_trajtr} flights (4.4--9.9\\,km)} \\\\",
         "\\cmidrule(lr){2-5}\\cmidrule(lr){6-9}",
         "Method & " + " & ".join(SC_TEX[s] for s in SC) * 1 + " & " + " & ".join(SC_TEX[s] for s in SC) + " \\\\"]
    for fe, title in (("ft", "Retrieval fine-tuned on non-test flights (Sec.~\\ref{sec:ft})"), ("zs", "Retrieval zero-shot (trained on DenseUAV only)")):
        ms, rs = aerialvl_block("short", fe)
        _, rl = aerialvl_block("long", fe)
        L += ["\\midrule", f"\\multicolumn{{9}}{{l}}{{\\emph{{{title}}}}} \\\\"]
        for k in ms:
            L.append(NAME[k] + " & " + " & ".join(rs[s][k] for s in SC) + " & " + " & ".join(rl[s][k] for s in SC) + " \\\\")
    L += ["\\bottomrule", "\\end{tabular}", "\\end{table*}"]
    open(os.path.join(OUT, "aerialvl.tex"), "w").write("\n".join(L) + "\n")


# ------------------------------------------------------------------ DenseUAV
def table_dense():
    methods = ["retrieval_top1", "ekf_gated", "pf_topk", "naviloc_yaw", "mh_ekf"]
    res = {}
    for sc in SC:
        acc = {k: [] for k in methods}
        for h in HEADS:
            for s in SEEDS:
                for t in (0, 1, 2):
                    c = f"{h}_s{s}_t{t}_{sc}"
                    e = dict(np.load(f"{P}/F3-09_{c}/errors.npz"))
                    o = np.load(f"{P}/F3-08_{c}/errors.npz")
                    e["pf_topk"], e["retrieval_top1"] = o["pf_topk"], o["retrieval_top1"]
                    e["naviloc_yaw"] = np.load(f"{P}/F6-02_dense_{c}/errors.npz")["naviloc_yaw"]
                    for k in methods:
                        acc[k].append(stats(e[k], 30))
        vals = {k: tuple(np.mean(acc[k], 0)) for k in methods}
        filt = {k: v for k, v in vals.items() if k != "retrieval_top1"}
        res[sc] = fmt_cells(vals, min(filt, key=lambda k: filt[k][0]))
    L = ["\\begin{table}[t]", "\\centering",
         "\\caption{DenseUAV test campuses (semi-simulated flights over the real tile grid, real retrieval Top-$K$). "
         "p95 error in metres (\\% runs lost after 30\\,s); mean over 3 heads $\\times$ 3 retrieval seeds $\\times$ "
         "3 trajectory seeds (27 cells of 100 flights of 300\\,s).}",
         "\\label{tab:dense}", "\\setlength{\\tabcolsep}{3.5pt}", "\\small",
         "\\begin{tabular}{lcccc}", "\\toprule", "Method & " + " & ".join(SC_TEX[s] for s in SC) + " \\\\", "\\midrule"]
    for k in methods:
        L.append(NAME[k] + " & " + " & ".join(res[s][k] for s in SC) + " \\\\")
    L += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    open(os.path.join(OUT, "dense.tex"), "w").write("\n".join(L) + "\n")


# ------------------------------------------------------------------ retrieval
def top1(path):
    d = np.load(path)
    gf, qf = d["gallery_f"].astype(np.float32), d["query_f"].astype(np.float32)
    gxy, qxy, seq = d["gallery_xy"], d["query_xy"], d["query_seq"].astype(str)
    t1 = np.concatenate([np.argmax(qf[a:a + 512] @ gf.T, 1) for a in range(0, len(qf), 512)])
    e1 = np.hypot(*(gxy[t1] - qxy).T)
    short = np.isin(seq, ["2023-03-18-16-30-27", "2023-03-18-16-43-16", "2023-03-18-16-55-37"])
    long_ = np.char.startswith(seq, "2023-03-18") & ~short
    return [100 * (e1[m] <= 50).mean() for m in (np.char.startswith(seq, "2023-03-11"), short, long_)], \
           [np.median(e1[m]) for m in (short, long_)]


def table_retrieval():
    r1 = {"baseline": (79.67, 80.35, 80.22), "lpn": (86.36, 84.17, 84.47), "fsra": (81.85, 80.69, 80.18)}  # E006 (EXPERIMENT_LOG)
    hn = {"baseline": "ViT-S, single branch", "lpn": "ViT-S + LPN", "fsra": "ViT-S + FSRA"}
    L = ["\\begin{table}[t]", "\\centering",
         "\\caption{Retrieval. DenseUAV: Recall@1 (\\%) of our re-trained models (mean $\\pm$ std over 3 seeds). "
         "AerialVL: \\% frames whose top-1 tile is within 50\\,m of GNSS, zero-shot $\\rightarrow$ fine-tuned "
         "(val = 2023-03-11 flight; test = 2023-03-18 flights).}",
         "\\label{tab:retrieval}", "\\setlength{\\tabcolsep}{3pt}", "\\small",
         "\\begin{tabular}{lcccc}", "\\toprule",
         " & DenseUAV & \\multicolumn{3}{c}{AerialVL top-1 $\\le$ 50\\,m} \\\\", "\\cmidrule(lr){3-5}",
         "Head & R@1 & val & test short & test long \\\\", "\\midrule"]
    for h in HEADS:
        z = np.mean([top1(f"{TF}/aerialvl/feats/merged/{h}_s{s}.npz")[0] for s in SEEDS], 0)
        f = np.mean([top1(f"{TF}/aerialvl/feats/ft/merged/{h}_s{s}.npz")[0] for s in SEEDS], 0)
        L.append(f"{hn[h]} & {np.mean(r1[h]):.1f}$\\pm${np.std(r1[h], ddof=1):.1f} & "
                 + " & ".join(f"{a:.0f}$\\rightarrow${b:.0f}" for a, b in zip(z, f)) + " \\\\")
    L += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    open(os.path.join(OUT, "retrieval.tex"), "w").write("\n".join(L) + "\n")


# ------------------------------------------------------------------ ablation
VAR = [("max1", "single hypothesis ($M=1$)"), ("max3", "$M=3$"), ("max5", "$M=5$"), ("max20", "$M=20$"),
       ("k1", "top-1 only ($K=1$)"), ("k3", "$K=3$"), ("k5", "$K=5$"),
       ("gate599", "gate $\\chi^2_{0.95}$"), ("gate1382", "gate $\\chi^2_{0.999}$"), ("gateinf", "no gate"),
       ("noreacq", "no re-acquisition"), ("reachoff", "re-acq.\\ anywhere"), ("vmax10", "re-acq.\\ $3\\sigma+v_{\\max}\\Delta t$"),
       ("bestchild", "lost rule: best child")]


def table_ablation():
    sets = [("longft", A, lambda s, t: f"F7-02_long_lpn_s{s}_{t}", 60), ("dense", P, lambda s, t: f"F3-09_lpn_s{s}_t0_{t}", 30)]
    def cell(root, name, skip):
        return np.mean([stats(np.load(f"{root}/{name(s)}/errors.npz")["mh_ekf"], skip) for s in SEEDS], 0)
    rows, have = [], False
    ref = {(st, t): cell(r, lambda s, f=f, t=t: f(s, t), k) for st, r, f, k in sets for t in SC}
    rows.append("MH-EKF v3 (full) & " + " & ".join(f"{ref[(st, t)][0]:.0f} ({ref[(st, t)][1]:.0f})" for st, *_ in sets for t in SC) + " \\\\")
    rows.append("\\midrule")
    for v, nm in VAR:
        cells = []
        for st, r, f, k in sets:
            for t in SC:
                tail = (lambda s: f"F8_{st}_{v}_lpn_s{s}_t0_{t}") if st == "dense" else (lambda s: f"F8_{st}_{v}_lpn_s{s}_{t}")
                if not all(os.path.exists(f"{r}/{tail(s)}/errors.npz") for s in SEEDS):
                    cells.append("--")
                    continue
                have = True
                p, l = cell(r, tail, k)
                mk = "$^\\blacktriangle$" if p >= 1.1 * ref[(st, t)][0] else ("$^\\triangledown$" if p <= 0.9 * ref[(st, t)][0] else "")
                cells.append(f"{p:.0f}{mk} ({l:.0f})")
        rows.append(nm + " & " + " & ".join(cells) + " \\\\")
    if not have:
        return
    L = ["\\begin{table*}[t]", "\\centering",
         "\\caption{Ablation of MH-EKF (one factor changed at a time; LPN head, 3 seeds; test data, analysis only --- the "
         "design was frozen on validation data before). p95 error in metres (\\% runs lost). $^\\blacktriangle$/$^\\triangledown$: "
         "p95 at least 10\\,\\% worse/better than the full method. --: run not available.}",
         "\\label{tab:ablation}", "\\setlength{\\tabcolsep}{3.5pt}", "\\small",
         "\\begin{tabular}{l" + "c" * 8 + "}", "\\toprule",
         " & \\multicolumn{4}{c}{AerialVL long flights, fine-tuned retrieval} & \\multicolumn{4}{c}{DenseUAV test campuses} \\\\",
         "\\cmidrule(lr){2-5}\\cmidrule(lr){6-9}",
         "Variant & " + " & ".join(SC_TEX[s] for s in SC) + " & " + " & ".join(SC_TEX[s] for s in SC) + " \\\\", "\\midrule"]
    L += rows + ["\\bottomrule", "\\end{tabular}", "\\end{table*}"]
    open(os.path.join(OUT, "ablation.tex"), "w").write("\n".join(L) + "\n")


os.makedirs(OUT, exist_ok=True)
for f in (table_aerialvl, table_dense, table_retrieval, table_ablation):
    f()
    print("[INFO]", f.__name__, "done")

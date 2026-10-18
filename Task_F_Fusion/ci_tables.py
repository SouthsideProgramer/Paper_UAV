# -*- coding: utf-8 -*-
"""
ci_tables.py — F8-03: paired differences MH-EKF v3 − competitor with 95 % bootstrap CIs that resample whole
independent units: FLIGHTS on AerialVL (windows of a flight overlap), TRAJECTORIES on DenseUAV (a trajectory
= trajectory seed x run index, shared by the 3 retrieval seeds). The 3 retrieval training seeds of a head are
pooled; the same resampled units are used for every seed and both methods (paired).
Metrics: p95 error (m) and % runs lost (error > 100 m at any time after the first `skip` s).
usage: python ci_tables.py aerialvl_short_zs|aerialvl_long_zs|aerialvl_short_ft|aerialvl_long_ft|dense [n_boot]
"""
import json, sys
import numpy as np

ds = sys.argv[1]
n_boot = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
SC = ["vio", "imu", "init300", "imuinit300"]
REFS = ["dead_reckoning", "ekf_gated", "pf_topk", "naviloc_yaw"]
A, P = "aerialvl/results", "prototype/results"


def aerialvl_cells(kind, fe):
    base = {"short": "F5-04_test", "long": "F5-05_testlong"}[kind]
    for h in ("baseline", "lpn", "fsra"):
        for sc in SC:
            runs = []
            for s in (666, 667, 668):
                c = f"{h}_s{s}_{sc}"
                if fe == "ft":
                    f = f"{A}/F7-02_{kind}_{c}"
                    e = dict(np.load(f"{f}/errors.npz"))
                else:
                    f = f"{A}/{base}_{c}"
                    e = dict(np.load(f"{f}/errors.npz"))
                    e["naviloc_yaw"] = np.load(f"{A}/F6-02_{kind}_{c}/errors.npz")["naviloc_yaw"]
                meta = json.load(open(f"{f}/summary.json"))["meta"]
                runs.append((e, np.array([m[0] for m in meta])))
            yield h, sc, runs, 60


def dense_cells():
    for h in ("baseline", "lpn", "fsra"):
        for sc in SC:
            runs = []
            for s in (666, 667, 668):
                for t in (0, 1, 2):
                    c = f"{h}_s{s}_t{t}_{sc}"
                    e = {k: v for k, v in np.load(f"{P}/F3-09_{c}/errors.npz").items()}
                    e["pf_topk"] = np.load(f"{P}/F3-08_{c}/errors.npz")["pf_topk"]
                    e["naviloc_yaw"] = np.load(f"{P}/F6-02_dense_{c}/errors.npz")["naviloc_yaw"]
                    n = len(e["mh_ekf"])
                    runs.append((e, np.array([f"t{t}_{i}" for i in range(n)])))
            yield h, sc, runs, 30


def boot(runs, a, b, skip, rng):
    units = np.unique(np.concatenate([u for _, u in runs]))
    idx = {u: i for i, u in enumerate(units)}
    # per unit: stacked errors of a and b over all seeds
    ua = [[] for _ in units]
    ub = [[] for _ in units]
    for e, u in runs:
        for r, uu in enumerate(u):
            ua[idx[uu]].append(e[a][r])
            ub[idx[uu]].append(e[b][r])
    ua = [np.array(x) for x in ua]
    ub = [np.array(x) for x in ub]

    def stat(sel):
        Ea, Eb = np.concatenate([ua[i] for i in sel]), np.concatenate([ub[i] for i in sel])
        return (np.percentile(Ea, 95) - np.percentile(Eb, 95),
                100 * ((Ea[:, skip:] > 100).any(1).mean() - (Eb[:, skip:] > 100).any(1).mean()))

    d = stat(range(len(units)))
    bs = np.array([stat(rng.integers(0, len(units), len(units))) for _ in range(n_boot)])
    return d, np.percentile(bs, [2.5, 97.5], 0), len(units)


def fmt(d, ci):
    sig = "*" if ci[1] < 0 or ci[0] > 0 else ""
    return f"{d:+.0f} [{ci[0]:+.0f}, {ci[1]:+.0f}]{sig}"


if ds == "dense":
    cells = dense_cells()
else:
    _, kind, fe = ds.split("_")
    cells = aerialvl_cells(kind, fe)
rng = np.random.default_rng(0)
rows = []
for h, sc, runs, skip in cells:
    refs = [r for r in REFS if r in runs[0][0]]
    out = []
    for r in refs:
        d, ci, nu = boot(runs, "mh_ekf", r, skip, rng)
        out.append((r, d, ci))
    rows.append((h, sc, nu, out))
refs = [r for r, _, _ in rows[0][3]]
unit = "trajectories" if ds == "dense" else "flights"
print(f"## {ds}: MH-EKF v3 − X, 95 % CI bootstrap over {rows[0][2]} {unit} (3 retrieval seeds pooled, paired); * = CI excludes 0\n")
print("p95 difference (m)\n")
print("| Head | Scenario | " + " | ".join(f"− {r}" for r in refs) + " |\n|---|---|" + "---|" * len(refs))
for h, sc, nu, out in rows:
    print(f"| {h} | {sc} | " + " | ".join(fmt(d[0], ci[:, 0]) for _, d, ci in out) + " |")
print(f"\n% runs lost (> 100 m after the first {30 if ds == 'dense' else 60} s), difference in percentage points\n")
print("| Head | Scenario | " + " | ".join(f"− {r}" for r in refs) + " |\n|---|---|" + "---|" * len(refs))
for h, sc, nu, out in rows:
    print(f"| {h} | {sc} | " + " | ".join(fmt(d[1], ci[:, 1]) for _, d, ci in out) + " |")
n_sig = sum(ci[1, 0] < 0 for _, _, _, o in rows for _, _, ci in o)
n_worse = sum(ci[0, 0] > 0 for _, _, _, o in rows for _, _, ci in o)
print(f"\nSummary p95: MH-EKF significantly better in {n_sig}/{len(rows) * len(refs)} comparisons, significantly worse in {n_worse}.")

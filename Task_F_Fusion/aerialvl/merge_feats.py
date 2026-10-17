# -*- coding: utf-8 -*-
"""merge_feats.py — short-flight feature file + the per-flight long files -> one file (same gallery).
Query order: short flights first, then long flights in the order given (as feats/merged/ of F5-05).
usage: python merge_feats.py <short.npz> <out.npz> <long_1.npz> [<long_2.npz> ...]"""
import sys
import numpy as np

short, out, longs = sys.argv[1], sys.argv[2], sys.argv[3:]
a = dict(np.load(short))
for f in longs:
    b = np.load(f)
    assert np.array_equal(a["gallery_f"], b["gallery_f"]), f"gallery differs: {f}"
    for k in ("query_f", "query_xy", "query_t", "query_seq"):
        a[k] = np.concatenate([a[k], b[k]])
np.savez_compressed(out, **a)
print(f"[INFO] {out}: {len(a['query_f'])} queries")

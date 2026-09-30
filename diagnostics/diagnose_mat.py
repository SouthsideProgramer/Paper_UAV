# -*- coding: utf-8 -*-
"""
diagnose_mat.py — Giai đoạn 0: kiểm tra một (hoặc nhiều) file pytorch_result_*.mat.

Không cần torch. Kiểm tra:
  - feature có L2-normalize chưa
  - nhãn query/gallery có khớp (mọi query class có trong gallery)
  - path được sinh trên Windows hay Linux, test_dir nào
  - R@1 / R@5 tính lại trực tiếp, R@1 theo độ cao (H80/H90/H100)
  - dấu hiệu feature collapse (cosine trung bình giữa các query, top-1 dồn vào ít tile)

Ví dụ:
  python diagnostics/diagnose_mat.py Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat
  python diagnostics/diagnose_mat.py run_A.mat run_B.mat          # so sánh nhiều file
"""
import argparse
import hashlib
import json
import os
import re

import numpy as np
import scipy.io as sio


def sha256(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(chunk), b''):
            h.update(b)
    return h.hexdigest()


def altitude_of(path):
    m = re.search(r'H(80|90|100)', os.path.basename(path.replace('\\', '/')))
    return m.group(0) if m else '?'


def diagnose(path, max_rank=5):
    m = sio.loadmat(path)
    qf, gf = m['query_f'].astype(np.float32), m['gallery_f'].astype(np.float32)
    ql, gl = m['query_label'].ravel(), m['gallery_label'].ravel()
    qp = [str(p).strip() for p in m['query_path']]
    gp = [str(p).strip() for p in m['gallery_path']]

    qn, gn = np.linalg.norm(qf, axis=1), np.linalg.norm(gf, axis=1)
    score = qf @ gf.T
    order = np.argsort(-score, axis=1)[:, :max_rank]
    hit = gl[order] == ql[:, None]
    r1 = hit[:, 0]
    alt = np.array([altitude_of(p) for p in qp])

    top1 = order[:, 0]
    sub = qf[:min(500, len(qf))]
    return {
        'file': path,
        'sha256': sha256(path)[:16],
        'n_query': len(ql), 'n_gallery': len(gl),
        'n_query_class': int(len(np.unique(ql))), 'n_gallery_class': int(len(np.unique(gl))),
        'query_class_in_gallery': float(np.isin(ql, gl).mean()),
        'feat_dim': int(qf.shape[1]),
        'query_norm_min_max': [float(qn.min()), float(qn.max())],
        'gallery_norm_min_max': [float(gn.min()), float(gn.max())],
        'l2_normalized': bool(np.allclose(qn, 1, atol=1e-3) and np.allclose(gn, 1, atol=1e-3)),
        'path_style': 'windows' if '\\' in qp[0] else 'posix',
        'query_path_example': qp[0], 'gallery_path_example': gp[0],
        'R@1': float(r1.mean() * 100),
        'R@5': float(hit.any(axis=1).mean() * 100),
        'R@1_by_altitude': {a: float(r1[alt == a].mean() * 100) for a in sorted(set(alt))},
        'mean_cos_query_query': float((sub @ sub.T).mean()),
        'mean_top1_score': float(score[np.arange(len(ql)), top1].mean()),
        'max_queries_on_one_gallery_tile': int(np.bincount(top1).max()),
        'n_distinct_top1_tiles': int(len(np.unique(top1))),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mats', nargs='+', help='một hoặc nhiều file pytorch_result_*.mat')
    ap.add_argument('--json_out', default='', help='ghi kết quả ra file json')
    args = ap.parse_args()

    reports = [diagnose(p) for p in args.mats]
    for r in reports:
        print('=' * 70)
        for k, v in r.items():
            print(f'{k:34s} {v}')
        warn = []
        if not r['l2_normalized']:
            warn.append('feature CHƯA L2-normalize -> cosine sai')
        if r['query_class_in_gallery'] < 1:
            warn.append('có query class không có trong gallery -> lệch nhãn')
        if r['mean_cos_query_query'] > 0.8:
            warn.append('cosine giữa các query rất cao -> nghi feature collapse')
        for w in warn:
            print(f'[WARN] {w}')
    if len(reports) > 1:
        print('=' * 70)
        print(f'{"file":50s} {"R@1":>7s} {"R@5":>7s}')
        for r in reports:
            print(f'{os.path.basename(r["file"]):50s} {r["R@1"]:7.2f} {r["R@5"]:7.2f}')
    if args.json_out:
        with open(args.json_out, 'w') as f:
            json.dump(reports, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()

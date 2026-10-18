Config: `{"feats": "feats/merged/baseline_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1272.7 | 868.2 | 3744.3 | 4830.6 | 72.5 | 67.4 | 100.0 | [3631.8, 3833.3] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 39.9 | 29.1 | 107.0 | 296.1 | 13.7 | 5.3 | 0.0 | [76.8, 209.2] |
| pf_topk | 29.9 | 28.7 | 50.2 | 139.0 | 5.1 | 0.2 | 0.0 | [47.8, 53.7] |
| mh_ekf | 30.0 | 28.9 | 48.9 | 109.1 | 4.3 | 0.0 | 0.0 | [46.8, 51.4] |

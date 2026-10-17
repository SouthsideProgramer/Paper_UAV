Config: `{"feats": "feats/merged/baseline_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1272.7 | 868.2 | 3744.3 | 4830.6 | 72.5 | 67.4 | 100.0 | [3631.8, 3833.3] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 445.8 | 245.5 | 1506.0 | 2191.2 | 58.2 | 54.8 | 50.0 | [1222.4, 1538.0] |
| pf_topk | 187.6 | 42.8 | 755.2 | 1505.7 | 42.8 | 33.8 | 42.5 | [635.9, 1005.6] |
| mh_ekf | 85.4 | 31.2 | 508.1 | 2086.6 | 16.7 | 11.7 | 60.3 | [246.3, 580.8] |

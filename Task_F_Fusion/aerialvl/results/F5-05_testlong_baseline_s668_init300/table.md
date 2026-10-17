Config: `{"feats": "feats/merged/baseline_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1335.9 | 1038.9 | 3734.8 | 5512.3 | 75.1 | 70.9 | 100.0 | [3660.6, 3847.2] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 479.6 | 325.0 | 1338.1 | 2065.3 | 62.3 | 57.0 | 52.9 | [1262.5, 1552.6] |
| pf_topk | 231.0 | 42.4 | 963.0 | 1773.3 | 44.0 | 36.3 | 47.1 | [843.7, 1186.5] |
| mh_ekf | 129.1 | 30.9 | 922.4 | 2060.8 | 19.7 | 16.0 | 63.8 | [674.3, 1049.5] |

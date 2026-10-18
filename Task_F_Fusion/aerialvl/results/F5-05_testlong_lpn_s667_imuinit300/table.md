Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1305.7 | 1013.7 | 3682.1 | 4952.4 | 72.7 | 68.4 | 100.0 | [3555.6, 3808.4] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 536.7 | 73.7 | 2331.7 | 5826.9 | 56.1 | 47.1 | 52.3 | [1930.7, 2673.5] |
| pf_topk | 643.9 | 398.3 | 2074.9 | 6171.3 | 85.3 | 75.2 | 90.2 | [1870.6, 2253.5] |
| mh_ekf | 181.1 | 36.7 | 954.5 | 5516.5 | 34.7 | 23.1 | 62.1 | [808.5, 1195.6] |

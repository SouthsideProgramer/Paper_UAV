Config: `{"feats": "feats/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1255.8 | 875.4 | 3715.7 | 5121.4 | 70.7 | 65.9 | 100.0 | [3595.5, 3830.9] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 583.6 | 177.3 | 2259.9 | 7031.6 | 64.9 | 56.0 | 60.3 | [1915.8, 2570.3] |
| pf_topk | 656.0 | 405.9 | 2217.4 | 6669.0 | 84.2 | 74.1 | 87.9 | [1974.9, 2445.0] |
| mh_ekf | 191.2 | 35.5 | 1037.6 | 4367.6 | 34.0 | 22.6 | 59.8 | [793.8, 1313.4] |

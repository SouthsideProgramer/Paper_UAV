Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s667_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1170.8 | 586.5 | 3867.5 | 4758.2 | 64.9 | 59.4 | 100.0 | [3827.3, 3894.5] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 426.3 | 41.7 | 1778.6 | 6219.1 | 44.6 | 38.5 | 42.2 | [1462.3, 2080.0] |
| pf_topk | 562.1 | 299.6 | 2001.8 | 6306.4 | 78.5 | 67.5 | 83.0 | [1807.5, 2203.2] |
| mh_ekf | 83.2 | 30.0 | 157.4 | 7598.3 | 11.6 | 6.5 | 44.8 | [97.7, 253.0] |

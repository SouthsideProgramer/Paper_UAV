Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 586.2 | 42.9 | 3347.5 | 4928.9 | 43.8 | 32.3 | 100.0 | [3028.3, 3483.9] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 108.6 | 32.7 | 584.4 | 3086.0 | 26.3 | 12.4 | 14.4 | [297.3, 856.6] |
| pf_topk | 164.0 | 42.8 | 732.7 | 4836.7 | 43.9 | 27.6 | 33.3 | [569.2, 925.2] |
| mh_ekf | 79.6 | 30.9 | 280.5 | 2334.1 | 23.2 | 9.6 | 10.3 | [132.8, 591.5] |
| naviloc | 416.8 | 206.2 | 1575.4 | 3956.5 | 85.3 | 69.2 | 72.4 | [1262.6, 1780.8] |
| naviloc_yaw | 424.4 | 265.7 | 1399.3 | 3297.2 | 88.3 | 74.8 | 75.9 | [1226.8, 1528.3] |

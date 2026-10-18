Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 586.2 | 42.9 | 3347.5 | 4928.9 | 43.8 | 32.3 | 100.0 | [3028.3, 3483.9] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 239.1 | 36.8 | 1461.6 | 5392.2 | 35.5 | 22.4 | 27.0 | [966.0, 1794.2] |
| pf_topk | 505.5 | 230.1 | 1897.5 | 7225.2 | 76.4 | 62.0 | 77.6 | [1654.0, 2150.5] |
| mh_ekf | 91.5 | 32.3 | 385.7 | 3907.6 | 26.0 | 11.9 | 44.3 | [230.6, 561.9] |
| naviloc | 416.8 | 206.2 | 1575.4 | 3956.5 | 85.3 | 69.2 | 72.4 | [1262.6, 1780.8] |
| naviloc_yaw | 424.4 | 265.7 | 1399.3 | 3297.2 | 88.3 | 74.8 | 75.9 | [1226.8, 1528.3] |

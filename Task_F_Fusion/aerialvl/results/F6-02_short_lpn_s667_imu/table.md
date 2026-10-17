Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s667_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1724.4, 1939.0] |
| naviloc | 552.3 | 354.7 | 1625.1 | 3741.0 | 90.4 | 80.9 | 82.2 | [1542.2, 1753.7] |
| naviloc_yaw | 456.9 | 342.6 | 1252.4 | 3032.7 | 92.2 | 83.9 | 82.2 | [1177.4, 1341.2] |
| naviloc_causal | 571.3 | 285.5 | 1915.3 | 4247.7 | 80.9 | 71.8 | 95.7 | [1806.6, 2101.6] |

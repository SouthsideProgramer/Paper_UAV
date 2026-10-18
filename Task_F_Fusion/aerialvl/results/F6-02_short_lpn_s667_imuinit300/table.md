Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1822.3, 2057.3] |
| naviloc | 552.3 | 354.7 | 1625.1 | 3741.0 | 90.4 | 80.9 | 82.2 | [1542.2, 1753.7] |
| naviloc_yaw | 456.9 | 342.6 | 1252.4 | 3032.7 | 92.2 | 83.9 | 82.2 | [1177.4, 1341.2] |
| naviloc_causal | 574.3 | 291.8 | 1915.3 | 4247.7 | 81.7 | 72.6 | 97.0 | [1806.6, 2101.6] |

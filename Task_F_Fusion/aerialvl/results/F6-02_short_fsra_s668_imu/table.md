Config: `{"feats": "feats/fsra_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_fsra_s668_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1724.4, 1939.0] |
| naviloc | 668.4 | 524.2 | 1758.1 | 3435.4 | 92.7 | 85.9 | 90.4 | [1653.4, 1889.4] |
| naviloc_yaw | 577.2 | 462.0 | 1405.6 | 3163.8 | 95.3 | 89.8 | 88.3 | [1302.8, 1466.7] |
| naviloc_causal | 682.6 | 543.2 | 1855.4 | 3836.7 | 85.8 | 78.5 | 99.1 | [1768.4, 1968.5] |

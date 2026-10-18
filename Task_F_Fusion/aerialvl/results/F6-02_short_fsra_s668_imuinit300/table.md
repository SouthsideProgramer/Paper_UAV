Config: `{"feats": "feats/fsra_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_fsra_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1822.3, 2057.3] |
| naviloc | 668.4 | 524.2 | 1758.1 | 3435.4 | 92.7 | 85.9 | 90.4 | [1653.4, 1889.4] |
| naviloc_yaw | 577.2 | 462.0 | 1405.6 | 3163.8 | 95.3 | 89.8 | 88.3 | [1302.8, 1466.7] |
| naviloc_causal | 685.6 | 546.0 | 1855.4 | 3836.7 | 86.6 | 79.4 | 99.1 | [1768.4, 1968.5] |

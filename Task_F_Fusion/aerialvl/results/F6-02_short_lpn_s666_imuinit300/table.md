Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1822.3, 2057.3] |
| naviloc | 525.3 | 339.0 | 1599.0 | 3172.0 | 89.9 | 79.8 | 80.0 | [1461.8, 1710.2] |
| naviloc_yaw | 421.8 | 304.1 | 1185.5 | 2984.7 | 91.6 | 82.3 | 80.9 | [1117.5, 1254.4] |
| naviloc_causal | 473.3 | 249.8 | 1692.1 | 4053.3 | 81.1 | 69.9 | 95.2 | [1578.2, 1795.7] |

Config: `{"feats": "feats/fsra_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_fsra_s667_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1724.4, 1939.0] |
| naviloc | 681.9 | 528.8 | 1817.5 | 3832.9 | 93.2 | 86.3 | 88.7 | [1671.5, 1972.7] |
| naviloc_yaw | 577.3 | 483.8 | 1371.6 | 3490.9 | 94.9 | 89.2 | 87.8 | [1290.9, 1449.4] |
| naviloc_causal | 655.6 | 467.7 | 1847.7 | 4070.5 | 87.1 | 79.1 | 97.0 | [1786.9, 1929.1] |

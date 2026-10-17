Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s667_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1724.4, 1939.0] |
| naviloc | 496.9 | 301.7 | 1541.2 | 3540.5 | 88.5 | 76.7 | 79.1 | [1437.6, 1633.1] |
| naviloc_yaw | 418.3 | 295.4 | 1203.9 | 3277.3 | 90.0 | 80.3 | 80.4 | [1116.0, 1281.3] |
| naviloc_causal | 492.9 | 254.1 | 1875.3 | 3888.1 | 80.8 | 70.0 | 96.5 | [1771.2, 2031.1] |

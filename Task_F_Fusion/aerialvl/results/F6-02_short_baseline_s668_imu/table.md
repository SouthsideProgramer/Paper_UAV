Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s668_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1724.4, 1939.0] |
| naviloc | 622.3 | 492.0 | 1651.2 | 3649.1 | 93.3 | 86.1 | 91.3 | [1506.1, 1790.7] |
| naviloc_yaw | 517.1 | 424.8 | 1330.0 | 3453.7 | 95.4 | 89.6 | 89.1 | [1228.9, 1421.5] |
| naviloc_causal | 726.6 | 514.5 | 2392.4 | 3985.3 | 87.5 | 81.0 | 99.6 | [2289.1, 2457.7] |

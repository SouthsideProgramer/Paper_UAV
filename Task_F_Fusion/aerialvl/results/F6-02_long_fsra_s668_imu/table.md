Config: `{"feats": "feats/merged/fsra_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1588.4, 1892.3] |
| naviloc | 789.4 | 465.8 | 2697.3 | 5326.6 | 94.3 | 86.9 | 86.2 | [2340.2, 3041.3] |
| naviloc_yaw | 740.3 | 492.1 | 2359.2 | 4071.4 | 95.0 | 88.5 | 86.8 | [2070.7, 2695.9] |
| naviloc_causal | 808.9 | 438.4 | 2980.0 | 5337.5 | 86.7 | 79.2 | 97.1 | [2558.6, 3284.9] |

Config: `{"feats": "feats/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1588.4, 1892.3] |
| naviloc | 624.4 | 379.6 | 2064.0 | 4634.6 | 90.7 | 81.2 | 81.6 | [1902.3, 2343.8] |
| naviloc_yaw | 578.2 | 386.3 | 1943.2 | 3728.8 | 92.7 | 84.7 | 83.3 | [1643.0, 2084.9] |
| naviloc_causal | 670.3 | 358.2 | 2497.8 | 4681.5 | 84.3 | 75.2 | 96.0 | [2217.5, 2743.8] |

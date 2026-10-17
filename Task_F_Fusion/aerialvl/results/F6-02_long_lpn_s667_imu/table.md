Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s667_imu", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1588.4, 1892.3] |
| naviloc | 731.7 | 395.4 | 2495.8 | 5255.7 | 91.8 | 82.4 | 80.5 | [2298.0, 2767.5] |
| naviloc_yaw | 657.9 | 403.7 | 2125.7 | 3752.5 | 93.3 | 85.4 | 82.8 | [1926.0, 2300.8] |
| naviloc_causal | 724.9 | 390.6 | 2656.3 | 5254.8 | 84.8 | 76.5 | 95.4 | [2439.5, 2913.8] |

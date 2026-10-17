Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1714.7, 2048.8] |
| naviloc | 731.7 | 395.4 | 2495.8 | 5255.7 | 91.8 | 82.4 | 80.5 | [2298.0, 2767.5] |
| naviloc_yaw | 657.9 | 403.7 | 2125.7 | 3752.5 | 93.3 | 85.4 | 82.8 | [1926.0, 2300.8] |
| naviloc_causal | 728.0 | 396.0 | 2656.3 | 5254.8 | 85.7 | 77.3 | 96.6 | [2439.5, 2913.8] |

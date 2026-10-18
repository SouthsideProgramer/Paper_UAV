Config: `{"feats": "feats/merged/baseline_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 377.2 | 44.0 | 2204.9 | 3551.0 | 44.0 | 32.5 | 24.7 | [1945.5, 2519.5] |
| naviloc_yaw | 333.7 | 44.2 | 2059.6 | 2584.6 | 43.9 | 32.6 | 20.7 | [1831.9, 2233.1] |
| naviloc_causal | 505.1 | 53.1 | 2518.6 | 4257.6 | 52.3 | 41.9 | 84.5 | [2182.5, 2904.2] |

Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 434.7 | 38.8 | 2313.8 | 3523.6 | 38.4 | 29.6 | 27.6 | [2040.4, 2595.2] |
| naviloc_yaw | 379.5 | 39.0 | 2096.0 | 2296.6 | 38.6 | 29.9 | 23.0 | [1883.4, 2166.0] |
| naviloc_causal | 507.3 | 52.8 | 2518.1 | 4550.7 | 52.1 | 41.6 | 75.9 | [2261.6, 2760.7] |

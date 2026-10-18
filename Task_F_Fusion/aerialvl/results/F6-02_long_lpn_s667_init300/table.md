Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [682.7, 881.6] |
| naviloc | 434.7 | 38.8 | 2313.8 | 3523.6 | 38.4 | 29.6 | 27.6 | [2040.4, 2595.2] |
| naviloc_yaw | 379.5 | 39.0 | 2096.0 | 2296.6 | 38.6 | 29.9 | 23.0 | [1883.4, 2166.0] |
| naviloc_causal | 510.4 | 54.3 | 2518.1 | 4550.7 | 52.9 | 42.4 | 82.8 | [2261.6, 2760.7] |

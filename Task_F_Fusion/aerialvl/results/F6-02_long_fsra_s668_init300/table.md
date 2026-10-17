Config: `{"feats": "feats/merged/fsra_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [682.7, 881.6] |
| naviloc | 529.8 | 64.6 | 2369.1 | 3513.2 | 56.4 | 43.3 | 35.1 | [2060.7, 2763.2] |
| naviloc_yaw | 464.9 | 65.5 | 2440.6 | 3056.3 | 56.5 | 44.0 | 25.9 | [1823.5, 2753.8] |
| naviloc_causal | 626.2 | 102.4 | 2832.3 | 4157.5 | 61.7 | 50.2 | 90.8 | [2391.0, 3191.6] |

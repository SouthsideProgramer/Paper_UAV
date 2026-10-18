Config: `{"feats": "feats/merged/fsra_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 529.8 | 64.6 | 2369.1 | 3513.2 | 56.4 | 43.3 | 35.1 | [2060.7, 2763.2] |
| naviloc_yaw | 464.9 | 65.5 | 2440.6 | 3056.3 | 56.5 | 44.0 | 25.9 | [1823.5, 2753.8] |
| naviloc_causal | 623.1 | 94.3 | 2832.3 | 4157.5 | 60.9 | 49.4 | 87.9 | [2391.0, 3191.6] |

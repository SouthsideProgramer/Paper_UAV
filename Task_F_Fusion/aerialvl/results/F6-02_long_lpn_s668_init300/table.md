Config: `{"feats": "feats/merged/lpn_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [682.7, 881.6] |
| naviloc | 273.6 | 34.4 | 1866.2 | 3328.0 | 31.4 | 22.3 | 19.5 | [1154.3, 2148.6] |
| naviloc_yaw | 249.6 | 34.4 | 1799.4 | 2124.0 | 31.0 | 22.6 | 17.2 | [1363.7, 1961.0] |
| naviloc_causal | 430.6 | 46.8 | 2285.9 | 4381.6 | 47.4 | 36.5 | 87.4 | [1876.7, 2609.5] |

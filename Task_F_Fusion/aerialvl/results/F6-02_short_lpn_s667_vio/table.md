Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s667_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 74.3 | 28.2 | 346.3 | 1520.0 | 11.8 | 6.9 | 5.7 | [62.8, 706.7] |
| naviloc_yaw | 50.9 | 28.2 | 160.2 | 742.7 | 11.5 | 6.4 | 2.2 | [60.5, 328.7] |
| naviloc_causal | 247.6 | 37.2 | 1287.2 | 4246.5 | 37.3 | 27.2 | 67.4 | [1130.5, 1436.3] |

Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s667_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [692.6, 828.4] |
| naviloc | 74.3 | 28.2 | 346.3 | 1520.0 | 11.8 | 6.9 | 5.7 | [62.8, 706.7] |
| naviloc_yaw | 50.9 | 28.2 | 160.2 | 742.7 | 11.5 | 6.4 | 2.2 | [60.5, 328.7] |
| naviloc_causal | 250.6 | 37.7 | 1287.2 | 4246.5 | 38.1 | 28.0 | 75.7 | [1130.5, 1436.3] |

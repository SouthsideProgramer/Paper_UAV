Config: `{"feats": "feats/baseline_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s666_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [692.6, 828.4] |
| naviloc | 115.2 | 31.0 | 777.3 | 1524.9 | 25.8 | 15.8 | 11.3 | [336.4, 940.8] |
| naviloc_yaw | 71.8 | 31.1 | 289.4 | 940.2 | 26.0 | 14.9 | 2.2 | [229.4, 309.7] |
| naviloc_causal | 210.7 | 43.3 | 1044.2 | 3980.2 | 45.4 | 33.2 | 82.6 | [960.6, 1078.4] |

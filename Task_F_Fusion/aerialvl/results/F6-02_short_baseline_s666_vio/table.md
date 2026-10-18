Config: `{"feats": "feats/baseline_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s666_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 115.2 | 31.0 | 777.3 | 1524.9 | 25.8 | 15.8 | 11.3 | [336.4, 940.8] |
| naviloc_yaw | 71.8 | 31.1 | 289.4 | 940.2 | 26.0 | 14.9 | 2.2 | [229.4, 309.7] |
| naviloc_causal | 207.7 | 42.4 | 1044.2 | 3980.2 | 44.6 | 32.4 | 76.1 | [960.6, 1078.4] |

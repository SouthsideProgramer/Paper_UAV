Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W30_init300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 189.2 | 78.3 | 858.8 | 1641.1 | 64.5 | 43.7 | 15.4 | [403.1, 1153.9] |
| naviloc_yaw | 86.7 | 63.6 | 229.4 | 334.1 | 60.9 | 32.3 | 0.0 | [188.3, 263.4] |
| naviloc_causal | 387.0 | 114.7 | 1468.3 | 3048.1 | 60.8 | 50.7 | 84.6 | [1344.0, 1637.5] |
| mh_ekf | 134.9 | 48.2 | 561.9 | 1481.0 | 48.4 | 22.8 | 63.1 | [462.9, 757.8] |

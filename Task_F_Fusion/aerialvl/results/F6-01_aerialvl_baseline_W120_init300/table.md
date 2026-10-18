Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W120_init300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 183.0 | 70.6 | 865.2 | 1662.7 | 62.8 | 42.2 | 15.4 | [397.8, 1144.7] |
| naviloc_yaw | 82.3 | 56.6 | 258.9 | 291.6 | 56.7 | 28.7 | 0.0 | [194.1, 265.2] |
| naviloc_causal | 383.7 | 99.3 | 1464.2 | 3048.1 | 61.2 | 49.9 | 84.6 | [1347.7, 1644.4] |
| mh_ekf | 134.9 | 48.2 | 561.9 | 1481.0 | 48.4 | 22.8 | 63.1 | [462.9, 757.8] |

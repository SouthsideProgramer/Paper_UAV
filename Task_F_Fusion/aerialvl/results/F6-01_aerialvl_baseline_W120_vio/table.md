Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W120_vio", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 183.0 | 70.6 | 865.2 | 1662.7 | 62.8 | 42.2 | 15.4 | [397.8, 1144.7] |
| naviloc_yaw | 82.3 | 56.6 | 258.9 | 291.6 | 56.7 | 28.7 | 0.0 | [194.1, 265.2] |
| naviloc_causal | 380.6 | 89.1 | 1464.2 | 3048.1 | 60.4 | 49.1 | 76.9 | [1347.7, 1644.4] |
| mh_ekf | 39.2 | 31.7 | 94.4 | 150.3 | 30.8 | 3.0 | 0.0 | [89.3, 98.3] |

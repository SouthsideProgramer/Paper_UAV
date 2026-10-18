Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W30_imu", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 638.8 | 491.2 | 1703.9 | 4002.0 | 94.4 | 88.4 | 90.8 | [1426.9, 1929.2] |
| naviloc_yaw | 509.8 | 398.9 | 1360.9 | 4210.3 | 95.4 | 91.5 | 80.0 | [1115.2, 1532.8] |
| naviloc_causal | 687.4 | 507.2 | 1980.3 | 4002.1 | 86.9 | 79.7 | 96.9 | [1679.5, 2325.8] |
| mh_ekf | 120.2 | 41.5 | 400.0 | 2296.9 | 43.7 | 34.7 | 16.9 | [335.9, 524.8] |

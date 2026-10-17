Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W60_imuinit300", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 483.1 | 315.3 | 1502.6 | 3986.8 | 91.1 | 81.9 | 75.4 | [1138.4, 1779.5] |
| naviloc_yaw | 451.3 | 324.1 | 1353.5 | 2614.0 | 92.2 | 84.3 | 73.8 | [1103.2, 1464.6] |
| naviloc_causal | 628.5 | 360.5 | 2034.0 | 3877.2 | 86.6 | 76.7 | 96.9 | [1760.7, 2173.6] |
| mh_ekf | 389.1 | 132.1 | 1759.7 | 4122.7 | 66.0 | 56.4 | 72.3 | [1284.9, 2124.1] |

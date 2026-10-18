Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W60_imu", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 641.8 | 499.3 | 1729.1 | 4022.5 | 94.3 | 87.6 | 90.8 | [1445.0, 1969.1] |
| naviloc_yaw | 506.1 | 391.3 | 1358.4 | 3056.1 | 95.8 | 90.7 | 80.0 | [1122.4, 1536.4] |
| naviloc_causal | 691.7 | 510.7 | 2018.8 | 4035.3 | 86.8 | 79.6 | 96.9 | [1695.2, 2455.8] |
| mh_ekf | 120.2 | 41.5 | 400.0 | 2296.9 | 43.7 | 34.7 | 16.9 | [335.9, 524.8] |

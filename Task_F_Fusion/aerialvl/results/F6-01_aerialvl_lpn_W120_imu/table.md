Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W120_imu", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 645.5 | 497.3 | 1742.7 | 4000.1 | 94.5 | 87.9 | 90.8 | [1439.0, 2021.4] |
| naviloc_yaw | 510.8 | 392.1 | 1371.4 | 4193.5 | 95.5 | 90.1 | 83.1 | [1132.2, 1544.0] |
| naviloc_causal | 694.0 | 508.6 | 2023.5 | 4244.7 | 87.2 | 80.0 | 96.9 | [1703.8, 2490.0] |
| mh_ekf | 120.2 | 41.5 | 400.0 | 2296.9 | 43.7 | 34.7 | 16.9 | [335.9, 524.8] |

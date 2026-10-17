Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W120_imuinit300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 645.5 | 497.3 | 1742.7 | 4000.1 | 94.5 | 87.9 | 90.8 | [1439.0, 2021.4] |
| naviloc_yaw | 510.8 | 392.1 | 1371.4 | 4193.5 | 95.5 | 90.1 | 83.1 | [1132.2, 1544.0] |
| naviloc_causal | 697.1 | 512.3 | 2023.5 | 4244.7 | 88.0 | 80.8 | 98.5 | [1703.8, 2490.0] |
| mh_ekf | 449.2 | 115.4 | 1852.4 | 5133.2 | 58.3 | 51.7 | 70.8 | [1217.9, 2395.8] |

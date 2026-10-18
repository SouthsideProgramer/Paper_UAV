Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W120_init300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 392.9 | 259.1 | 1215.7 | 1673.6 | 77.0 | 70.8 | 53.8 | [1168.4, 1239.1] |
| naviloc_yaw | 201.9 | 213.2 | 475.1 | 520.3 | 79.7 | 75.1 | 1.5 | [351.8, 480.8] |
| naviloc_causal | 443.5 | 283.5 | 1350.4 | 3590.1 | 66.4 | 64.1 | 89.2 | [1296.3, 1419.2] |
| mh_ekf | 229.3 | 32.3 | 1194.1 | 1410.3 | 29.9 | 27.5 | 66.2 | [870.2, 1293.7] |

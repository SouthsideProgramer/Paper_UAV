Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W30_init300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 400.2 | 258.5 | 1210.0 | 1667.7 | 82.6 | 77.1 | 53.8 | [1165.0, 1235.7] |
| naviloc_yaw | 207.1 | 211.0 | 478.4 | 538.8 | 86.6 | 81.6 | 7.7 | [325.9, 480.6] |
| naviloc_causal | 446.7 | 292.5 | 1346.4 | 3590.1 | 67.2 | 64.8 | 89.2 | [1294.8, 1405.9] |
| mh_ekf | 229.3 | 32.3 | 1194.1 | 1410.3 | 29.9 | 27.5 | 66.2 | [870.2, 1293.7] |

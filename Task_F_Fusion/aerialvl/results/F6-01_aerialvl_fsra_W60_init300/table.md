Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W60_init300", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 368.7 | 243.0 | 1163.8 | 1673.2 | 81.4 | 75.0 | 52.3 | [1133.9, 1239.9] |
| naviloc_yaw | 169.0 | 161.0 | 351.5 | 419.9 | 83.0 | 75.7 | 0.0 | [296.8, 360.0] |
| naviloc_causal | 475.3 | 304.6 | 1358.5 | 3086.8 | 68.7 | 64.4 | 92.3 | [1271.1, 1588.6] |
| mh_ekf | 347.4 | 50.1 | 1161.7 | 1321.5 | 50.1 | 36.4 | 63.1 | [1047.1, 1302.0] |

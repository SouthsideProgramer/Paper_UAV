Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W120_init300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 361.0 | 242.6 | 1158.7 | 1680.4 | 77.4 | 69.6 | 50.8 | [1126.9, 1223.2] |
| naviloc_yaw | 160.4 | 154.2 | 350.6 | 454.4 | 77.3 | 68.0 | 0.0 | [299.9, 358.6] |
| naviloc_causal | 474.8 | 302.3 | 1361.6 | 3086.8 | 68.7 | 64.5 | 92.3 | [1270.0, 1586.2] |
| mh_ekf | 347.4 | 50.1 | 1161.7 | 1321.5 | 50.1 | 36.4 | 63.1 | [1047.1, 1302.0] |

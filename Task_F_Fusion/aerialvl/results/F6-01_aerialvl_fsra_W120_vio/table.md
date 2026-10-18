Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W120_vio", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 361.0 | 242.6 | 1158.7 | 1680.4 | 77.4 | 69.6 | 50.8 | [1126.9, 1223.2] |
| naviloc_yaw | 160.4 | 154.2 | 350.6 | 454.4 | 77.3 | 68.0 | 0.0 | [299.9, 358.6] |
| naviloc_causal | 471.7 | 298.1 | 1361.6 | 3086.8 | 67.9 | 63.6 | 84.6 | [1270.0, 1586.2] |
| mh_ekf | 32.6 | 22.8 | 88.3 | 168.9 | 17.9 | 2.4 | 0.0 | [84.2, 96.5] |

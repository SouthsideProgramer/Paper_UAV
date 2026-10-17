Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W30_init300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 369.3 | 242.9 | 1175.4 | 1674.0 | 84.1 | 76.5 | 50.8 | [1129.6, 1205.4] |
| naviloc_yaw | 171.3 | 161.9 | 351.9 | 402.1 | 87.2 | 78.5 | 0.0 | [302.3, 364.7] |
| naviloc_causal | 475.9 | 299.7 | 1354.8 | 3086.8 | 69.3 | 64.5 | 92.3 | [1273.2, 1587.1] |
| mh_ekf | 347.4 | 50.1 | 1161.7 | 1321.5 | 50.1 | 36.4 | 63.1 | [1047.1, 1302.0] |

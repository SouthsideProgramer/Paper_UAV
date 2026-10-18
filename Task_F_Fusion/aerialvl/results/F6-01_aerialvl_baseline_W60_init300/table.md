Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W60_init300", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 188.6 | 76.0 | 866.3 | 1640.4 | 61.5 | 43.3 | 15.4 | [419.3, 1160.7] |
| naviloc_yaw | 86.9 | 61.4 | 244.0 | 333.7 | 58.7 | 32.6 | 0.0 | [191.6, 263.5] |
| naviloc_causal | 386.3 | 111.7 | 1466.8 | 3048.1 | 60.5 | 50.4 | 86.2 | [1348.2, 1644.6] |
| mh_ekf | 134.9 | 48.2 | 561.9 | 1481.0 | 48.4 | 22.8 | 63.1 | [462.9, 757.8] |

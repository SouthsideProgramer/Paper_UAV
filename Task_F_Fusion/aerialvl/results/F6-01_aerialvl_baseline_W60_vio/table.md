Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W60_vio", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 188.6 | 76.0 | 866.3 | 1640.4 | 61.5 | 43.3 | 15.4 | [419.3, 1160.7] |
| naviloc_yaw | 86.9 | 61.4 | 244.0 | 333.7 | 58.7 | 32.6 | 0.0 | [191.6, 263.5] |
| naviloc_causal | 383.2 | 95.1 | 1466.8 | 3048.1 | 59.7 | 49.6 | 78.5 | [1348.2, 1644.6] |
| mh_ekf | 39.2 | 31.7 | 94.4 | 150.3 | 30.8 | 3.0 | 0.0 | [89.3, 98.3] |

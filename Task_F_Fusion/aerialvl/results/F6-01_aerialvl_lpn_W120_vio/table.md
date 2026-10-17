Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W120_vio", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 392.9 | 259.1 | 1215.7 | 1673.6 | 77.0 | 70.8 | 53.8 | [1168.4, 1239.1] |
| naviloc_yaw | 201.9 | 213.2 | 475.1 | 520.3 | 79.7 | 75.1 | 1.5 | [351.8, 480.8] |
| naviloc_causal | 440.4 | 279.7 | 1350.4 | 3590.1 | 65.5 | 63.2 | 84.6 | [1296.3, 1419.2] |
| mh_ekf | 23.9 | 21.5 | 45.5 | 109.0 | 2.5 | 0.2 | 0.0 | [43.2, 47.7] |

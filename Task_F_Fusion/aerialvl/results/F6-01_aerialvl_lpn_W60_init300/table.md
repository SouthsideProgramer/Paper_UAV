Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W60_init300", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 400.6 | 259.5 | 1214.7 | 1661.9 | 81.4 | 76.3 | 53.8 | [1170.8, 1248.7] |
| naviloc_yaw | 207.6 | 213.4 | 475.9 | 529.6 | 84.5 | 81.1 | 3.1 | [328.1, 480.5] |
| naviloc_causal | 446.1 | 278.9 | 1349.3 | 3590.1 | 66.7 | 64.5 | 89.2 | [1293.3, 1419.2] |
| mh_ekf | 229.3 | 32.3 | 1194.1 | 1410.3 | 29.9 | 27.5 | 66.2 | [870.2, 1293.7] |

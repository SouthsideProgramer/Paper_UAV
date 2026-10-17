Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_lpn_W60_vio", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 400.6 | 259.5 | 1214.7 | 1661.9 | 81.4 | 76.3 | 53.8 | [1170.8, 1248.7] |
| naviloc_yaw | 207.6 | 213.4 | 475.9 | 529.6 | 84.5 | 81.1 | 3.1 | [328.1, 480.5] |
| naviloc_causal | 443.0 | 275.6 | 1349.3 | 3590.1 | 65.9 | 63.7 | 84.6 | [1293.3, 1419.2] |
| mh_ekf | 23.9 | 21.5 | 45.5 | 109.0 | 2.5 | 0.2 | 0.0 | [43.2, 47.7] |

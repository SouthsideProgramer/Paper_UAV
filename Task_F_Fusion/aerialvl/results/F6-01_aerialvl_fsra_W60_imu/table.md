Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W60_imu", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 593.1 | 457.8 | 1579.7 | 3967.9 | 93.6 | 87.2 | 89.2 | [1303.1, 1852.9] |
| naviloc_yaw | 508.2 | 377.8 | 1430.5 | 3879.2 | 94.5 | 88.9 | 76.9 | [1188.9, 1581.8] |
| naviloc_causal | 662.7 | 467.6 | 1891.3 | 4120.1 | 86.4 | 78.0 | 96.9 | [1614.0, 2161.7] |
| mh_ekf | 161.5 | 56.6 | 499.2 | 4050.2 | 52.0 | 41.9 | 26.2 | [320.6, 973.0] |

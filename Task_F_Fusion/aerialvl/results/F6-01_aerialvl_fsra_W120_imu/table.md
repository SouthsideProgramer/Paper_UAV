Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W120_imu", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 598.7 | 466.7 | 1615.5 | 4141.8 | 93.8 | 87.3 | 89.2 | [1321.5, 1877.4] |
| naviloc_yaw | 505.9 | 377.1 | 1435.5 | 4008.1 | 94.9 | 88.3 | 75.4 | [1194.3, 1584.2] |
| naviloc_causal | 666.6 | 464.9 | 1893.4 | 4171.7 | 86.4 | 78.5 | 96.9 | [1615.7, 2169.1] |
| mh_ekf | 161.5 | 56.6 | 499.2 | 4050.2 | 52.0 | 41.9 | 26.2 | [320.6, 973.0] |

Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W30_imu", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 595.9 | 459.3 | 1589.7 | 3688.6 | 93.4 | 87.4 | 89.2 | [1319.8, 1867.9] |
| naviloc_yaw | 505.2 | 374.8 | 1410.0 | 3874.2 | 95.5 | 89.0 | 76.9 | [1148.7, 1578.7] |
| naviloc_causal | 658.4 | 462.5 | 1856.9 | 3690.4 | 86.3 | 77.8 | 96.9 | [1592.8, 2146.7] |
| mh_ekf | 161.5 | 56.6 | 499.2 | 4050.2 | 52.0 | 41.9 | 26.2 | [320.6, 973.0] |

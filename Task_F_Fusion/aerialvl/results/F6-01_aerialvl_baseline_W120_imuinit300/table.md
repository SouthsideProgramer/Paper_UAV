Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W120_imuinit300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 482.9 | 302.3 | 1524.0 | 4402.1 | 90.8 | 80.7 | 75.4 | [1158.7, 1788.5] |
| naviloc_yaw | 458.5 | 322.0 | 1391.5 | 4207.4 | 91.4 | 82.6 | 73.8 | [1142.6, 1518.7] |
| naviloc_causal | 631.3 | 355.0 | 2043.6 | 4407.4 | 86.8 | 77.1 | 96.9 | [1791.2, 2176.2] |
| mh_ekf | 389.1 | 132.1 | 1759.7 | 4122.7 | 66.0 | 56.4 | 72.3 | [1284.9, 2124.1] |

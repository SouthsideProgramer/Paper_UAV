Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W120_imu", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 482.9 | 302.3 | 1524.0 | 4402.1 | 90.8 | 80.7 | 75.4 | [1158.7, 1788.5] |
| naviloc_yaw | 458.5 | 322.0 | 1391.5 | 4207.4 | 91.4 | 82.6 | 73.8 | [1142.6, 1518.7] |
| naviloc_causal | 628.2 | 349.5 | 2043.6 | 4407.4 | 86.0 | 76.3 | 95.4 | [1791.2, 2176.2] |
| mh_ekf | 217.4 | 63.1 | 955.2 | 2725.4 | 56.3 | 43.7 | 36.9 | [708.7, 1215.0] |

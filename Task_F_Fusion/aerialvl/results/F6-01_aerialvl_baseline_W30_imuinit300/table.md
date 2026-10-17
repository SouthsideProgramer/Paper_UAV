Config: `{"feats": "feats/baseline_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_baseline_W30_imuinit300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 479.4 | 316.2 | 1508.4 | 3896.7 | 90.8 | 82.2 | 75.4 | [1135.5, 1768.5] |
| naviloc_yaw | 455.2 | 325.3 | 1363.9 | 2614.9 | 93.0 | 85.1 | 73.8 | [1100.1, 1468.2] |
| naviloc_causal | 626.1 | 357.3 | 2033.2 | 3898.0 | 86.1 | 76.8 | 96.9 | [1751.8, 2165.8] |
| mh_ekf | 389.1 | 132.1 | 1759.7 | 4122.7 | 66.0 | 56.4 | 72.3 | [1284.9, 2124.1] |

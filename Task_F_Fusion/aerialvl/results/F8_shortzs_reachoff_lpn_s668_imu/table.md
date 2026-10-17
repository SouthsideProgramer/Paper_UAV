Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_reachoff_lpn_s668_imu", "cfg": "{\"mh_reach\": false}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 147.1 | 28.0 | 1643.8 | 4885.9 | 10.5 | 6.6 | 48.3 | [98.2, 1674.6] |

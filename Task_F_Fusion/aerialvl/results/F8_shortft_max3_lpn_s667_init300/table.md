Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_max3_lpn_s667_init300", "cfg": "{\"mh_max\": 3}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 23.6 | 22.1 | 34.2 | 1025.3 | 0.8 | 0.4 | 27.4 | [33.6, 34.9] |

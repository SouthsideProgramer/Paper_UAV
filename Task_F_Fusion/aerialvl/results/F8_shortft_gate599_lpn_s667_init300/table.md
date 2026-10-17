Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_gate599_lpn_s667_init300", "cfg": "{\"mh_gate\": 5.99}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 24.2 | 22.1 | 34.0 | 1376.7 | 0.9 | 0.4 | 29.6 | [33.5, 34.6] |

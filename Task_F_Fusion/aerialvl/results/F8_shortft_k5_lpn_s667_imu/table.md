Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_k5_lpn_s667_imu", "cfg": "{\"mh_topk\": 5}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 29.9 | 25.8 | 46.7 | 1448.5 | 3.6 | 1.0 | 3.5 | [45.1, 48.6] |

Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_k1_lpn_s667_imu", "cfg": "{\"mh_topk\": 1}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 29.2 | 25.6 | 46.9 | 1089.1 | 3.6 | 0.9 | 2.6 | [45.1, 49.0] |

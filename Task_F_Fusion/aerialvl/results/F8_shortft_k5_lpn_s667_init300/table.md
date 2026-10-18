Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_k5_lpn_s667_init300", "cfg": "{\"mh_topk\": 5}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 25.0 | 21.7 | 34.8 | 1373.5 | 0.9 | 0.6 | 31.3 | [34.0, 35.7] |

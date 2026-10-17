Config: `{"feats": "feats/ft/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_k5_lpn_s668_vio", "cfg": "{\"mh_topk\": 5}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 25.5 | 25.6 | 38.6 | 49.9 | 0.0 | 0.0 | 0.0 | [37.6, 39.1] |

Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_max1_lpn_s666_init300", "cfg": "{\"mh_max\": 1}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 208.5 | 29.6 | 753.2 | 1025.3 | 31.7 | 31.5 | 28.3 | [695.8, 822.9] |

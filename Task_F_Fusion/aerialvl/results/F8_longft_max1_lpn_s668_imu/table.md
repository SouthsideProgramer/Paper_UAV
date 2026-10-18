Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_max1_lpn_s668_imu", "cfg": "{\"mh_max\": 1}", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 119.4 | 32.0 | 621.5 | 4517.9 | 26.2 | 13.4 | 16.1 | [388.2, 935.6] |

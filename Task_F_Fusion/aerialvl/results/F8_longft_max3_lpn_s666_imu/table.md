Config: `{"feats": "feats/ft/merged/lpn_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_max3_lpn_s666_imu", "cfg": "{\"mh_max\": 3}", "calib": "val", "calib_from": "feats/ft/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 67.4 | 31.8 | 185.3 | 2496.3 | 20.5 | 7.3 | 8.6 | [98.5, 362.5] |

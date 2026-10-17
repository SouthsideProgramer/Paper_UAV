Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_gateinf_lpn_s668_imu", "cfg": "{\"mh_gate\": 1e12}", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 75.6 | 30.1 | 139.0 | 3118.6 | 19.7 | 6.3 | 8.0 | [95.1, 334.2] |

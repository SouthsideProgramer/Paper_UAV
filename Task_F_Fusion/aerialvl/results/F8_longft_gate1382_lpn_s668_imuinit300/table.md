Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_gate1382_lpn_s668_imuinit300", "cfg": "{\"mh_gate\": 13.82}", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 144.2 | 32.6 | 828.7 | 6585.9 | 26.2 | 11.9 | 42.5 | [226.5, 1417.0] |

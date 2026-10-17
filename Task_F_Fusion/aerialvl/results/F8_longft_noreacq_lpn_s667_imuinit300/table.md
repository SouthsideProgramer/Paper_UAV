Config: `{"feats": "feats/ft/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_noreacq_lpn_s667_imuinit300", "cfg": "{\"n_reacq\": 1000000000}", "calib": "val", "calib_from": "feats/ft/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 90.4 | 28.4 | 334.6 | 5852.3 | 18.0 | 7.8 | 45.4 | [104.0, 593.3] |

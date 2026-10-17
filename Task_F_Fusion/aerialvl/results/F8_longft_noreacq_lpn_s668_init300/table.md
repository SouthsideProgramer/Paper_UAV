Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_noreacq_lpn_s668_init300", "cfg": "{\"n_reacq\": 1000000000}", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 55.3 | 27.5 | 69.9 | 1637.0 | 9.2 | 4.1 | 39.1 | [55.0, 314.0] |

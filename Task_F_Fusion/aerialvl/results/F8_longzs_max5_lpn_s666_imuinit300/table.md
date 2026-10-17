Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longzs_max5_lpn_s666_imuinit300", "cfg": "{\"mh_max\": 5}", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 277.1 | 43.3 | 1453.8 | 5754.7 | 44.2 | 32.3 | 63.2 | [1187.8, 1751.0] |

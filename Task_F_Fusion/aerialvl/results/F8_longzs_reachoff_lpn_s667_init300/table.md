Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longzs_reachoff_lpn_s667_init300", "cfg": "{\"mh_reach\": false}", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 380.5 | 30.6 | 2531.4 | 4876.0 | 23.8 | 21.4 | 87.9 | [2163.7, 2940.2] |

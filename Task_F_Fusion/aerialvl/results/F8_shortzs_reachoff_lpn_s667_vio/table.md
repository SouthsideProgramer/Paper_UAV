Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_reachoff_lpn_s667_vio", "cfg": "{\"mh_reach\": false}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 165.7 | 25.5 | 2149.2 | 3742.7 | 6.2 | 6.0 | 54.3 | [2144.6, 2155.4] |

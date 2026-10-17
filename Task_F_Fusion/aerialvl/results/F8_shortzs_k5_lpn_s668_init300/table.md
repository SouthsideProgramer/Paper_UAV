Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_k5_lpn_s668_init300", "cfg": "{\"mh_topk\": 5}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 42.7 | 25.4 | 40.0 | 1675.1 | 3.3 | 2.6 | 50.4 | [38.2, 42.7] |

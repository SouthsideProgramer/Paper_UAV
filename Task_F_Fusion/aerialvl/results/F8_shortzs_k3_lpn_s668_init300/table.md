Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_k3_lpn_s668_init300", "cfg": "{\"mh_topk\": 3}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 46.0 | 25.7 | 38.8 | 1820.9 | 3.8 | 3.2 | 52.2 | [37.2, 41.8] |

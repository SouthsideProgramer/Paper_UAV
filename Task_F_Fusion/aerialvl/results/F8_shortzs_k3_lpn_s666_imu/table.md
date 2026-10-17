Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_k3_lpn_s666_imu", "cfg": "{\"mh_topk\": 3}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 69.4 | 30.2 | 130.9 | 5683.0 | 12.6 | 5.9 | 7.4 | [88.2, 252.4] |

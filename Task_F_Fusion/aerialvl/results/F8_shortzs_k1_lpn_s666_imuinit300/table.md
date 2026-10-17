Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_k1_lpn_s666_imuinit300", "cfg": "{\"mh_topk\": 1}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 63.1 | 31.2 | 122.7 | 5513.7 | 14.2 | 5.9 | 46.5 | [93.1, 158.3] |

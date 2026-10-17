Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_noreacq_lpn_s666_imuinit300", "cfg": "{\"n_reacq\": 1000000000}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 80.3 | 30.5 | 206.8 | 6798.9 | 11.1 | 6.2 | 46.5 | [74.4, 431.7] |

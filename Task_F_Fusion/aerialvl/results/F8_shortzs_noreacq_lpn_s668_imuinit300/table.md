Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_noreacq_lpn_s668_imuinit300", "cfg": "{\"n_reacq\": 1000000000}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 56.3 | 28.0 | 69.3 | 5014.1 | 8.3 | 4.1 | 52.6 | [57.0, 149.6] |

Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_gate1382_lpn_s667_imuinit300", "cfg": "{\"mh_gate\": 13.82}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 68.4 | 30.1 | 128.5 | 5266.6 | 11.0 | 5.7 | 43.9 | [83.9, 235.0] |

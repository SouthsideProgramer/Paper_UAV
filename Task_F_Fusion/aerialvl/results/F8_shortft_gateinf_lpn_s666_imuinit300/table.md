Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_gateinf_lpn_s666_imuinit300", "cfg": "{\"mh_gate\": 1e12}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 107.9 | 30.4 | 388.1 | 7056.1 | 12.9 | 7.4 | 35.7 | [82.4, 873.1] |

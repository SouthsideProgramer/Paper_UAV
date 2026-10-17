Config: `{"feats": "feats/ft/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_gateinf_lpn_s668_init300", "cfg": "{\"mh_gate\": 1e12}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 47.2 | 26.2 | 43.0 | 1025.3 | 3.3 | 2.7 | 30.0 | [40.3, 52.1] |

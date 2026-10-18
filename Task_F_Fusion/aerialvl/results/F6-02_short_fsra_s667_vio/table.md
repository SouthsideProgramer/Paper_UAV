Config: `{"feats": "feats/fsra_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_fsra_s667_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 348.7 | 52.0 | 1328.0 | 2283.5 | 50.4 | 44.1 | 39.6 | [1278.8, 1375.4] |
| naviloc_yaw | 232.3 | 53.9 | 950.0 | 1117.5 | 50.7 | 44.8 | 21.7 | [882.1, 1028.7] |
| naviloc_causal | 417.4 | 92.5 | 1415.6 | 4067.3 | 57.1 | 49.1 | 76.5 | [1372.8, 1457.2] |

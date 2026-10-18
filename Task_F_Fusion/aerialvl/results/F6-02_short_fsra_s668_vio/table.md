Config: `{"feats": "feats/fsra_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_fsra_s668_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 323.7 | 38.2 | 1278.3 | 2500.5 | 45.0 | 37.4 | 34.3 | [1207.1, 1337.8] |
| naviloc_yaw | 203.2 | 38.8 | 1051.0 | 1225.6 | 45.4 | 37.1 | 12.2 | [1002.6, 1114.2] |
| naviloc_causal | 426.6 | 69.4 | 1452.9 | 3838.2 | 53.8 | 46.2 | 87.0 | [1395.0, 1529.1] |

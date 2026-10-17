Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s668_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 52.1 | 26.3 | 71.6 | 1292.2 | 8.2 | 4.5 | 3.0 | [52.7, 343.5] |
| naviloc_yaw | 35.2 | 26.1 | 66.6 | 463.6 | 7.8 | 4.3 | 0.0 | [51.0, 184.3] |
| naviloc_causal | 207.5 | 34.9 | 979.7 | 4400.4 | 34.3 | 26.1 | 78.3 | [910.0, 1026.0] |

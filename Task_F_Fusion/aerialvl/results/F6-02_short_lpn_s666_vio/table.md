Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s666_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 62.6 | 30.4 | 92.0 | 2596.5 | 13.3 | 4.3 | 3.0 | [73.9, 351.2] |
| naviloc_yaw | 37.3 | 30.5 | 85.4 | 254.6 | 13.0 | 3.0 | 0.0 | [69.7, 104.6] |
| naviloc_causal | 152.8 | 35.2 | 748.6 | 4052.4 | 30.2 | 20.2 | 62.6 | [691.8, 799.0] |

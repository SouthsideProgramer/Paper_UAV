Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s666_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [692.6, 828.4] |
| naviloc | 62.6 | 30.4 | 92.0 | 2596.5 | 13.3 | 4.3 | 3.0 | [73.9, 351.2] |
| naviloc_yaw | 37.3 | 30.5 | 85.4 | 254.6 | 13.0 | 3.0 | 0.0 | [69.7, 104.6] |
| naviloc_causal | 155.8 | 35.6 | 750.7 | 4052.4 | 31.0 | 21.0 | 72.2 | [697.1, 802.0] |

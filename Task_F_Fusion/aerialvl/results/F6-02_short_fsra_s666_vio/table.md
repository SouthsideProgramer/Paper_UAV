Config: `{"feats": "feats/fsra_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_fsra_s666_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 122.0 | 34.1 | 714.8 | 1825.8 | 30.1 | 20.2 | 12.2 | [454.1, 984.8] |
| naviloc_yaw | 80.6 | 34.1 | 450.2 | 685.9 | 29.9 | 17.7 | 4.3 | [265.2, 560.6] |
| naviloc_causal | 237.2 | 42.6 | 1028.9 | 4474.8 | 43.2 | 32.9 | 76.1 | [952.5, 1067.7] |

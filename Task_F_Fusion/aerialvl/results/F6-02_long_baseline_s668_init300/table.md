Config: `{"feats": "feats/merged/baseline_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [682.7, 881.6] |
| naviloc | 379.2 | 48.9 | 1644.7 | 3043.1 | 49.2 | 39.6 | 30.5 | [1522.4, 1919.7] |
| naviloc_yaw | 320.4 | 49.8 | 1584.5 | 2201.8 | 49.9 | 40.2 | 21.3 | [1369.2, 1672.1] |
| naviloc_causal | 551.2 | 84.3 | 2518.9 | 4947.2 | 59.4 | 48.6 | 90.2 | [2274.5, 2729.8] |

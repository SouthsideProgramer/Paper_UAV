Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1822.3, 2057.3] |
| naviloc | 622.3 | 492.0 | 1651.2 | 3649.1 | 93.3 | 86.1 | 91.3 | [1506.1, 1790.7] |
| naviloc_yaw | 517.1 | 424.8 | 1330.0 | 3453.7 | 95.4 | 89.6 | 89.1 | [1228.9, 1421.5] |
| naviloc_causal | 729.7 | 518.8 | 2392.4 | 3985.3 | 88.3 | 81.8 | 100.0 | [2289.1, 2457.7] |

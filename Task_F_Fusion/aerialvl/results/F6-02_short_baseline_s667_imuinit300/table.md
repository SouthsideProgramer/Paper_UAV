Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1822.3, 2057.3] |
| naviloc | 496.9 | 301.7 | 1541.2 | 3540.5 | 88.5 | 76.7 | 79.1 | [1437.6, 1633.1] |
| naviloc_yaw | 418.3 | 295.4 | 1203.9 | 3277.3 | 90.0 | 80.3 | 80.4 | [1116.0, 1281.3] |
| naviloc_causal | 496.0 | 258.7 | 1875.3 | 3888.1 | 81.6 | 70.8 | 97.4 | [1771.2, 2031.1] |

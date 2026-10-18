Config: `{"feats": "feats/fsra_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_fsra_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1822.3, 2057.3] |
| naviloc | 539.8 | 367.2 | 1572.6 | 4155.5 | 90.8 | 81.7 | 84.8 | [1458.0, 1651.4] |
| naviloc_yaw | 473.8 | 369.5 | 1280.1 | 3568.0 | 93.6 | 85.9 | 85.7 | [1185.5, 1362.1] |
| naviloc_causal | 537.1 | 310.4 | 1764.8 | 4474.9 | 83.6 | 73.5 | 97.4 | [1682.3, 1853.2] |

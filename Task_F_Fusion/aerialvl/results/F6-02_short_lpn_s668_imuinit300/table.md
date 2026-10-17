Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_lpn_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1822.3, 2057.3] |
| naviloc | 522.3 | 330.1 | 1577.2 | 4083.2 | 89.4 | 79.8 | 82.6 | [1461.2, 1684.3] |
| naviloc_yaw | 441.1 | 327.5 | 1223.5 | 3000.7 | 91.0 | 82.6 | 82.6 | [1151.9, 1300.3] |
| naviloc_causal | 526.7 | 294.4 | 1780.1 | 4401.2 | 81.9 | 72.3 | 97.0 | [1681.9, 1878.3] |

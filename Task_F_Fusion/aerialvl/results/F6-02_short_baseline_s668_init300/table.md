Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s668_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [692.6, 828.4] |
| naviloc | 300.9 | 80.7 | 1230.8 | 2292.4 | 55.6 | 46.6 | 37.0 | [1159.1, 1283.1] |
| naviloc_yaw | 152.1 | 79.3 | 508.8 | 603.4 | 56.0 | 45.3 | 9.1 | [471.9, 539.5] |
| naviloc_causal | 458.7 | 127.4 | 2266.0 | 3983.0 | 61.7 | 53.1 | 98.3 | [2036.3, 2369.5] |

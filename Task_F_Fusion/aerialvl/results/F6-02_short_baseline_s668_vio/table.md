Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s668_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 300.9 | 80.7 | 1230.8 | 2292.4 | 55.6 | 46.6 | 37.0 | [1159.1, 1283.1] |
| naviloc_yaw | 152.1 | 79.3 | 508.8 | 603.4 | 56.0 | 45.3 | 9.1 | [471.9, 539.5] |
| naviloc_causal | 455.7 | 118.6 | 2266.0 | 3983.0 | 60.8 | 52.3 | 97.8 | [2036.3, 2369.5] |

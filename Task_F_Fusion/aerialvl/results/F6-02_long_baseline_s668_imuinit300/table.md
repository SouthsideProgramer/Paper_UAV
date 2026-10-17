Config: `{"feats": "feats/merged/baseline_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1714.7, 2048.8] |
| naviloc | 678.6 | 442.6 | 2065.9 | 3886.0 | 93.7 | 86.4 | 87.4 | [1912.6, 2338.5] |
| naviloc_yaw | 613.6 | 437.2 | 1692.3 | 3607.0 | 95.1 | 88.0 | 85.1 | [1609.5, 1813.3] |
| naviloc_causal | 751.3 | 426.1 | 2608.3 | 4947.0 | 88.2 | 80.3 | 98.9 | [2469.5, 2830.5] |

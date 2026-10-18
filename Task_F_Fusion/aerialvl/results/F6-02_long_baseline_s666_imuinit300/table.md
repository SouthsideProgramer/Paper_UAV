Config: `{"feats": "feats/merged/baseline_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1714.7, 2048.8] |
| naviloc | 651.9 | 396.3 | 2012.0 | 3807.8 | 92.8 | 84.1 | 83.9 | [1857.9, 2246.2] |
| naviloc_yaw | 589.3 | 415.4 | 1687.6 | 3627.7 | 94.5 | 86.2 | 82.8 | [1554.6, 1858.4] |
| naviloc_causal | 667.5 | 373.1 | 2321.2 | 4554.5 | 85.3 | 76.4 | 96.0 | [2130.3, 2549.0] |

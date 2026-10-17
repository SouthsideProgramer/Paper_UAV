Config: `{"feats": "feats/merged/baseline_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s666_imu", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1588.4, 1892.3] |
| naviloc | 651.9 | 396.3 | 2012.0 | 3807.8 | 92.8 | 84.1 | 83.9 | [1857.9, 2246.2] |
| naviloc_yaw | 589.3 | 415.4 | 1687.6 | 3627.7 | 94.5 | 86.2 | 82.8 | [1554.6, 1858.4] |
| naviloc_causal | 664.4 | 366.9 | 2321.2 | 4554.5 | 84.5 | 75.6 | 95.4 | [2130.3, 2549.0] |

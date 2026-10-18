Config: `{"feats": "feats/merged/baseline_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 379.2 | 48.9 | 1644.7 | 3043.1 | 49.2 | 39.6 | 30.5 | [1522.4, 1919.7] |
| naviloc_yaw | 320.4 | 49.8 | 1584.5 | 2201.8 | 49.9 | 40.2 | 21.3 | [1369.2, 1672.1] |
| naviloc_causal | 548.1 | 77.9 | 2518.9 | 4947.2 | 58.6 | 47.8 | 86.8 | [2274.5, 2729.8] |

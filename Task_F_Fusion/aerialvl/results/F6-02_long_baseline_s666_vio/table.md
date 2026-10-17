Config: `{"feats": "feats/merged/baseline_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_baseline_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 388.3 | 44.7 | 1953.4 | 3358.9 | 45.3 | 36.5 | 28.2 | [1777.5, 2081.7] |
| naviloc_yaw | 293.2 | 44.7 | 1451.4 | 2005.7 | 45.6 | 37.3 | 21.8 | [1090.9, 1707.1] |
| naviloc_causal | 449.3 | 54.9 | 2112.4 | 4538.5 | 53.2 | 41.8 | 74.7 | [1932.4, 2298.7] |

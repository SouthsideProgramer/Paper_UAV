Config: `{"feats": "feats/baseline_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s666_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1724.4, 1939.0] |
| naviloc | 558.9 | 370.0 | 1621.8 | 3713.3 | 91.5 | 81.8 | 84.3 | [1511.1, 1726.2] |
| naviloc_yaw | 454.3 | 341.1 | 1212.9 | 3488.1 | 93.4 | 85.2 | 81.7 | [1150.2, 1275.5] |
| naviloc_causal | 507.5 | 284.9 | 1671.6 | 3981.3 | 83.6 | 73.2 | 97.0 | [1599.3, 1744.7] |

Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1714.7, 2048.8] |
| naviloc | 605.9 | 379.1 | 1938.8 | 3574.0 | 91.6 | 82.5 | 81.6 | [1773.7, 2089.6] |
| naviloc_yaw | 545.3 | 402.4 | 1549.0 | 3189.7 | 93.1 | 84.6 | 81.0 | [1431.7, 1618.5] |
| naviloc_causal | 640.8 | 335.4 | 2270.1 | 4922.1 | 84.3 | 74.4 | 96.6 | [2054.5, 2548.1] |

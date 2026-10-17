Config: `{"feats": "feats/merged/fsra_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1714.7, 2048.8] |
| naviloc | 679.2 | 410.4 | 2219.1 | 4719.6 | 92.5 | 83.4 | 83.9 | [2003.3, 2435.5] |
| naviloc_yaw | 599.7 | 423.8 | 1801.3 | 3550.0 | 93.8 | 85.4 | 83.9 | [1515.5, 2043.4] |
| naviloc_causal | 664.8 | 349.8 | 2432.8 | 4815.9 | 85.5 | 75.6 | 94.8 | [2147.4, 2705.1] |

Config: `{"feats": "feats/merged/fsra_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1714.7, 2048.8] |
| naviloc | 653.2 | 443.2 | 1853.0 | 3883.2 | 93.2 | 85.5 | 83.9 | [1705.0, 2083.4] |
| naviloc_yaw | 618.7 | 471.3 | 1583.8 | 3452.9 | 94.2 | 87.1 | 86.8 | [1457.9, 1720.6] |
| naviloc_causal | 693.0 | 399.5 | 2238.5 | 4238.2 | 85.8 | 77.4 | 97.1 | [2120.1, 2468.9] |

Config: `{"feats": "feats/merged/fsra_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [682.7, 881.6] |
| naviloc | 343.5 | 48.0 | 1477.8 | 2909.9 | 48.1 | 35.9 | 28.2 | [1401.7, 1619.4] |
| naviloc_yaw | 330.0 | 48.3 | 1369.6 | 1563.3 | 48.6 | 36.4 | 27.6 | [1266.2, 1440.8] |
| naviloc_causal | 472.4 | 64.5 | 1970.6 | 4235.3 | 57.4 | 44.1 | 87.4 | [1771.4, 2203.8] |

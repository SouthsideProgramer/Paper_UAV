Config: `{"feats": "feats/merged/fsra_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 343.5 | 48.0 | 1477.8 | 2909.9 | 48.1 | 35.9 | 28.2 | [1401.7, 1619.4] |
| naviloc_yaw | 330.0 | 48.3 | 1369.6 | 1563.3 | 48.6 | 36.4 | 27.6 | [1266.2, 1440.8] |
| naviloc_causal | 469.3 | 62.0 | 1970.6 | 4235.3 | 56.6 | 43.3 | 80.5 | [1771.4, 2203.8] |

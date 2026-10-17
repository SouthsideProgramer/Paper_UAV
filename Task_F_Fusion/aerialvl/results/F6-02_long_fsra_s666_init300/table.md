Config: `{"feats": "feats/merged/fsra_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [682.7, 881.6] |
| naviloc | 370.6 | 41.4 | 1842.7 | 3366.0 | 40.2 | 29.4 | 25.9 | [1551.9, 2302.5] |
| naviloc_yaw | 302.6 | 41.8 | 1397.1 | 2392.0 | 40.6 | 29.7 | 21.8 | [1154.5, 2012.4] |
| naviloc_causal | 446.7 | 53.9 | 2183.1 | 4172.4 | 53.3 | 38.9 | 84.5 | [1891.6, 2461.7] |

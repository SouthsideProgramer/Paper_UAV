Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [682.7, 881.6] |
| naviloc | 320.3 | 46.3 | 1611.2 | 2704.4 | 46.6 | 34.8 | 28.2 | [1381.3, 1779.6] |
| naviloc_yaw | 231.0 | 47.4 | 1182.7 | 1650.1 | 47.7 | 35.6 | 19.0 | [942.0, 1386.8] |
| naviloc_causal | 415.6 | 56.7 | 1990.3 | 4473.5 | 54.5 | 39.0 | 89.7 | [1786.6, 2212.8] |

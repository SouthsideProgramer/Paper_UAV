Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_lpn_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 320.3 | 46.3 | 1611.2 | 2704.4 | 46.6 | 34.8 | 28.2 | [1381.3, 1779.6] |
| naviloc_yaw | 231.0 | 47.4 | 1182.7 | 1650.1 | 47.7 | 35.6 | 19.0 | [942.0, 1386.8] |
| naviloc_causal | 412.5 | 55.3 | 1990.3 | 4473.5 | 53.7 | 38.2 | 82.2 | [1786.6, 2212.8] |

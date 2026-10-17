Config: `{"feats": "feats/merged/fsra_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_long_fsra_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 106.0] |
| naviloc | 370.6 | 41.4 | 1842.7 | 3366.0 | 40.2 | 29.4 | 25.9 | [1551.9, 2302.5] |
| naviloc_yaw | 302.6 | 41.8 | 1397.1 | 2392.0 | 40.6 | 29.7 | 21.8 | [1154.5, 2012.4] |
| naviloc_causal | 443.6 | 52.9 | 2183.1 | 4172.4 | 52.5 | 38.1 | 77.6 | [1891.6, 2461.7] |

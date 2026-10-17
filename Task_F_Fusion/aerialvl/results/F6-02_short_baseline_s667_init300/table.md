Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s667_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [692.6, 828.4] |
| naviloc | 30.4 | 28.3 | 53.2 | 131.6 | 6.1 | 1.0 | 0.0 | [47.5, 65.9] |
| naviloc_yaw | 30.3 | 28.3 | 51.9 | 130.5 | 5.7 | 1.0 | 0.0 | [47.3, 61.7] |
| naviloc_causal | 171.6 | 35.3 | 799.6 | 3050.5 | 31.3 | 22.4 | 80.0 | [728.7, 911.5] |

Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "dead_reckoning,naviloc,naviloc_yaw,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_short_baseline_s667_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.3, 119.4] |
| naviloc | 30.4 | 28.3 | 53.2 | 131.6 | 6.1 | 1.0 | 0.0 | [47.5, 65.9] |
| naviloc_yaw | 30.3 | 28.3 | 51.9 | 130.5 | 5.7 | 1.0 | 0.0 | [47.3, 61.7] |
| naviloc_causal | 168.6 | 34.8 | 796.3 | 3050.5 | 30.5 | 21.6 | 72.6 | [725.2, 908.5] |

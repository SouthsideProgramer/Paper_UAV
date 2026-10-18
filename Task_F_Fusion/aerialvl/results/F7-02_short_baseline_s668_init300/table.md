Config: `{"feats": "feats/ft/baseline_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s668_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 375.9 | 31.7 | 2584.7 | 4647.8 | 25.1 | 19.8 | 95.7 | [2525.3, 2679.8] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 79.6 | 24.3 | 633.6 | 1261.2 | 7.7 | 6.5 | 6.5 | [49.0, 893.2] |
| pf_topk | 50.6 | 25.1 | 61.4 | 1102.1 | 6.9 | 4.1 | 14.8 | [48.7, 483.9] |
| mh_ekf | 44.2 | 24.2 | 44.8 | 1245.3 | 3.9 | 3.2 | 33.9 | [40.0, 244.7] |
| naviloc | 23.4 | 23.7 | 37.0 | 88.7 | 0.5 | 0.0 | 0.0 | [36.1, 38.0] |
| naviloc_yaw | 23.3 | 23.6 | 36.7 | 73.8 | 0.4 | 0.0 | 0.0 | [35.9, 37.7] |

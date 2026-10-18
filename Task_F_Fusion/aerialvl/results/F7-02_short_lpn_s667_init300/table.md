Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s667_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 339.2 | 30.7 | 2377.5 | 4871.0 | 21.8 | 17.3 | 100.0 | [2334.0, 2421.6] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 39.9 | 22.2 | 36.6 | 958.1 | 2.9 | 2.3 | 4.8 | [34.2, 43.4] |
| pf_topk | 33.8 | 23.9 | 45.3 | 1348.1 | 3.7 | 1.3 | 8.7 | [41.7, 51.4] |
| mh_ekf | 24.4 | 22.1 | 34.1 | 1374.8 | 0.9 | 0.5 | 30.4 | [33.4, 34.7] |
| naviloc | 22.2 | 21.9 | 35.8 | 85.5 | 0.6 | 0.0 | 0.0 | [34.7, 37.0] |
| naviloc_yaw | 22.2 | 21.9 | 36.1 | 87.0 | 0.6 | 0.0 | 0.0 | [34.9, 37.2] |

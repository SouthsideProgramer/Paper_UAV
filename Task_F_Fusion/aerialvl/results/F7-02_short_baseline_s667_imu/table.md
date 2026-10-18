Config: `{"feats": "feats/ft/baseline_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s667_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 301.7 | 33.1 | 2130.2 | 5014.8 | 26.9 | 17.8 | 100.0 | [2085.1, 2359.4] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 44.8 | 27.5 | 73.8 | 2356.2 | 10.2 | 3.7 | 4.8 | [64.1, 103.2] |
| pf_topk | 139.7 | 35.3 | 723.3 | 3360.4 | 34.5 | 23.8 | 33.9 | [627.2, 822.7] |
| mh_ekf | 37.1 | 27.2 | 51.1 | 3244.5 | 5.5 | 2.0 | 4.8 | [48.5, 56.3] |
| naviloc | 355.8 | 200.2 | 1265.0 | 3659.9 | 81.5 | 67.6 | 73.9 | [1137.3, 1376.9] |
| naviloc_yaw | 367.4 | 253.9 | 1120.2 | 3167.9 | 85.0 | 73.1 | 77.8 | [1032.3, 1222.0] |

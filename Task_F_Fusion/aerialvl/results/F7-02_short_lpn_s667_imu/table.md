Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s667_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 339.2 | 30.7 | 2377.5 | 4871.0 | 21.8 | 17.3 | 100.0 | [2334.0, 2421.6] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 29.4 | 25.8 | 47.0 | 1428.4 | 3.5 | 0.8 | 2.6 | [45.5, 48.9] |
| pf_topk | 97.4 | 30.5 | 502.1 | 1982.6 | 27.8 | 17.1 | 26.5 | [416.3, 572.3] |
| mh_ekf | 29.2 | 25.4 | 45.7 | 1438.4 | 3.3 | 0.9 | 3.0 | [44.2, 47.9] |
| naviloc | 338.3 | 195.5 | 1130.8 | 3131.0 | 80.6 | 66.8 | 74.3 | [1046.7, 1218.6] |
| naviloc_yaw | 368.9 | 256.8 | 1102.8 | 3170.5 | 84.7 | 73.4 | 78.7 | [1030.7, 1197.9] |

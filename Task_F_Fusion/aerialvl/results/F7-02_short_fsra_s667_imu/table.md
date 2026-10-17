Config: `{"feats": "feats/ft/fsra_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s667_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 269.2 | 33.2 | 1750.7 | 4078.3 | 25.8 | 18.2 | 95.7 | [1617.9, 1931.8] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 44.6 | 26.0 | 67.5 | 5094.1 | 8.7 | 2.9 | 2.2 | [57.8, 83.2] |
| pf_topk | 101.5 | 31.0 | 502.2 | 2477.4 | 27.2 | 18.1 | 25.2 | [419.1, 603.0] |
| mh_ekf | 28.5 | 25.7 | 46.7 | 1278.1 | 3.5 | 0.6 | 0.9 | [45.4, 48.4] |
| naviloc | 345.2 | 199.5 | 1171.5 | 3117.9 | 81.4 | 67.6 | 75.7 | [1069.6, 1266.3] |
| naviloc_yaw | 368.9 | 255.8 | 1100.5 | 2993.1 | 84.4 | 73.1 | 79.1 | [1024.0, 1185.1] |

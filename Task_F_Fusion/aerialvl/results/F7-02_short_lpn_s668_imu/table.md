Config: `{"feats": "feats/ft/lpn_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s668_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 283.8 | 33.9 | 2183.6 | 4189.5 | 27.8 | 19.1 | 100.0 | [2099.5, 2224.7] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 34.1 | 28.3 | 55.8 | 1288.3 | 8.1 | 1.4 | 4.8 | [53.7, 58.0] |
| pf_topk | 117.7 | 34.8 | 604.3 | 2576.9 | 31.6 | 20.0 | 29.6 | [514.9, 699.1] |
| mh_ekf | 34.1 | 29.5 | 51.7 | 1262.3 | 5.9 | 1.3 | 3.9 | [49.7, 54.5] |
| naviloc | 356.4 | 208.7 | 1222.5 | 3518.7 | 82.5 | 68.8 | 74.3 | [1112.2, 1317.2] |
| naviloc_yaw | 367.8 | 256.4 | 1093.5 | 2967.2 | 86.0 | 74.4 | 77.4 | [1028.8, 1178.8] |

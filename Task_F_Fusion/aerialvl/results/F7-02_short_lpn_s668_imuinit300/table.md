Config: `{"feats": "feats/ft/lpn_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 283.8 | 33.9 | 2183.6 | 4189.5 | 27.8 | 19.1 | 100.0 | [2099.5, 2224.7] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 78.5 | 29.1 | 310.3 | 4582.6 | 13.0 | 6.1 | 9.1 | [75.0, 529.1] |
| pf_topk | 518.7 | 227.0 | 1931.5 | 6194.9 | 72.6 | 60.5 | 79.6 | [1773.6, 2153.5] |
| mh_ekf | 53.6 | 30.1 | 59.7 | 2806.8 | 8.1 | 3.4 | 32.2 | [53.0, 144.0] |
| naviloc | 356.4 | 208.7 | 1222.5 | 3518.7 | 82.5 | 68.8 | 74.3 | [1112.2, 1317.2] |
| naviloc_yaw | 367.8 | 256.4 | 1093.5 | 2967.2 | 86.0 | 74.4 | 77.4 | [1028.8, 1178.8] |

Config: `{"feats": "feats/ft/fsra_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 269.2 | 33.2 | 1750.7 | 4078.3 | 25.8 | 18.2 | 95.7 | [1617.9, 1931.8] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 81.1 | 26.7 | 133.3 | 5043.1 | 12.0 | 6.1 | 5.7 | [90.1, 785.5] |
| pf_topk | 484.7 | 216.1 | 1835.6 | 4674.1 | 72.3 | 60.3 | 81.3 | [1694.4, 2019.5] |
| mh_ekf | 34.3 | 26.2 | 48.5 | 1353.8 | 4.4 | 1.5 | 33.0 | [46.9, 51.0] |
| naviloc | 345.2 | 199.5 | 1171.5 | 3117.9 | 81.4 | 67.6 | 75.7 | [1069.6, 1266.3] |
| naviloc_yaw | 368.9 | 255.8 | 1100.5 | 2993.1 | 84.4 | 73.1 | 79.1 | [1024.0, 1185.1] |

Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 339.2 | 30.7 | 2377.5 | 4871.0 | 21.8 | 17.3 | 100.0 | [2334.0, 2421.6] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 44.1 | 26.4 | 52.5 | 3066.3 | 5.8 | 2.6 | 7.0 | [47.9, 64.6] |
| pf_topk | 488.3 | 200.9 | 1892.6 | 5934.1 | 70.2 | 58.6 | 80.9 | [1712.4, 2085.1] |
| mh_ekf | 31.5 | 25.8 | 47.6 | 1383.8 | 4.2 | 1.4 | 32.6 | [45.8, 50.2] |
| naviloc | 338.3 | 195.5 | 1130.8 | 3131.0 | 80.6 | 66.8 | 74.3 | [1046.7, 1218.6] |
| naviloc_yaw | 368.9 | 256.8 | 1102.8 | 3170.5 | 84.7 | 73.4 | 78.7 | [1030.7, 1197.9] |

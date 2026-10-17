Config: `{"feats": "feats/ft/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 522.4 | 38.2 | 2878.1 | 4589.3 | 39.9 | 29.6 | 100.0 | [2670.7, 2995.9] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 244.6 | 32.5 | 1484.8 | 4382.3 | 31.3 | 21.4 | 26.4 | [1082.3, 1716.7] |
| pf_topk | 486.6 | 182.8 | 1897.6 | 7200.7 | 72.5 | 58.3 | 75.3 | [1692.7, 2113.6] |
| mh_ekf | 94.1 | 28.4 | 334.5 | 5852.3 | 18.0 | 7.8 | 45.4 | [97.2, 674.2] |
| naviloc | 352.1 | 193.8 | 1256.6 | 3711.1 | 82.8 | 67.3 | 70.1 | [1086.9, 1379.6] |
| naviloc_yaw | 375.8 | 247.6 | 1194.8 | 2936.1 | 86.6 | 73.4 | 75.9 | [1084.2, 1269.3] |

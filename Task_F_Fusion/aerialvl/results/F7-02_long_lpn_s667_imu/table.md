Config: `{"feats": "feats/ft/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s667_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 522.4 | 38.2 | 2878.1 | 4589.3 | 39.9 | 29.6 | 100.0 | [2670.7, 2995.9] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 57.6 | 27.9 | 169.0 | 2240.8 | 18.4 | 7.7 | 6.9 | [110.2, 284.3] |
| pf_topk | 167.2 | 39.1 | 760.1 | 4695.7 | 40.7 | 25.6 | 33.3 | [544.3, 1028.2] |
| mh_ekf | 43.3 | 27.0 | 76.1 | 1970.5 | 13.7 | 3.6 | 4.6 | [63.6, 107.6] |
| naviloc | 352.1 | 193.8 | 1256.6 | 3711.1 | 82.8 | 67.3 | 70.1 | [1086.9, 1379.6] |
| naviloc_yaw | 375.8 | 247.6 | 1194.8 | 2936.1 | 86.6 | 73.4 | 75.9 | [1084.2, 1269.3] |

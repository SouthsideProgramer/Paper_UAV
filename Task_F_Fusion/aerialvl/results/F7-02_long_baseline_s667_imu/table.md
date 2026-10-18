Config: `{"feats": "feats/ft/merged/baseline_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s667_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 823.3 | 55.6 | 3515.5 | 5030.2 | 53.1 | 44.2 | 100.0 | [3382.8, 3646.6] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 86.0 | 34.4 | 376.3 | 2896.7 | 28.1 | 12.0 | 11.5 | [196.7, 532.1] |
| pf_topk | 182.1 | 45.9 | 843.1 | 6579.4 | 46.3 | 28.1 | 35.6 | [645.2, 1053.6] |
| mh_ekf | 70.1 | 33.4 | 225.3 | 2840.1 | 23.3 | 8.2 | 10.9 | [120.6, 422.2] |
| naviloc | 416.0 | 246.5 | 1407.7 | 3911.2 | 88.2 | 73.8 | 75.3 | [1206.3, 1577.9] |
| naviloc_yaw | 408.6 | 291.2 | 1225.7 | 3510.5 | 90.8 | 78.8 | 77.0 | [1089.8, 1347.9] |

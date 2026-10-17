Config: `{"feats": "feats/ft/merged/baseline_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 823.3 | 55.6 | 3515.5 | 5030.2 | 53.1 | 44.2 | 100.0 | [3382.8, 3646.6] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 334.0 | 43.9 | 1698.2 | 5785.4 | 44.2 | 30.3 | 33.9 | [1421.5, 1943.1] |
| pf_topk | 582.6 | 308.6 | 2025.7 | 6174.3 | 80.9 | 67.9 | 84.5 | [1802.2, 2291.8] |
| mh_ekf | 142.1 | 35.8 | 797.2 | 4438.1 | 29.3 | 14.4 | 51.7 | [474.7, 1119.3] |
| naviloc | 416.0 | 246.5 | 1407.7 | 3911.2 | 88.2 | 73.8 | 75.3 | [1206.3, 1577.9] |
| naviloc_yaw | 408.6 | 291.2 | 1225.7 | 3510.5 | 90.8 | 78.8 | 77.0 | [1089.8, 1347.9] |

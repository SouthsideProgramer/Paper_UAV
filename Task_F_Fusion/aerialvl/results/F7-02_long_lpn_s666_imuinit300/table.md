Config: `{"feats": "feats/ft/merged/lpn_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 620.7 | 43.3 | 3237.3 | 4979.8 | 44.0 | 33.7 | 98.3 | [3015.6, 3411.0] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 237.7 | 38.5 | 1398.2 | 6836.3 | 36.1 | 22.4 | 27.0 | [958.6, 1818.8] |
| pf_topk | 525.3 | 229.9 | 1915.8 | 7124.9 | 76.3 | 62.8 | 79.9 | [1657.6, 2206.3] |
| mh_ekf | 92.5 | 33.4 | 444.9 | 2579.3 | 25.2 | 12.3 | 48.3 | [277.3, 634.7] |
| naviloc | 342.0 | 200.1 | 1163.3 | 3579.6 | 84.4 | 68.8 | 73.0 | [1017.2, 1333.9] |
| naviloc_yaw | 385.2 | 252.8 | 1195.5 | 3366.5 | 87.9 | 74.8 | 78.7 | [1089.9, 1302.0] |

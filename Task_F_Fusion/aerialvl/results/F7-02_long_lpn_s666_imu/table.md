Config: `{"feats": "feats/ft/merged/lpn_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s666_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 620.7 | 43.3 | 3237.3 | 4979.8 | 44.0 | 33.7 | 98.3 | [3015.6, 3411.0] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 96.4 | 33.9 | 375.8 | 2880.9 | 26.8 | 11.9 | 10.3 | [184.6, 732.3] |
| pf_topk | 157.0 | 44.6 | 784.4 | 2423.4 | 44.8 | 27.5 | 36.8 | [620.4, 884.1] |
| mh_ekf | 62.0 | 31.6 | 183.0 | 2042.9 | 19.9 | 7.1 | 9.2 | [92.7, 303.5] |
| naviloc | 342.0 | 200.1 | 1163.3 | 3579.6 | 84.4 | 68.8 | 73.0 | [1017.2, 1333.9] |
| naviloc_yaw | 385.2 | 252.8 | 1195.5 | 3366.5 | 87.9 | 74.8 | 78.7 | [1089.9, 1302.0] |

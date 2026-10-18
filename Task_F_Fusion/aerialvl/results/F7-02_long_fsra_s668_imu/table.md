Config: `{"feats": "feats/ft/merged/fsra_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 678.2 | 44.6 | 3271.8 | 4945.4 | 46.1 | 38.0 | 100.0 | [3004.9, 3381.5] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 97.1 | 31.2 | 415.6 | 4461.0 | 23.4 | 10.8 | 12.6 | [209.6, 667.8] |
| pf_topk | 160.4 | 41.6 | 700.5 | 6654.4 | 42.2 | 26.6 | 33.9 | [534.6, 901.2] |
| mh_ekf | 72.2 | 29.8 | 170.8 | 3422.3 | 15.9 | 6.6 | 6.9 | [84.7, 401.3] |
| naviloc | 371.9 | 216.7 | 1277.9 | 4076.7 | 85.0 | 70.6 | 73.6 | [1100.7, 1514.6] |
| naviloc_yaw | 383.8 | 267.1 | 1177.2 | 3022.8 | 88.0 | 74.8 | 76.4 | [1069.3, 1254.3] |

Config: `{"feats": "feats/ft/merged/fsra_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 678.2 | 44.6 | 3271.8 | 4945.4 | 46.1 | 38.0 | 100.0 | [3004.9, 3381.5] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 265.6 | 33.6 | 1279.3 | 1775.0 | 31.4 | 28.2 | 28.2 | [1086.3, 1438.1] |
| pf_topk | 133.5 | 31.0 | 729.3 | 1499.7 | 23.4 | 17.6 | 25.3 | [574.7, 1070.4] |
| mh_ekf | 57.0 | 26.5 | 67.0 | 1730.5 | 7.9 | 4.0 | 46.0 | [54.7, 217.3] |
| naviloc | 55.9 | 27.7 | 153.4 | 1552.6 | 10.1 | 5.6 | 5.2 | [55.8, 430.9] |
| naviloc_yaw | 44.4 | 27.7 | 173.6 | 471.0 | 10.6 | 6.5 | 0.0 | [55.9, 339.2] |

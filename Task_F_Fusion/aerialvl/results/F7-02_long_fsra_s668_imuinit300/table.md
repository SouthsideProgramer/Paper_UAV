Config: `{"feats": "feats/ft/merged/fsra_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 678.2 | 44.6 | 3271.8 | 4945.4 | 46.1 | 38.0 | 100.0 | [3004.9, 3381.5] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 328.7 | 38.7 | 1683.3 | 6696.6 | 39.1 | 29.5 | 36.8 | [1430.3, 1960.8] |
| pf_topk | 523.8 | 264.8 | 1862.4 | 4710.6 | 77.6 | 64.9 | 80.5 | [1657.7, 2095.9] |
| mh_ekf | 94.7 | 31.0 | 425.2 | 3083.1 | 20.1 | 9.9 | 48.9 | [212.3, 710.1] |
| naviloc | 371.9 | 216.7 | 1277.9 | 4076.7 | 85.0 | 70.6 | 73.6 | [1100.7, 1514.6] |
| naviloc_yaw | 383.8 | 267.1 | 1177.2 | 3022.8 | 88.0 | 74.8 | 76.4 | [1069.3, 1254.3] |

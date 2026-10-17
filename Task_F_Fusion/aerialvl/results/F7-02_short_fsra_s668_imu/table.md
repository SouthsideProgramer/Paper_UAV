Config: `{"feats": "feats/ft/fsra_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s668_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 313.8 | 33.8 | 2148.1 | 4430.4 | 27.5 | 19.1 | 97.8 | [2104.1, 2342.0] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 81.8 | 29.7 | 260.4 | 4628.8 | 14.8 | 6.9 | 10.0 | [103.5, 541.4] |
| pf_topk | 161.8 | 35.2 | 779.5 | 5205.1 | 33.8 | 22.9 | 34.8 | [632.1, 969.3] |
| mh_ekf | 66.2 | 27.6 | 54.4 | 5385.9 | 6.1 | 3.3 | 5.2 | [48.4, 127.9] |
| naviloc | 344.5 | 200.1 | 1176.1 | 3248.2 | 81.9 | 67.6 | 74.8 | [1070.1, 1293.7] |
| naviloc_yaw | 370.6 | 262.3 | 1112.1 | 3063.9 | 85.0 | 73.8 | 78.7 | [1040.3, 1198.0] |

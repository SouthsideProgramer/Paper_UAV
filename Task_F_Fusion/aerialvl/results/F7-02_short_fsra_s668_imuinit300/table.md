Config: `{"feats": "feats/ft/fsra_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 313.8 | 33.8 | 2148.1 | 4430.4 | 27.5 | 19.1 | 97.8 | [2104.1, 2342.0] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 143.1 | 31.0 | 853.7 | 4639.1 | 21.1 | 13.6 | 19.6 | [631.3, 1120.3] |
| pf_topk | 507.7 | 228.8 | 1881.1 | 6364.2 | 73.5 | 61.7 | 81.7 | [1723.9, 2047.5] |
| mh_ekf | 64.9 | 28.2 | 63.3 | 5397.9 | 7.3 | 4.0 | 37.4 | [51.3, 154.5] |
| naviloc | 344.5 | 200.1 | 1176.1 | 3248.2 | 81.9 | 67.6 | 74.8 | [1070.1, 1293.7] |
| naviloc_yaw | 370.6 | 262.3 | 1112.1 | 3063.9 | 85.0 | 73.8 | 78.7 | [1040.3, 1198.0] |

Config: `{"feats": "feats/ft/baseline_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 301.7 | 33.1 | 2130.2 | 5014.8 | 26.9 | 17.8 | 100.0 | [2085.1, 2359.4] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 81.4 | 28.7 | 312.1 | 3372.5 | 14.9 | 7.9 | 11.7 | [115.8, 740.8] |
| pf_topk | 508.0 | 227.5 | 1893.9 | 6547.0 | 72.7 | 60.9 | 82.6 | [1724.6, 2096.3] |
| mh_ekf | 49.7 | 28.0 | 59.9 | 3395.4 | 7.7 | 3.5 | 35.2 | [53.0, 124.1] |
| naviloc | 355.8 | 200.2 | 1265.0 | 3659.9 | 81.5 | 67.6 | 73.9 | [1137.3, 1376.9] |
| naviloc_yaw | 367.4 | 253.9 | 1120.2 | 3167.9 | 85.0 | 73.1 | 77.8 | [1032.3, 1222.0] |

Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 289.0 | 32.7 | 2063.6 | 4573.9 | 24.4 | 17.9 | 97.8 | [1918.9, 2167.8] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 124.6 | 30.0 | 767.4 | 5287.8 | 15.0 | 8.0 | 10.4 | [107.2, 971.6] |
| pf_topk | 508.9 | 227.3 | 1870.7 | 5629.2 | 72.7 | 60.7 | 83.0 | [1692.7, 2070.0] |
| mh_ekf | 64.6 | 30.1 | 76.3 | 4984.3 | 10.1 | 4.5 | 35.2 | [58.4, 228.1] |
| naviloc | 329.4 | 199.2 | 1090.3 | 2885.4 | 81.1 | 66.8 | 75.2 | [994.5, 1175.4] |
| naviloc_yaw | 368.0 | 257.1 | 1112.0 | 3042.5 | 84.6 | 73.2 | 78.7 | [1025.2, 1192.8] |

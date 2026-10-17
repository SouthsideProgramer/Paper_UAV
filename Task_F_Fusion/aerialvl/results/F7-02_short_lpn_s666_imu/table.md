Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s666_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 289.0 | 32.7 | 2063.6 | 4573.9 | 24.4 | 17.9 | 97.8 | [1918.9, 2167.8] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 34.0 | 28.8 | 58.6 | 1106.0 | 8.9 | 1.5 | 2.6 | [55.5, 63.0] |
| pf_topk | 132.6 | 34.8 | 669.0 | 2770.3 | 33.4 | 22.6 | 32.2 | [555.5, 783.6] |
| mh_ekf | 34.3 | 29.4 | 55.2 | 1568.1 | 7.5 | 1.6 | 3.0 | [52.8, 59.3] |
| naviloc | 329.4 | 199.2 | 1090.3 | 2885.4 | 81.1 | 66.8 | 75.2 | [994.5, 1175.4] |
| naviloc_yaw | 368.0 | 257.1 | 1112.0 | 3042.5 | 84.6 | 73.2 | 78.7 | [1025.2, 1192.8] |

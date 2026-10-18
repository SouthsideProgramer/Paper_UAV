Config: `{"feats": "feats/ft/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s668_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 283.8 | 33.9 | 2183.6 | 4189.5 | 27.8 | 19.1 | 100.0 | [2099.5, 2224.7] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 77.4 | 26.8 | 441.3 | 1602.2 | 7.8 | 6.8 | 3.9 | [52.2, 680.8] |
| pf_topk | 51.7 | 26.7 | 65.2 | 978.5 | 7.1 | 4.7 | 10.0 | [49.6, 396.8] |
| mh_ekf | 47.1 | 26.2 | 42.8 | 1025.3 | 3.3 | 2.7 | 30.0 | [39.5, 53.9] |
| naviloc | 24.1 | 23.6 | 38.8 | 76.8 | 0.9 | 0.0 | 0.0 | [37.8, 39.9] |
| naviloc_yaw | 24.1 | 23.6 | 39.0 | 79.0 | 0.9 | 0.0 | 0.0 | [37.9, 40.0] |

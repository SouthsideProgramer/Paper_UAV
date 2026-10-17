Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s666_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 289.0 | 32.7 | 2063.6 | 4573.9 | 24.4 | 17.9 | 97.8 | [1918.9, 2167.8] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 85.8 | 26.2 | 794.5 | 1278.6 | 11.1 | 7.7 | 6.5 | [82.8, 894.5] |
| pf_topk | 47.0 | 25.8 | 76.4 | 1204.6 | 8.0 | 4.8 | 13.5 | [52.2, 231.0] |
| mh_ekf | 32.7 | 24.9 | 41.2 | 1188.3 | 2.4 | 1.8 | 33.0 | [39.9, 43.8] |
| naviloc | 23.7 | 23.6 | 38.0 | 83.6 | 0.5 | 0.0 | 0.0 | [37.4, 38.9] |
| naviloc_yaw | 23.6 | 23.4 | 38.1 | 70.6 | 0.5 | 0.0 | 0.0 | [37.4, 38.9] |

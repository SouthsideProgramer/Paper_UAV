Config: `{"feats": "feats/ft/fsra_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s668_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 313.8 | 33.8 | 2148.1 | 4430.4 | 27.5 | 19.1 | 97.8 | [2104.1, 2342.0] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 93.4 | 25.4 | 665.2 | 1249.5 | 10.9 | 9.7 | 10.4 | [621.7, 835.3] |
| pf_topk | 44.4 | 25.5 | 75.9 | 1100.7 | 8.7 | 4.3 | 13.5 | [55.2, 218.6] |
| mh_ekf | 30.1 | 23.7 | 38.7 | 1160.3 | 2.2 | 1.3 | 33.9 | [37.0, 40.6] |
| naviloc | 23.4 | 23.0 | 38.5 | 87.4 | 0.6 | 0.0 | 0.0 | [37.5, 39.6] |
| naviloc_yaw | 23.4 | 23.0 | 38.6 | 87.4 | 0.6 | 0.0 | 0.0 | [37.6, 39.6] |

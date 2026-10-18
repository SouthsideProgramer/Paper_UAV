Config: `{"feats": "feats/fsra_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s666_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1185.8 | 580.3 | 3917.6 | 5026.2 | 64.4 | 59.5 | 100.0 | [3887.6, 3925.3] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 191.9 | 33.6 | 871.0 | 1955.5 | 29.8 | 28.3 | 20.4 | [835.5, 1007.2] |
| pf_topk | 110.6 | 33.9 | 653.2 | 1794.3 | 21.6 | 15.0 | 27.0 | [537.6, 827.7] |
| mh_ekf | 53.0 | 29.8 | 50.2 | 1374.4 | 5.0 | 4.5 | 42.6 | [43.8, 432.0] |

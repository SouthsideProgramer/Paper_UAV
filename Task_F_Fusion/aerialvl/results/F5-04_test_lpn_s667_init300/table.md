Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s667_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1170.8 | 586.5 | 3867.5 | 4758.2 | 64.9 | 59.4 | 100.0 | [3827.3, 3894.5] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 321.9 | 35.1 | 1256.4 | 2020.9 | 38.9 | 36.0 | 37.4 | [1066.4, 1413.0] |
| pf_topk | 92.3 | 29.4 | 585.9 | 1408.5 | 20.3 | 15.6 | 25.2 | [330.4, 706.7] |
| mh_ekf | 38.5 | 25.1 | 41.0 | 1444.0 | 3.4 | 2.5 | 43.0 | [38.9, 44.9] |

Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s668_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1248.6 | 799.5 | 3638.2 | 4971.8 | 70.9 | 67.4 | 100.0 | [3613.0, 3648.6] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 350.4 | 38.4 | 1163.8 | 1649.4 | 45.3 | 42.4 | 46.5 | [1097.6, 1406.3] |
| pf_topk | 136.0 | 31.4 | 642.3 | 1453.6 | 27.1 | 23.4 | 34.8 | [611.7, 676.3] |
| mh_ekf | 53.1 | 25.8 | 159.1 | 1092.6 | 6.9 | 5.3 | 53.9 | [52.0, 540.1] |

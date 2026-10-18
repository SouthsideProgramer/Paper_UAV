Config: `{"feats": "feats/fsra_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s668_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1276.9 | 833.4 | 3830.5 | 4967.5 | 67.3 | 63.3 | 100.0 | [3790.9, 3875.5] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 97.5 | 27.9 | 343.9 | 5826.0 | 15.5 | 9.4 | 12.6 | [156.6, 740.8] |
| pf_topk | 122.2 | 33.5 | 575.5 | 4382.2 | 31.1 | 21.4 | 25.7 | [462.1, 690.9] |
| mh_ekf | 43.6 | 27.3 | 66.4 | 3598.3 | 8.1 | 3.1 | 3.5 | [55.9, 85.3] |

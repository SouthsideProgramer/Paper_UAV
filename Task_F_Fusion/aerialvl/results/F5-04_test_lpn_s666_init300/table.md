Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s666_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 989.0 | 233.4 | 3890.0 | 4860.8 | 61.8 | 56.3 | 100.0 | [3880.7, 3895.9] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 249.3 | 31.9 | 1087.0 | 1625.5 | 30.2 | 29.0 | 29.6 | [1036.5, 1210.7] |
| pf_topk | 90.0 | 31.2 | 573.4 | 1345.5 | 19.9 | 14.2 | 28.7 | [415.4, 620.7] |
| mh_ekf | 45.7 | 27.5 | 49.3 | 1492.1 | 4.8 | 3.5 | 44.3 | [43.1, 170.8] |

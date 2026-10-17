Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s666_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 989.0 | 233.4 | 3890.0 | 4860.8 | 61.8 | 56.3 | 100.0 | [3880.7, 3895.9] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 53.7 | 30.0 | 120.1 | 4102.5 | 14.6 | 5.9 | 7.0 | [85.8, 184.9] |
| pf_topk | 158.6 | 40.4 | 715.8 | 5730.8 | 40.4 | 27.4 | 37.4 | [622.0, 841.3] |
| mh_ekf | 60.1 | 29.7 | 57.6 | 6795.6 | 7.7 | 2.5 | 3.9 | [52.9, 69.2] |

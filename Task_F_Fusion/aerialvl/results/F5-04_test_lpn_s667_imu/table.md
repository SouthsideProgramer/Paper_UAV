Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s667_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1170.8 | 586.5 | 3867.5 | 4758.2 | 64.9 | 59.4 | 100.0 | [3827.3, 3894.5] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 73.0 | 30.9 | 174.0 | 4021.7 | 15.6 | 8.0 | 8.7 | [118.9, 354.2] |
| pf_topk | 146.2 | 36.9 | 660.5 | 7480.2 | 36.9 | 26.0 | 33.5 | [547.9, 808.1] |
| mh_ekf | 76.9 | 29.6 | 79.8 | 7581.9 | 8.9 | 4.1 | 3.0 | [60.0, 131.6] |

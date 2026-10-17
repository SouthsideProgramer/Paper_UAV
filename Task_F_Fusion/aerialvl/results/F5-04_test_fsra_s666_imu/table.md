Config: `{"feats": "feats/fsra_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s666_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1185.8 | 580.3 | 3917.6 | 5026.2 | 64.4 | 59.5 | 100.0 | [3887.6, 3925.3] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 207.4 | 34.1 | 1069.2 | 5365.4 | 29.5 | 22.1 | 28.3 | [809.6, 1401.3] |
| pf_topk | 135.7 | 39.8 | 669.3 | 3036.1 | 37.2 | 23.6 | 31.7 | [567.2, 776.1] |
| mh_ekf | 33.9 | 31.2 | 51.4 | 614.3 | 5.7 | 1.3 | 1.7 | [49.6, 53.6] |

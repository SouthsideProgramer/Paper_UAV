Config: `{"feats": "feats/fsra_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s667_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1257.6 | 823.9 | 3925.5 | 5003.3 | 66.3 | 62.8 | 100.0 | [3852.5, 3964.0] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 92.0 | 30.6 | 356.0 | 5502.5 | 17.2 | 9.5 | 10.9 | [262.1, 608.9] |
| pf_topk | 114.3 | 34.4 | 527.4 | 6516.1 | 29.8 | 19.0 | 23.0 | [416.1, 656.5] |
| mh_ekf | 31.9 | 29.0 | 50.7 | 571.4 | 5.2 | 1.3 | 0.4 | [48.3, 53.6] |

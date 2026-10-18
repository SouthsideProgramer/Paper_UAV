Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s668_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1085.1 | 573.5 | 3837.9 | 4996.5 | 62.9 | 57.5 | 100.0 | [3813.3, 3851.5] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 189.4 | 30.2 | 1053.4 | 6069.3 | 25.2 | 18.3 | 23.5 | [671.1, 1557.2] |
| pf_topk | 114.2 | 32.7 | 576.2 | 3007.5 | 30.4 | 19.4 | 26.5 | [464.7, 684.4] |
| mh_ekf | 41.8 | 27.5 | 55.7 | 5218.7 | 6.6 | 2.4 | 4.8 | [50.1, 71.6] |

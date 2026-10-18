Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s668_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1085.1 | 573.5 | 3837.9 | 4996.5 | 62.9 | 57.5 | 100.0 | [3813.3, 3851.5] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 229.6 | 28.5 | 1238.0 | 1820.8 | 25.7 | 23.7 | 29.1 | [1103.6, 1438.6] |
| pf_topk | 100.4 | 29.4 | 692.6 | 1418.8 | 15.2 | 11.1 | 30.4 | [408.3, 1082.6] |
| mh_ekf | 40.9 | 25.2 | 39.6 | 1616.5 | 3.1 | 2.5 | 50.0 | [38.2, 41.7] |

Config: `{"feats": "feats/merged/fsra_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s667_imu", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1350.9 | 1040.5 | 3839.4 | 4997.8 | 72.7 | 68.1 | 100.0 | [3703.7, 3926.7] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 217.0 | 42.0 | 1186.7 | 6404.1 | 42.4 | 26.3 | 29.3 | [842.0, 1557.0] |
| pf_topk | 234.1 | 55.2 | 1085.0 | 5511.8 | 53.3 | 36.6 | 39.7 | [845.8, 1343.1] |
| mh_ekf | 94.2 | 34.3 | 331.5 | 2861.5 | 25.9 | 12.7 | 11.5 | [200.1, 621.1] |

Config: `{"feats": "feats/merged/baseline_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s667_imu", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1291.5 | 861.6 | 3815.4 | 5190.1 | 71.5 | 66.1 | 100.0 | [3735.4, 3911.5] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 232.9 | 43.0 | 1342.3 | 3604.8 | 43.4 | 28.0 | 29.9 | [954.3, 1653.3] |
| pf_topk | 215.8 | 44.6 | 1134.6 | 5129.3 | 46.0 | 30.8 | 34.5 | [816.0, 1394.4] |
| mh_ekf | 150.4 | 34.4 | 697.4 | 6717.2 | 28.7 | 16.4 | 14.9 | [342.8, 1157.2] |

Config: `{"feats": "feats/merged/fsra_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1404.1 | 1108.8 | 3821.6 | 5511.3 | 75.7 | 71.1 | 100.0 | [3700.6, 3878.0] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 233.2 | 41.7 | 1252.1 | 5365.7 | 43.6 | 28.9 | 32.8 | [930.5, 1590.0] |
| pf_topk | 207.9 | 55.8 | 923.8 | 4433.3 | 53.5 | 36.3 | 42.5 | [771.1, 1100.9] |
| mh_ekf | 84.9 | 31.4 | 394.9 | 2339.7 | 24.1 | 12.7 | 13.8 | [231.2, 561.1] |

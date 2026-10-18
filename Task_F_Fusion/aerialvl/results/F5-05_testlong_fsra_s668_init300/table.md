Config: `{"feats": "feats/merged/fsra_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1404.1 | 1108.8 | 3821.6 | 5511.3 | 75.7 | 71.1 | 100.0 | [3700.6, 3878.0] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 442.9 | 88.6 | 1480.6 | 2138.4 | 55.2 | 49.1 | 48.9 | [1373.1, 1620.2] |
| pf_topk | 194.3 | 40.0 | 770.4 | 1710.4 | 42.7 | 36.3 | 40.8 | [656.0, 984.0] |
| mh_ekf | 101.2 | 28.5 | 576.2 | 2088.3 | 19.2 | 14.8 | 60.3 | [465.2, 665.3] |

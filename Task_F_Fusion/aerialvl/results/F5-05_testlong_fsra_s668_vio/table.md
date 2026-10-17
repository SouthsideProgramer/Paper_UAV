Config: `{"feats": "feats/merged/fsra_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1404.1 | 1108.8 | 3821.6 | 5511.3 | 75.7 | 71.1 | 100.0 | [3700.6, 3878.0] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 38.1 | 27.3 | 115.5 | 238.8 | 13.7 | 6.6 | 0.0 | [102.7, 178.5] |
| pf_topk | 29.6 | 26.4 | 59.2 | 184.5 | 6.7 | 2.0 | 0.0 | [48.3, 87.6] |
| mh_ekf | 29.1 | 26.0 | 53.2 | 200.8 | 5.7 | 1.5 | 0.0 | [46.8, 78.6] |

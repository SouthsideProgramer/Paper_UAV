Config: `{"feats": "feats/merged/fsra_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1404.1 | 1108.8 | 3821.6 | 5511.3 | 75.7 | 71.1 | 100.0 | [3700.6, 3878.0] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 678.3 | 244.4 | 2456.7 | 7286.6 | 67.9 | 58.4 | 63.8 | [2135.4, 2825.8] |
| pf_topk | 636.8 | 373.0 | 2181.8 | 5962.2 | 84.7 | 75.3 | 89.7 | [1954.5, 2403.9] |
| mh_ekf | 189.6 | 35.9 | 1032.4 | 4124.7 | 35.0 | 24.2 | 66.7 | [805.6, 1263.2] |

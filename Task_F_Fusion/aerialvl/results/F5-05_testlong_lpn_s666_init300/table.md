Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1244.3 | 829.2 | 3650.1 | 5108.1 | 72.1 | 66.8 | 100.0 | [3519.3, 3800.2] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 376.1 | 55.7 | 1492.3 | 2110.9 | 52.2 | 45.4 | 43.7 | [1277.7, 1587.5] |
| pf_topk | 181.8 | 41.2 | 709.8 | 1855.2 | 41.9 | 32.2 | 41.4 | [607.9, 1138.3] |
| mh_ekf | 91.8 | 31.3 | 535.2 | 2060.4 | 16.0 | 12.1 | 58.6 | [216.5, 934.5] |

Config: `{"feats": "feats/merged/fsra_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1350.9 | 1040.5 | 3839.4 | 4997.8 | 72.7 | 68.1 | 100.0 | [3703.7, 3926.7] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 415.3 | 67.4 | 1352.7 | 2233.4 | 54.3 | 47.3 | 46.0 | [1244.3, 1481.6] |
| pf_topk | 210.9 | 42.4 | 923.3 | 1562.1 | 44.0 | 34.9 | 43.1 | [812.7, 1130.4] |
| mh_ekf | 99.7 | 32.5 | 566.5 | 2114.8 | 18.9 | 12.5 | 56.9 | [321.5, 919.4] |

Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1305.7 | 1013.7 | 3682.1 | 4952.4 | 72.7 | 68.4 | 100.0 | [3555.6, 3808.4] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 389.8 | 47.9 | 1396.6 | 2223.8 | 49.2 | 43.7 | 39.1 | [1229.9, 1611.9] |
| pf_topk | 218.7 | 39.4 | 977.3 | 1769.5 | 42.0 | 35.5 | 38.5 | [861.3, 1314.3] |
| mh_ekf | 100.6 | 30.1 | 535.2 | 2056.7 | 18.3 | 14.2 | 57.5 | [388.5, 771.8] |

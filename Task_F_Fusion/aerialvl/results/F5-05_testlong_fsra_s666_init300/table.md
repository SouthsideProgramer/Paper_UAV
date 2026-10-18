Config: `{"feats": "feats/merged/fsra_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1309.6 | 950.1 | 3771.8 | 5046.0 | 73.6 | 68.7 | 100.0 | [3640.9, 3894.3] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 321.2 | 46.6 | 1181.1 | 2072.4 | 47.7 | 42.7 | 35.6 | [956.2, 1567.4] |
| pf_topk | 175.9 | 39.6 | 851.9 | 1582.9 | 40.4 | 30.9 | 42.5 | [618.2, 996.2] |
| mh_ekf | 99.8 | 31.7 | 512.2 | 2053.4 | 18.4 | 14.1 | 55.2 | [467.2, 639.5] |

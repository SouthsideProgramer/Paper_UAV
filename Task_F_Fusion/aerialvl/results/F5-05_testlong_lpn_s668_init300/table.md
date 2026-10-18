Config: `{"feats": "feats/merged/lpn_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1255.8 | 875.4 | 3715.7 | 5121.4 | 70.7 | 65.9 | 100.0 | [3595.5, 3830.9] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 372.9 | 49.7 | 1302.3 | 2063.4 | 49.9 | 44.6 | 47.1 | [1167.6, 1422.9] |
| pf_topk | 201.2 | 39.1 | 883.1 | 1569.3 | 40.8 | 33.0 | 41.4 | [692.6, 970.5] |
| mh_ekf | 94.3 | 27.9 | 601.4 | 1648.1 | 14.3 | 11.3 | 54.0 | [395.5, 703.3] |

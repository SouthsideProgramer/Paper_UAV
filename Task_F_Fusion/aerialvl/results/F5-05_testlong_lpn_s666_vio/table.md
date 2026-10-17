Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1244.3 | 829.2 | 3650.1 | 5108.1 | 72.1 | 66.8 | 100.0 | [3519.3, 3800.2] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 34.8 | 28.2 | 73.0 | 243.1 | 11.6 | 3.5 | 0.0 | [62.1, 94.7] |
| pf_topk | 30.2 | 28.2 | 50.7 | 220.2 | 5.4 | 1.2 | 0.0 | [47.5, 55.5] |
| mh_ekf | 30.5 | 29.0 | 49.5 | 215.0 | 4.7 | 0.8 | 0.0 | [47.7, 51.5] |

Config: `{"feats": "feats/fsra_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s667_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1257.6 | 823.9 | 3925.5 | 5003.3 | 66.3 | 62.8 | 100.0 | [3852.5, 3964.0] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 357.2 | 38.0 | 1814.8 | 6052.0 | 38.5 | 32.0 | 33.5 | [1497.5, 2151.3] |
| pf_topk | 584.6 | 296.7 | 2155.9 | 6582.3 | 79.6 | 68.2 | 83.9 | [1931.6, 2402.2] |
| mh_ekf | 99.6 | 30.5 | 480.3 | 5248.6 | 14.4 | 10.2 | 44.3 | [244.9, 720.1] |

Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s666_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 989.0 | 233.4 | 3890.0 | 4860.8 | 61.8 | 56.3 | 100.0 | [3880.7, 3895.9] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 329.0 | 37.9 | 1612.1 | 5077.2 | 37.5 | 30.2 | 35.7 | [1330.4, 1838.4] |
| pf_topk | 572.6 | 309.8 | 2083.6 | 6340.3 | 78.9 | 67.7 | 87.8 | [1879.2, 2275.4] |
| mh_ekf | 78.7 | 30.5 | 207.3 | 6798.9 | 11.1 | 6.3 | 46.5 | [75.2, 442.1] |

Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s668_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1085.1 | 573.5 | 3837.9 | 4996.5 | 62.9 | 57.5 | 100.0 | [3813.3, 3851.5] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 389.6 | 35.2 | 2133.6 | 6049.9 | 38.3 | 32.2 | 40.9 | [1618.2, 2522.3] |
| pf_topk | 556.2 | 286.1 | 2069.3 | 6338.9 | 76.3 | 65.6 | 86.1 | [1843.0, 2294.1] |
| mh_ekf | 56.0 | 28.0 | 67.8 | 5014.1 | 8.2 | 4.0 | 52.6 | [58.1, 137.3] |

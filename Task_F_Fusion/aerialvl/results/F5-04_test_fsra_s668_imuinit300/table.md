Config: `{"feats": "feats/fsra_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s668_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1276.9 | 833.4 | 3830.5 | 4967.5 | 67.3 | 63.3 | 100.0 | [3790.9, 3875.5] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 458.3 | 35.7 | 2338.9 | 7901.5 | 40.9 | 34.6 | 43.0 | [1943.2, 2704.7] |
| pf_topk | 597.3 | 312.5 | 2181.7 | 7013.5 | 77.0 | 66.5 | 85.2 | [1988.2, 2384.3] |
| mh_ekf | 105.6 | 28.6 | 555.5 | 4447.9 | 15.3 | 10.2 | 54.3 | [393.7, 845.2] |

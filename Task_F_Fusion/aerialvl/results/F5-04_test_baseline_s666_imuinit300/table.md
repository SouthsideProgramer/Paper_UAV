Config: `{"feats": "feats/baseline_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s666_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1044.3 | 280.1 | 3820.5 | 4801.1 | 62.2 | 56.3 | 100.0 | [3800.5, 3828.6] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 250.7 | 34.2 | 1430.7 | 5499.6 | 29.8 | 23.0 | 23.0 | [1152.6, 1785.8] |
| pf_topk | 573.8 | 292.3 | 2084.5 | 6094.9 | 77.9 | 65.9 | 83.9 | [1877.1, 2288.3] |
| mh_ekf | 106.8 | 32.8 | 482.7 | 5939.8 | 16.1 | 11.9 | 50.4 | [311.6, 607.6] |

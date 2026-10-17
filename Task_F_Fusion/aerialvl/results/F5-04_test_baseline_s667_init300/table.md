Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s667_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1022.2 | 126.7 | 3778.2 | 5025.9 | 59.0 | 52.4 | 100.0 | [3707.1, 3810.2] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 136.5 | 30.8 | 1062.1 | 1433.2 | 18.0 | 14.0 | 19.6 | [715.3, 1089.8] |
| pf_topk | 73.4 | 31.1 | 541.9 | 1061.4 | 15.7 | 8.8 | 25.2 | [123.5, 620.5] |
| mh_ekf | 37.7 | 28.0 | 48.2 | 1444.0 | 4.3 | 1.9 | 42.2 | [46.2, 50.2] |

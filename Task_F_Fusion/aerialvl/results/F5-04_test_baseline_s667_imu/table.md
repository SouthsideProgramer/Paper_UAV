Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s667_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1022.2 | 126.7 | 3778.2 | 5025.9 | 59.0 | 52.4 | 100.0 | [3707.1, 3810.2] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 76.6 | 32.8 | 188.9 | 4810.5 | 18.2 | 9.3 | 7.8 | [130.6, 354.0] |
| pf_topk | 190.2 | 41.8 | 884.2 | 6230.0 | 42.8 | 29.2 | 36.5 | [706.3, 1086.6] |
| mh_ekf | 40.4 | 31.1 | 61.3 | 2813.9 | 9.0 | 2.4 | 3.9 | [56.1, 72.5] |

Config: `{"feats": "feats/baseline_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s666_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1044.3 | 280.1 | 3820.5 | 4801.1 | 62.2 | 56.3 | 100.0 | [3800.5, 3828.6] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 89.3 | 32.0 | 328.6 | 5401.4 | 21.0 | 14.2 | 12.2 | [196.1, 510.6] |
| pf_topk | 115.1 | 36.8 | 544.4 | 2565.3 | 33.3 | 20.7 | 25.7 | [449.0, 655.4] |
| mh_ekf | 40.0 | 31.7 | 95.4 | 1239.2 | 9.4 | 4.8 | 2.2 | [61.2, 120.8] |

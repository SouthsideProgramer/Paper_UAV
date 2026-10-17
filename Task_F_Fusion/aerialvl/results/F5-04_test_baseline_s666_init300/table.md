Config: `{"feats": "feats/baseline_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s666_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1044.3 | 280.1 | 3820.5 | 4801.1 | 62.2 | 56.3 | 100.0 | [3800.5, 3828.6] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 140.9 | 30.5 | 885.3 | 2006.5 | 22.7 | 18.1 | 16.1 | [607.5, 1136.9] |
| pf_topk | 109.6 | 32.6 | 580.3 | 1377.0 | 20.6 | 15.0 | 27.0 | [524.0, 704.8] |
| mh_ekf | 56.4 | 29.6 | 257.7 | 1443.4 | 7.8 | 6.7 | 49.6 | [70.6, 436.8] |

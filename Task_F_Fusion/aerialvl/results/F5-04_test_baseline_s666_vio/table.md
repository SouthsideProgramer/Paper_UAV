Config: `{"feats": "feats/baseline_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s666_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1044.3 | 280.1 | 3820.5 | 4801.1 | 62.2 | 56.3 | 100.0 | [3800.5, 3828.6] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 34.0 | 28.5 | 91.6 | 171.5 | 9.3 | 4.6 | 0.0 | [84.3, 130.7] |
| pf_topk | 28.4 | 28.3 | 42.1 | 75.2 | 1.7 | 0.0 | 0.0 | [40.6, 44.0] |
| mh_ekf | 27.8 | 28.7 | 40.7 | 69.5 | 0.6 | 0.0 | 0.0 | [40.0, 41.6] |

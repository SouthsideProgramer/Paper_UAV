Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s667_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1170.8 | 586.5 | 3867.5 | 4758.2 | 64.9 | 59.4 | 100.0 | [3827.3, 3894.5] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 29.3 | 26.4 | 49.7 | 156.1 | 5.0 | 1.8 | 0.0 | [46.1, 54.9] |
| pf_topk | 24.3 | 24.9 | 36.0 | 69.8 | 0.3 | 0.0 | 0.0 | [35.2, 37.1] |
| mh_ekf | 24.2 | 24.5 | 36.2 | 80.3 | 0.4 | 0.0 | 0.0 | [35.3, 37.3] |

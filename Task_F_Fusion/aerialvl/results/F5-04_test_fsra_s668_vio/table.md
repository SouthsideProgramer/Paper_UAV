Config: `{"feats": "feats/fsra_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s668_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1276.9 | 833.4 | 3830.5 | 4967.5 | 67.3 | 63.3 | 100.0 | [3790.9, 3875.5] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 25.3 | 24.1 | 37.1 | 156.2 | 1.4 | 1.0 | 0.0 | [36.4, 38.0] |
| pf_topk | 24.5 | 25.0 | 34.9 | 162.4 | 0.2 | 0.0 | 0.0 | [34.0, 35.7] |
| mh_ekf | 23.9 | 24.3 | 33.8 | 79.6 | 0.2 | 0.0 | 0.0 | [33.0, 34.6] |

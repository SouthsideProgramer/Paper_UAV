Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s668_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1248.6 | 799.5 | 3638.2 | 4971.8 | 70.9 | 67.4 | 100.0 | [3613.0, 3648.6] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 27.4 | 26.1 | 51.8 | 99.8 | 5.9 | 0.0 | 0.0 | [49.9, 54.0] |
| pf_topk | 24.7 | 24.6 | 38.2 | 79.6 | 1.4 | 0.0 | 0.0 | [36.6, 40.0] |
| mh_ekf | 25.4 | 25.3 | 39.6 | 73.6 | 1.5 | 0.0 | 0.0 | [37.9, 41.8] |

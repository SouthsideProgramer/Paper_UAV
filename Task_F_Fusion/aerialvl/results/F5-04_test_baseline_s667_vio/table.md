Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s667_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1022.2 | 126.7 | 3778.2 | 5025.9 | 59.0 | 52.4 | 100.0 | [3707.1, 3810.2] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 29.9 | 28.0 | 47.7 | 131.6 | 4.6 | 1.6 | 0.0 | [43.7, 55.1] |
| pf_topk | 27.8 | 27.2 | 42.2 | 80.3 | 1.8 | 0.0 | 0.0 | [40.7, 43.9] |
| mh_ekf | 28.0 | 27.3 | 42.1 | 78.5 | 1.5 | 0.0 | 0.0 | [41.1, 43.3] |

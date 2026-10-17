Config: `{"feats": "feats/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s668_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1085.1 | 573.5 | 3837.9 | 4996.5 | 62.9 | 57.5 | 100.0 | [3813.3, 3851.5] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 29.7 | 25.8 | 47.0 | 172.3 | 4.7 | 2.8 | 0.0 | [42.6, 59.3] |
| pf_topk | 24.7 | 25.1 | 36.0 | 57.4 | 0.2 | 0.0 | 0.0 | [35.0, 37.1] |
| mh_ekf | 24.5 | 25.4 | 35.8 | 68.0 | 0.2 | 0.0 | 0.0 | [35.1, 36.5] |

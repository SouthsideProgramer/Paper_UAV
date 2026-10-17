Config: `{"feats": "feats/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_lpn_s666_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 989.0 | 233.4 | 3890.0 | 4860.8 | 61.8 | 56.3 | 100.0 | [3880.7, 3895.9] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 29.5 | 27.8 | 43.3 | 163.4 | 3.5 | 2.0 | 0.0 | [41.2, 46.4] |
| pf_topk | 27.2 | 27.3 | 40.6 | 71.5 | 1.6 | 0.0 | 0.0 | [39.2, 42.0] |
| mh_ekf | 27.0 | 27.1 | 39.6 | 69.7 | 0.8 | 0.0 | 0.0 | [38.9, 40.5] |

Config: `{"feats": "feats/fsra_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s666_vio", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1185.8 | 580.3 | 3917.6 | 5026.2 | 64.4 | 59.5 | 100.0 | [3887.6, 3925.3] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [96.8, 119.0] |
| ekf_gated | 40.3 | 28.7 | 169.4 | 415.2 | 9.2 | 6.8 | 0.0 | [100.6, 210.8] |
| pf_topk | 28.8 | 29.3 | 40.7 | 72.3 | 0.5 | 0.0 | 0.0 | [39.9, 41.6] |
| mh_ekf | 28.7 | 28.9 | 40.7 | 70.9 | 0.3 | 0.0 | 0.0 | [40.1, 41.4] |

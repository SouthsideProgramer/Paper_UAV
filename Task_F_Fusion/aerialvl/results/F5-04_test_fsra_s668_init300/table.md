Config: `{"feats": "feats/fsra_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s668_init300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1276.9 | 833.4 | 3830.5 | 4967.5 | 67.3 | 63.3 | 100.0 | [3790.9, 3875.5] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [686.3, 834.0] |
| ekf_gated | 281.8 | 30.4 | 1176.6 | 1856.9 | 35.4 | 33.7 | 35.7 | [940.7, 1462.1] |
| pf_topk | 117.3 | 30.1 | 603.3 | 1647.6 | 21.4 | 16.7 | 33.0 | [569.7, 661.9] |
| mh_ekf | 65.2 | 25.5 | 440.6 | 1674.2 | 7.3 | 6.9 | 52.2 | [57.5, 552.3] |

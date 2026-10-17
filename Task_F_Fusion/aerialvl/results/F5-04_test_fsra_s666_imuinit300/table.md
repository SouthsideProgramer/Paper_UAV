Config: `{"feats": "feats/fsra_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_fsra_s666_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1185.8 | 580.3 | 3917.6 | 5026.2 | 64.4 | 59.5 | 100.0 | [3887.6, 3925.3] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 354.5 | 39.7 | 1788.3 | 7091.6 | 41.6 | 35.5 | 39.1 | [1339.9, 2199.7] |
| pf_topk | 588.5 | 324.1 | 2075.4 | 6250.9 | 80.1 | 68.6 | 86.5 | [1907.7, 2257.4] |
| mh_ekf | 88.6 | 32.5 | 418.1 | 5478.7 | 11.5 | 7.4 | 44.3 | [109.6, 650.8] |

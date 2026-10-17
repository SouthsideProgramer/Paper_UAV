Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 2, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "dev_lpn_val_imuinit300_calib", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1262.7 | 887.4 | 3556.2 | 4704.1 | 77.6 | 74.5 | 100.0 | [2909.6, 3762.6] |
| dead_reckoning | 704.8 | 549.9 | 1891.7 | 5006.3 | 99.6 | 98.8 | 88.5 | [1254.6, 2561.9] |
| ekf_gated | 701.2 | 329.3 | 2293.4 | 4671.1 | 70.1 | 66.0 | 65.4 | [1873.9, 2893.8] |
| pf_topk | 853.8 | 629.1 | 2599.8 | 6521.7 | 90.5 | 84.2 | 100.0 | [1876.7, 3457.7] |
| mh_ekf | 450.8 | 148.7 | 1415.4 | 3746.7 | 59.4 | 55.1 | 76.9 | [1187.7, 2039.5] |

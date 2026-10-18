Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 2, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "dev_lpn_val_init300_calib", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1262.7 | 887.4 | 3556.2 | 4704.1 | 77.6 | 74.5 | 100.0 | [2909.6, 3762.6] |
| dead_reckoning | 435.3 | 432.7 | 732.4 | 910.8 | 100.0 | 100.0 | 46.2 | [670.7, 893.0] |
| ekf_gated | 354.7 | 256.9 | 1003.0 | 1302.7 | 63.0 | 58.9 | 53.8 | [890.3, 1274.0] |
| pf_topk | 351.8 | 64.4 | 1034.6 | 1275.3 | 56.9 | 43.5 | 57.7 | [875.9, 1265.5] |
| mh_ekf | 392.0 | 40.7 | 1589.0 | 2015.2 | 45.4 | 45.2 | 73.1 | [963.8, 1816.2] |

Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 2, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 8, "n_boot": 500, "tag": "dev_lpn_val_vio", "cfg": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1270.3 | 895.4 | 3561.1 | 4700.7 | 82.5 | 74.4 | 100.0 | [2923.0, 3777.2] |
| dead_reckoning | 39.1 | 30.4 | 105.5 | 165.6 | 23.5 | 6.0 | 0.0 | [69.3, 133.2] |
| ekf_gated | 79.0 | 47.7 | 247.1 | 271.2 | 47.1 | 23.0 | 0.0 | [245.6, 248.7] |
| pf_topk | 32.0 | 28.9 | 62.6 | 108.4 | 15.8 | 0.1 | 0.0 | [55.4, 70.3] |
| mh_ekf | 71.6 | 33.1 | 323.4 | 513.9 | 33.7 | 22.6 | 7.7 | [252.7, 345.8] |

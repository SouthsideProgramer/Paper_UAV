Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 2, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 8, "n_boot": 500, "tag": "dev_lpn_val_vio_calib", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1262.7 | 887.4 | 3556.2 | 4704.1 | 77.6 | 74.5 | 100.0 | [2909.6, 3762.6] |
| dead_reckoning | 39.1 | 30.4 | 105.5 | 165.6 | 23.5 | 6.0 | 0.0 | [69.3, 133.2] |
| ekf_gated | 73.0 | 36.3 | 265.4 | 289.6 | 31.8 | 20.8 | 0.0 | [263.7, 266.4] |
| pf_topk | 25.9 | 22.1 | 57.5 | 106.2 | 9.1 | 0.1 | 0.0 | [49.9, 61.7] |
| mh_ekf | 69.5 | 25.1 | 336.5 | 493.2 | 22.7 | 22.5 | 0.0 | [269.7, 358.4] |

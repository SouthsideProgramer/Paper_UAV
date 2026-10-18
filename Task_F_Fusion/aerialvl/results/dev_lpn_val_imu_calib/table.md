Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 2, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "dev_lpn_val_imu_calib", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1262.7 | 887.4 | 3556.2 | 4704.1 | 77.6 | 74.5 | 100.0 | [2909.6, 3762.6] |
| dead_reckoning | 496.7 | 258.6 | 1957.2 | 4795.8 | 80.6 | 72.2 | 69.2 | [1259.9, 2553.8] |
| ekf_gated | 318.7 | 72.8 | 1558.9 | 5396.5 | 54.6 | 46.2 | 38.5 | [495.1, 2969.0] |
| pf_topk | 282.1 | 57.5 | 1329.2 | 4409.7 | 53.4 | 40.9 | 50.0 | [773.9, 1933.6] |
| mh_ekf | 155.4 | 42.6 | 631.3 | 2339.7 | 44.3 | 36.2 | 15.4 | [354.4, 1124.9] |

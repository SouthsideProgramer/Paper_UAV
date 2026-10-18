Config: `{"feats": "feats/merged/lpn_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1255.8 | 875.4 | 3715.7 | 5121.4 | 70.7 | 65.9 | 100.0 | [3595.5, 3830.9] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 39.7 | 27.6 | 134.1 | 353.9 | 12.2 | 6.0 | 0.0 | [96.9, 155.0] |
| pf_topk | 27.0 | 25.7 | 46.4 | 150.1 | 3.2 | 0.3 | 0.0 | [44.2, 48.9] |
| mh_ekf | 26.3 | 25.5 | 44.2 | 106.4 | 1.6 | 0.0 | 0.0 | [42.7, 45.7] |

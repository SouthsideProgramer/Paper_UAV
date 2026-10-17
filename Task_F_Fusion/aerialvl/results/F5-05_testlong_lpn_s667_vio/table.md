Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1305.7 | 1013.7 | 3682.1 | 4952.4 | 72.7 | 68.4 | 100.0 | [3555.6, 3808.4] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 34.8 | 28.3 | 87.3 | 270.9 | 12.6 | 2.8 | 0.0 | [73.8, 91.6] |
| pf_topk | 29.0 | 26.2 | 50.4 | 184.3 | 5.1 | 1.4 | 0.0 | [46.3, 68.4] |
| mh_ekf | 29.3 | 26.6 | 51.9 | 174.8 | 5.5 | 1.5 | 0.0 | [46.8, 70.8] |

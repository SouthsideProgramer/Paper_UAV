Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s667_imu", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1305.7 | 1013.7 | 3682.1 | 4952.4 | 72.7 | 68.4 | 100.0 | [3555.6, 3808.4] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 179.7 | 36.0 | 992.0 | 5055.1 | 33.1 | 18.2 | 18.4 | [569.9, 1544.0] |
| pf_topk | 192.9 | 46.7 | 899.9 | 3623.6 | 47.4 | 31.5 | 34.5 | [699.8, 1147.8] |
| mh_ekf | 80.1 | 32.0 | 246.6 | 3643.8 | 23.7 | 11.7 | 12.1 | [158.3, 423.9] |

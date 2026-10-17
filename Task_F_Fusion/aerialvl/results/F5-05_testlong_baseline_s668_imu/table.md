Config: `{"feats": "feats/merged/baseline_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1335.9 | 1038.9 | 3734.8 | 5512.3 | 75.1 | 70.9 | 100.0 | [3660.6, 3847.2] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 291.0 | 50.0 | 1596.4 | 5535.8 | 50.0 | 32.2 | 38.5 | [1201.0, 2067.3] |
| pf_topk | 255.6 | 57.6 | 1238.6 | 4280.7 | 54.7 | 38.3 | 47.7 | [981.9, 1479.2] |
| mh_ekf | 148.1 | 34.8 | 765.3 | 8276.3 | 30.9 | 17.1 | 18.4 | [400.6, 1106.6] |

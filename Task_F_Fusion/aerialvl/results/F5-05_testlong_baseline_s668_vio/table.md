Config: `{"feats": "feats/merged/baseline_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1335.9 | 1038.9 | 3734.8 | 5512.3 | 75.1 | 70.9 | 100.0 | [3660.6, 3847.2] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 41.3 | 29.9 | 136.6 | 333.7 | 17.0 | 7.3 | 0.0 | [116.5, 142.9] |
| pf_topk | 29.3 | 27.0 | 53.0 | 183.8 | 6.2 | 0.8 | 0.0 | [48.8, 60.2] |
| mh_ekf | 28.0 | 26.9 | 45.3 | 179.1 | 2.3 | 0.3 | 0.0 | [44.1, 47.0] |

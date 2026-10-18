Config: `{"feats": "feats/merged/lpn_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1255.8 | 875.4 | 3715.7 | 5121.4 | 70.7 | 65.9 | 100.0 | [3595.5, 3830.9] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 210.4 | 38.5 | 1135.3 | 6279.8 | 39.2 | 25.7 | 28.7 | [823.2, 1407.0] |
| pf_topk | 235.9 | 48.4 | 1170.3 | 5027.4 | 48.7 | 33.2 | 42.5 | [965.1, 1420.0] |
| mh_ekf | 104.1 | 31.1 | 473.1 | 3305.0 | 23.4 | 11.9 | 14.9 | [235.0, 811.1] |

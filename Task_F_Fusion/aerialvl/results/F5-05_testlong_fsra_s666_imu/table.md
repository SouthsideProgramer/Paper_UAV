Config: `{"feats": "feats/merged/fsra_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s666_imu", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1309.6 | 950.1 | 3771.8 | 5046.0 | 73.6 | 68.7 | 100.0 | [3640.9, 3894.3] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 259.8 | 40.8 | 1568.8 | 8283.1 | 39.1 | 23.6 | 30.5 | [1132.4, 2013.1] |
| pf_topk | 191.3 | 47.9 | 851.4 | 3727.4 | 48.1 | 31.4 | 38.5 | [696.8, 1099.8] |
| mh_ekf | 104.5 | 33.9 | 281.5 | 6430.9 | 21.9 | 11.1 | 12.1 | [153.0, 647.0] |

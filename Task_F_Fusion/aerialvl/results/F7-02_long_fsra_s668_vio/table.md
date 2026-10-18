Config: `{"feats": "feats/ft/merged/fsra_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 678.2 | 44.6 | 3271.8 | 4945.4 | 46.1 | 38.0 | 100.0 | [3004.9, 3381.5] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 30.6 | 25.6 | 54.2 | 254.4 | 6.6 | 2.7 | 0.0 | [49.5, 61.8] |
| pf_topk | 26.3 | 25.3 | 46.3 | 131.3 | 3.4 | 0.1 | 0.0 | [44.0, 49.4] |
| mh_ekf | 26.1 | 25.1 | 46.0 | 112.1 | 3.0 | 0.0 | 0.0 | [44.5, 48.6] |
| naviloc | 55.9 | 27.7 | 153.4 | 1552.6 | 10.1 | 5.6 | 5.2 | [55.8, 430.9] |
| naviloc_yaw | 44.4 | 27.7 | 173.6 | 471.0 | 10.6 | 6.5 | 0.0 | [55.9, 339.2] |

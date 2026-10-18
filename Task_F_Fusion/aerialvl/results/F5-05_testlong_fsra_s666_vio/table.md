Config: `{"feats": "feats/merged/fsra_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1309.6 | 950.1 | 3771.8 | 5046.0 | 73.6 | 68.7 | 100.0 | [3640.9, 3894.3] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 35.8 | 29.9 | 71.6 | 283.9 | 10.1 | 4.7 | 0.0 | [57.6, 127.0] |
| pf_topk | 30.2 | 28.3 | 48.5 | 177.2 | 4.3 | 1.6 | 0.0 | [45.4, 55.0] |
| mh_ekf | 30.9 | 28.7 | 49.5 | 250.6 | 4.7 | 1.5 | 0.0 | [46.9, 55.7] |

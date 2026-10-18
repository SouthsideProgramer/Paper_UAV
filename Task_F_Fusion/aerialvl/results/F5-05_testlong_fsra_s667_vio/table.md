Config: `{"feats": "feats/merged/fsra_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1350.9 | 1040.5 | 3839.4 | 4997.8 | 72.7 | 68.1 | 100.0 | [3703.7, 3926.7] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 38.6 | 29.3 | 108.5 | 380.9 | 14.9 | 5.7 | 0.0 | [81.2, 120.8] |
| pf_topk | 33.2 | 28.5 | 56.7 | 365.1 | 7.3 | 2.8 | 0.0 | [50.0, 83.9] |
| mh_ekf | 30.9 | 29.1 | 51.4 | 268.0 | 5.7 | 1.1 | 0.0 | [48.5, 56.9] |

Config: `{"feats": "feats/merged/fsra_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1309.6 | 950.1 | 3771.8 | 5046.0 | 73.6 | 68.7 | 100.0 | [3640.9, 3894.3] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 616.3 | 175.9 | 2432.9 | 8289.9 | 65.8 | 54.3 | 60.3 | [2124.5, 2691.3] |
| pf_topk | 606.3 | 374.5 | 2113.2 | 6297.2 | 83.2 | 72.2 | 87.9 | [1866.6, 2333.4] |
| mh_ekf | 191.3 | 38.2 | 1106.4 | 5034.4 | 32.9 | 22.6 | 61.5 | [795.4, 1405.7] |

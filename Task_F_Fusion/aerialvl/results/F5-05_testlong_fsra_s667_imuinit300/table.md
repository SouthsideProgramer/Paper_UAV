Config: `{"feats": "feats/merged/fsra_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_fsra_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1350.9 | 1040.5 | 3839.4 | 4997.8 | 72.7 | 68.1 | 100.0 | [3703.7, 3926.7] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 588.3 | 145.7 | 2275.0 | 6003.6 | 64.4 | 53.7 | 59.2 | [1916.7, 2587.7] |
| pf_topk | 674.0 | 426.9 | 2212.9 | 6095.2 | 86.6 | 76.7 | 90.2 | [1963.0, 2419.4] |
| mh_ekf | 241.2 | 40.5 | 1384.9 | 5164.4 | 38.7 | 25.7 | 65.5 | [1038.8, 1687.1] |

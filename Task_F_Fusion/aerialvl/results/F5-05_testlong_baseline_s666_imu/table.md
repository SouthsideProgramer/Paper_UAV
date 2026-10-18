Config: `{"feats": "feats/merged/baseline_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s666_imu", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1272.7 | 868.2 | 3744.3 | 4830.6 | 72.5 | 67.4 | 100.0 | [3631.8, 3833.3] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1578.3, 1891.6] |
| ekf_gated | 171.3 | 40.3 | 782.8 | 3721.9 | 40.5 | 25.2 | 28.2 | [606.7, 1101.2] |
| pf_topk | 228.1 | 53.7 | 1021.3 | 4131.1 | 52.4 | 36.3 | 43.7 | [858.7, 1215.6] |
| mh_ekf | 144.7 | 36.2 | 634.8 | 7188.5 | 30.7 | 15.5 | 19.0 | [373.8, 965.0] |

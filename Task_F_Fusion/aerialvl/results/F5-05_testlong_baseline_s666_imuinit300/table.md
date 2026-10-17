Config: `{"feats": "feats/merged/baseline_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1272.7 | 868.2 | 3744.3 | 4830.6 | 72.5 | 67.4 | 100.0 | [3631.8, 3833.3] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 615.4 | 224.8 | 2385.4 | 7064.2 | 66.0 | 57.5 | 62.1 | [2001.1, 2789.5] |
| pf_topk | 639.3 | 394.0 | 2135.5 | 5896.4 | 85.9 | 75.4 | 87.9 | [1862.7, 2366.9] |
| mh_ekf | 211.9 | 40.1 | 1100.4 | 4973.8 | 38.6 | 25.0 | 66.7 | [702.9, 1421.4] |

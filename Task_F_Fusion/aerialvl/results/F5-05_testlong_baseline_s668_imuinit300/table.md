Config: `{"feats": "feats/merged/baseline_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1335.9 | 1038.9 | 3734.8 | 5512.3 | 75.1 | 70.9 | 100.0 | [3660.6, 3847.2] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 700.2 | 346.8 | 2479.1 | 6606.3 | 73.3 | 62.4 | 67.8 | [2174.8, 2823.5] |
| pf_topk | 686.1 | 442.8 | 2242.6 | 5458.5 | 86.6 | 77.1 | 91.4 | [1980.7, 2483.7] |
| mh_ekf | 283.9 | 41.8 | 1480.1 | 4984.8 | 42.5 | 31.1 | 67.8 | [1160.4, 1764.2] |

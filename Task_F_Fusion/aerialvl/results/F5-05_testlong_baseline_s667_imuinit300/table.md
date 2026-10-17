Config: `{"feats": "feats/merged/baseline_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1291.5 | 861.6 | 3815.4 | 5190.1 | 71.5 | 66.1 | 100.0 | [3735.4, 3911.5] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 619.7 | 162.7 | 2484.8 | 5743.7 | 66.3 | 55.1 | 56.3 | [2182.7, 2703.1] |
| pf_topk | 686.6 | 448.0 | 2212.1 | 6047.2 | 85.7 | 77.3 | 92.5 | [1879.8, 2590.2] |
| mh_ekf | 227.8 | 40.0 | 1170.9 | 4107.8 | 40.3 | 28.4 | 62.6 | [933.4, 1472.2] |

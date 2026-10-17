Config: `{"feats": "feats/merged/baseline_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1291.5 | 861.6 | 3815.4 | 5190.1 | 71.5 | 66.1 | 100.0 | [3735.4, 3911.5] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.0, 107.9] |
| ekf_gated | 41.1 | 28.0 | 126.5 | 346.7 | 14.5 | 8.4 | 0.0 | [114.2, 185.8] |
| pf_topk | 32.2 | 27.1 | 64.1 | 314.4 | 8.2 | 2.8 | 0.0 | [51.7, 92.3] |
| mh_ekf | 29.5 | 26.6 | 56.1 | 181.4 | 6.8 | 1.3 | 0.0 | [49.7, 64.5] |

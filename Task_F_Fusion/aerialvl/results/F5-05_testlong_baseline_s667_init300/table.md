Config: `{"feats": "feats/merged/baseline_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_baseline_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1291.5 | 861.6 | 3815.4 | 5190.1 | 71.5 | 66.1 | 100.0 | [3735.4, 3911.5] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.7, 880.3] |
| ekf_gated | 413.0 | 63.3 | 1386.9 | 2071.7 | 52.7 | 46.8 | 41.4 | [1187.3, 1681.1] |
| pf_topk | 178.6 | 38.0 | 918.2 | 1775.2 | 37.8 | 28.6 | 42.0 | [742.6, 962.3] |
| mh_ekf | 117.6 | 29.9 | 754.5 | 2057.1 | 21.6 | 15.6 | 58.0 | [517.4, 925.1] |

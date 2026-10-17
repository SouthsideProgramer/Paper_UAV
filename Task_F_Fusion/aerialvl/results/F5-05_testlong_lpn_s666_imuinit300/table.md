Config: `{"feats": "feats/merged/lpn_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 500, "tag": "F5-05_testlong_lpn_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1244.3 | 829.2 | 3650.1 | 5108.1 | 72.1 | 66.8 | 100.0 | [3519.3, 3800.2] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.0, 2042.5] |
| ekf_gated | 576.0 | 148.6 | 2241.0 | 5430.7 | 64.2 | 53.6 | 58.6 | [1945.7, 2552.2] |
| pf_topk | 610.4 | 362.9 | 2063.5 | 7118.5 | 84.1 | 74.1 | 85.6 | [1817.5, 2297.2] |
| mh_ekf | 203.1 | 39.1 | 1120.3 | 7047.1 | 37.4 | 24.3 | 66.7 | [725.1, 1508.8] |

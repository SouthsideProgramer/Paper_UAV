Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s668_imu", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1248.6 | 799.5 | 3638.2 | 4971.8 | 70.9 | 67.4 | 100.0 | [3613.0, 3648.6] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1703.5, 1999.6] |
| ekf_gated | 55.1 | 30.6 | 115.7 | 5519.9 | 18.6 | 6.5 | 7.0 | [100.3, 149.0] |
| pf_topk | 125.3 | 35.2 | 611.7 | 2988.9 | 34.4 | 21.7 | 32.6 | [505.8, 727.9] |
| mh_ekf | 44.1 | 26.8 | 60.6 | 5349.4 | 7.9 | 2.1 | 4.3 | [55.1, 67.8] |

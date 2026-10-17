Config: `{"feats": "feats/baseline_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s668_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1248.6 | 799.5 | 3638.2 | 4971.8 | 70.9 | 67.4 | 100.0 | [3613.0, 3648.6] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 457.0 | 54.8 | 1764.6 | 7559.2 | 51.6 | 43.8 | 54.3 | [1523.5, 2036.3] |
| pf_topk | 630.3 | 406.4 | 2063.3 | 5777.6 | 81.8 | 72.8 | 89.1 | [1908.2, 2223.6] |
| mh_ekf | 73.5 | 28.1 | 408.1 | 4581.1 | 13.4 | 7.6 | 58.3 | [142.7, 577.5] |

Config: `{"feats": "feats/baseline_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 10, "n_boot": 500, "tag": "F5-04_test_baseline_s667_imuinit300", "cfg": "", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1022.2 | 126.7 | 3778.2 | 5025.9 | 59.0 | 52.4 | 100.0 | [3707.1, 3810.2] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1762.8, 2078.2] |
| ekf_gated | 205.6 | 35.5 | 1162.2 | 9002.8 | 27.9 | 18.7 | 23.9 | [969.6, 1399.3] |
| pf_topk | 550.5 | 265.6 | 2002.8 | 6387.3 | 76.5 | 64.4 | 86.5 | [1825.8, 2182.5] |
| mh_ekf | 71.1 | 32.1 | 109.5 | 6249.8 | 12.7 | 5.2 | 46.5 | [70.4, 329.4] |

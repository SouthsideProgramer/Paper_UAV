Config: `{"feats": "feats/ft/baseline_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s668_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 375.9 | 31.7 | 2584.7 | 4647.8 | 25.1 | 19.8 | 95.7 | [2525.3, 2679.8] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 32.8 | 28.1 | 56.1 | 1135.1 | 7.2 | 1.7 | 3.0 | [52.5, 62.5] |
| pf_topk | 98.5 | 31.0 | 485.5 | 3004.3 | 25.7 | 17.2 | 24.8 | [402.9, 572.5] |
| mh_ekf | 31.6 | 28.1 | 53.5 | 847.9 | 6.3 | 1.4 | 2.2 | [49.9, 58.2] |
| naviloc | 358.0 | 206.6 | 1235.7 | 2853.9 | 82.0 | 68.1 | 75.2 | [1124.4, 1318.8] |
| naviloc_yaw | 371.4 | 259.9 | 1112.5 | 2972.1 | 85.4 | 73.9 | 78.7 | [1040.4, 1211.8] |

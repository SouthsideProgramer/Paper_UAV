Config: `{"feats": "feats/ft/baseline_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s666_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 351.2 | 31.0 | 2487.2 | 4808.3 | 24.8 | 18.5 | 95.7 | [2402.7, 2530.7] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 30.7 | 25.5 | 57.2 | 1053.8 | 7.9 | 1.9 | 4.8 | [54.1, 62.8] |
| pf_topk | 82.9 | 28.6 | 405.6 | 2323.9 | 21.4 | 14.0 | 18.7 | [311.7, 489.5] |
| mh_ekf | 27.8 | 25.3 | 44.9 | 1010.4 | 2.8 | 0.7 | 1.7 | [43.6, 46.6] |
| naviloc | 331.1 | 195.9 | 1117.3 | 3024.8 | 80.7 | 67.0 | 74.8 | [1012.7, 1251.7] |
| naviloc_yaw | 372.2 | 260.1 | 1094.8 | 2952.2 | 85.1 | 74.1 | 78.7 | [1022.6, 1188.6] |

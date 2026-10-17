Config: `{"feats": "feats/ft/baseline_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 351.2 | 31.0 | 2487.2 | 4808.3 | 24.8 | 18.5 | 95.7 | [2402.7, 2530.7] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 88.6 | 26.4 | 156.1 | 6043.8 | 12.3 | 6.1 | 12.6 | [79.7, 797.3] |
| pf_topk | 509.5 | 219.8 | 1937.5 | 6074.0 | 72.8 | 60.2 | 81.7 | [1731.1, 2140.9] |
| mh_ekf | 46.3 | 25.8 | 53.2 | 3756.8 | 5.6 | 3.0 | 30.9 | [46.6, 74.3] |
| naviloc | 331.1 | 195.9 | 1117.3 | 3024.8 | 80.7 | 67.0 | 74.8 | [1012.7, 1251.7] |
| naviloc_yaw | 372.2 | 260.1 | 1094.8 | 2952.2 | 85.1 | 74.1 | 78.7 | [1022.6, 1188.6] |

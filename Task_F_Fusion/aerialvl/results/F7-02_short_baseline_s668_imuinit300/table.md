Config: `{"feats": "feats/ft/baseline_s668.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s668_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 375.9 | 31.7 | 2584.7 | 4647.8 | 25.1 | 19.8 | 95.7 | [2525.3, 2679.8] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 137.2 | 28.8 | 870.1 | 6430.6 | 12.8 | 8.1 | 10.0 | [124.7, 1215.8] |
| pf_topk | 540.1 | 224.0 | 2111.7 | 6626.4 | 72.3 | 60.3 | 81.3 | [1892.3, 2388.0] |
| mh_ekf | 60.7 | 28.5 | 91.3 | 4471.5 | 9.5 | 4.8 | 36.1 | [59.4, 304.8] |
| naviloc | 358.0 | 206.6 | 1235.7 | 2853.9 | 82.0 | 68.1 | 75.2 | [1124.4, 1318.8] |
| naviloc_yaw | 371.4 | 259.9 | 1112.5 | 2972.1 | 85.4 | 73.9 | 78.7 | [1040.4, 1211.8] |

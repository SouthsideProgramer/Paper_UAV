Config: `{"feats": "feats/ft/baseline_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s667_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 301.7 | 33.1 | 2130.2 | 5014.8 | 26.9 | 17.8 | 100.0 | [2085.1, 2359.4] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 23.9 | 23.5 | 37.3 | 191.1 | 1.3 | 0.4 | 0.0 | [35.9, 38.8] |
| pf_topk | 24.0 | 23.8 | 36.7 | 71.6 | 0.4 | 0.0 | 0.0 | [35.8, 37.7] |
| mh_ekf | 24.2 | 24.3 | 35.8 | 58.6 | 0.1 | 0.0 | 0.0 | [35.1, 36.6] |
| naviloc | 24.2 | 23.8 | 39.3 | 90.7 | 1.1 | 0.0 | 0.0 | [38.1, 40.4] |
| naviloc_yaw | 24.1 | 23.7 | 39.0 | 90.7 | 1.1 | 0.0 | 0.0 | [37.9, 40.1] |

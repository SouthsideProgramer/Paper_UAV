Config: `{"feats": "feats/ft/baseline_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s667_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 301.7 | 33.1 | 2130.2 | 5014.8 | 26.9 | 17.8 | 100.0 | [2085.1, 2359.4] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 58.2 | 24.2 | 100.5 | 931.8 | 6.6 | 5.0 | 6.1 | [45.9, 727.8] |
| pf_topk | 52.2 | 25.3 | 64.4 | 1058.5 | 6.8 | 4.3 | 12.2 | [47.5, 619.1] |
| mh_ekf | 30.4 | 24.4 | 37.4 | 1103.5 | 1.8 | 0.9 | 32.6 | [36.1, 38.8] |
| naviloc | 24.2 | 23.8 | 39.3 | 90.7 | 1.1 | 0.0 | 0.0 | [38.1, 40.4] |
| naviloc_yaw | 24.1 | 23.7 | 39.0 | 90.7 | 1.1 | 0.0 | 0.0 | [37.9, 40.1] |

Config: `{"feats": "feats/ft/fsra_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s667_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 269.2 | 33.2 | 1750.7 | 4078.3 | 25.8 | 18.2 | 95.7 | [1617.9, 1931.8] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 46.2 | 23.0 | 71.7 | 1100.5 | 5.8 | 3.8 | 2.2 | [43.9, 127.9] |
| pf_topk | 42.1 | 24.3 | 51.4 | 1221.7 | 5.3 | 3.1 | 11.7 | [45.5, 115.3] |
| mh_ekf | 28.0 | 22.6 | 37.0 | 1752.5 | 1.2 | 0.9 | 32.2 | [36.1, 37.8] |
| naviloc | 21.3 | 21.0 | 35.8 | 71.5 | 0.4 | 0.0 | 0.0 | [34.6, 37.3] |
| naviloc_yaw | 21.4 | 21.0 | 36.0 | 71.5 | 0.4 | 0.0 | 0.0 | [34.6, 37.6] |

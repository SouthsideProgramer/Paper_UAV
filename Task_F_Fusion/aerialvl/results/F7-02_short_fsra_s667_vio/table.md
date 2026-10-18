Config: `{"feats": "feats/ft/fsra_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s667_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 269.2 | 33.2 | 1750.7 | 4078.3 | 25.8 | 18.2 | 95.7 | [1617.9, 1931.8] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 24.5 | 22.4 | 40.6 | 134.4 | 3.1 | 1.3 | 0.0 | [38.5, 43.2] |
| pf_topk | 22.0 | 22.4 | 34.7 | 53.1 | 0.0 | 0.0 | 0.0 | [33.9, 35.4] |
| mh_ekf | 22.1 | 22.4 | 35.5 | 52.0 | 0.0 | 0.0 | 0.0 | [34.7, 36.3] |
| naviloc | 21.3 | 21.0 | 35.8 | 71.5 | 0.4 | 0.0 | 0.0 | [34.6, 37.3] |
| naviloc_yaw | 21.4 | 21.0 | 36.0 | 71.5 | 0.4 | 0.0 | 0.0 | [34.6, 37.6] |

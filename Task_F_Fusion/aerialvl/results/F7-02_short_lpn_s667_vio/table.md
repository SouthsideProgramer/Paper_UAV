Config: `{"feats": "feats/ft/lpn_s667.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s667_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 339.2 | 30.7 | 2377.5 | 4871.0 | 21.8 | 17.3 | 100.0 | [2334.0, 2421.6] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 21.6 | 21.5 | 33.0 | 165.9 | 0.1 | 0.1 | 0.0 | [32.4, 33.6] |
| pf_topk | 21.8 | 22.1 | 32.2 | 67.8 | 0.1 | 0.0 | 0.0 | [31.6, 33.0] |
| mh_ekf | 21.7 | 22.0 | 32.8 | 52.7 | 0.0 | 0.0 | 0.0 | [31.9, 33.4] |
| naviloc | 22.2 | 21.9 | 35.8 | 85.5 | 0.6 | 0.0 | 0.0 | [34.7, 37.0] |
| naviloc_yaw | 22.2 | 21.9 | 36.1 | 87.0 | 0.6 | 0.0 | 0.0 | [34.9, 37.2] |

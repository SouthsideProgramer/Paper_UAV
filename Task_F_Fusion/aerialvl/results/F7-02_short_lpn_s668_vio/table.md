Config: `{"feats": "feats/ft/lpn_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s668_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 283.8 | 33.9 | 2183.6 | 4189.5 | 27.8 | 19.1 | 100.0 | [2099.5, 2224.7] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 25.7 | 25.7 | 39.2 | 62.3 | 0.1 | 0.0 | 0.0 | [38.4, 39.7] |
| pf_topk | 24.7 | 25.1 | 37.1 | 50.4 | 0.0 | 0.0 | 0.0 | [36.3, 37.8] |
| mh_ekf | 25.4 | 25.6 | 38.3 | 49.1 | 0.0 | 0.0 | 0.0 | [37.5, 39.1] |
| naviloc | 24.1 | 23.6 | 38.8 | 76.8 | 0.9 | 0.0 | 0.0 | [37.8, 39.9] |
| naviloc_yaw | 24.1 | 23.6 | 39.0 | 79.0 | 0.9 | 0.0 | 0.0 | [37.9, 40.0] |

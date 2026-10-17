Config: `{"feats": "feats/ft/fsra_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s668_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 313.8 | 33.8 | 2148.1 | 4430.4 | 27.5 | 19.1 | 97.8 | [2104.1, 2342.0] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 24.2 | 24.0 | 40.6 | 253.2 | 0.9 | 0.0 | 0.0 | [39.5, 42.6] |
| pf_topk | 26.2 | 23.5 | 37.7 | 434.0 | 2.3 | 1.4 | 0.0 | [35.7, 42.0] |
| mh_ekf | 23.3 | 23.2 | 36.0 | 130.7 | 0.2 | 0.0 | 0.0 | [35.3, 36.7] |
| naviloc | 23.4 | 23.0 | 38.5 | 87.4 | 0.6 | 0.0 | 0.0 | [37.5, 39.6] |
| naviloc_yaw | 23.4 | 23.0 | 38.6 | 87.4 | 0.6 | 0.0 | 0.0 | [37.6, 39.6] |

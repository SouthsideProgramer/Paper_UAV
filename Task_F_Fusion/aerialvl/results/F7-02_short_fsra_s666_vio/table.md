Config: `{"feats": "feats/ft/fsra_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s666_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 387.4 | 37.0 | 2466.3 | 4384.7 | 33.6 | 26.7 | 100.0 | [2441.1, 2660.8] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 28.4 | 25.9 | 52.3 | 145.1 | 5.4 | 2.0 | 0.0 | [46.7, 59.3] |
| pf_topk | 25.5 | 25.2 | 39.1 | 77.8 | 0.5 | 0.0 | 0.0 | [38.0, 40.0] |
| mh_ekf | 26.0 | 25.8 | 40.1 | 59.8 | 0.6 | 0.0 | 0.0 | [38.3, 41.9] |
| naviloc | 26.6 | 26.2 | 43.7 | 88.9 | 2.3 | 0.0 | 0.0 | [42.5, 45.0] |
| naviloc_yaw | 26.6 | 26.1 | 43.4 | 88.9 | 2.1 | 0.0 | 0.0 | [42.2, 44.6] |

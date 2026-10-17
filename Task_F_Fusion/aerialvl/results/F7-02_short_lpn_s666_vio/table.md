Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_lpn_s666_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 289.0 | 32.7 | 2063.6 | 4573.9 | 24.4 | 17.9 | 97.8 | [1918.9, 2167.8] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 25.8 | 25.0 | 44.6 | 110.6 | 3.5 | 0.0 | 0.0 | [41.6, 48.5] |
| pf_topk | 23.6 | 23.8 | 37.1 | 62.4 | 0.2 | 0.0 | 0.0 | [36.2, 38.2] |
| mh_ekf | 24.1 | 24.4 | 38.9 | 63.4 | 0.3 | 0.0 | 0.0 | [37.5, 39.9] |
| naviloc | 23.7 | 23.6 | 38.0 | 83.6 | 0.5 | 0.0 | 0.0 | [37.4, 38.9] |
| naviloc_yaw | 23.6 | 23.4 | 38.1 | 70.6 | 0.5 | 0.0 | 0.0 | [37.4, 38.9] |

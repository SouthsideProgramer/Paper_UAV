Config: `{"feats": "feats/ft/baseline_s668.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s668_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 375.9 | 31.7 | 2584.7 | 4647.8 | 25.1 | 19.8 | 95.7 | [2525.3, 2679.8] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 23.6 | 23.5 | 37.6 | 162.4 | 1.3 | 0.0 | 0.0 | [36.3, 38.9] |
| pf_topk | 23.0 | 23.4 | 36.2 | 60.3 | 0.1 | 0.0 | 0.0 | [35.0, 37.1] |
| mh_ekf | 23.5 | 23.8 | 38.7 | 56.5 | 0.2 | 0.0 | 0.0 | [37.3, 39.7] |
| naviloc | 23.4 | 23.7 | 37.0 | 88.7 | 0.5 | 0.0 | 0.0 | [36.1, 38.0] |
| naviloc_yaw | 23.3 | 23.6 | 36.7 | 73.8 | 0.4 | 0.0 | 0.0 | [35.9, 37.7] |

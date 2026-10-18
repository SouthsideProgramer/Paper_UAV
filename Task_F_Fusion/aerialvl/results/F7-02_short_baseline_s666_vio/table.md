Config: `{"feats": "feats/ft/baseline_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s666_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 351.2 | 31.0 | 2487.2 | 4808.3 | 24.8 | 18.5 | 95.7 | [2402.7, 2530.7] |
| dead_reckoning | 40.0 | 30.5 | 105.6 | 240.9 | 28.0 | 5.9 | 0.0 | [97.2, 119.1] |
| ekf_gated | 24.2 | 23.6 | 40.7 | 110.3 | 2.8 | 0.1 | 0.0 | [38.1, 44.4] |
| pf_topk | 22.6 | 23.5 | 33.1 | 58.8 | 0.0 | 0.0 | 0.0 | [32.3, 34.1] |
| mh_ekf | 22.3 | 23.1 | 33.3 | 53.9 | 0.0 | 0.0 | 0.0 | [32.6, 34.0] |
| naviloc | 22.2 | 22.3 | 35.6 | 84.6 | 0.4 | 0.0 | 0.0 | [34.6, 36.9] |
| naviloc_yaw | 22.2 | 22.2 | 35.6 | 87.3 | 0.5 | 0.0 | 0.0 | [34.6, 37.0] |

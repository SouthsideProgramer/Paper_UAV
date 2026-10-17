Config: `{"feats": "feats/ft/baseline_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_baseline_s666_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 351.2 | 31.0 | 2487.2 | 4808.3 | 24.8 | 18.5 | 95.7 | [2402.7, 2530.7] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 71.1 | 24.3 | 486.7 | 1425.2 | 8.6 | 5.4 | 7.8 | [71.4, 804.4] |
| pf_topk | 46.4 | 25.5 | 136.1 | 982.3 | 8.3 | 5.3 | 10.9 | [52.1, 334.6] |
| mh_ekf | 38.6 | 23.5 | 37.5 | 1712.4 | 3.6 | 2.6 | 30.0 | [35.3, 63.5] |
| naviloc | 22.2 | 22.3 | 35.6 | 84.6 | 0.4 | 0.0 | 0.0 | [34.6, 36.9] |
| naviloc_yaw | 22.2 | 22.2 | 35.6 | 87.3 | 0.5 | 0.0 | 0.0 | [34.6, 37.0] |

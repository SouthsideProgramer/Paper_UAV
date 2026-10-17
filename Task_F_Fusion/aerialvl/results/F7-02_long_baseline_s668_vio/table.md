Config: `{"feats": "feats/ft/merged/baseline_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 632.1 | 44.2 | 3094.5 | 4963.6 | 45.6 | 35.8 | 100.0 | [2948.4, 3169.0] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 29.5 | 26.1 | 51.0 | 266.9 | 5.6 | 0.9 | 0.0 | [48.8, 54.5] |
| pf_topk | 27.9 | 26.2 | 49.4 | 135.7 | 4.7 | 0.9 | 0.0 | [45.7, 54.5] |
| mh_ekf | 27.2 | 25.7 | 48.3 | 112.0 | 4.0 | 0.3 | 0.0 | [45.3, 50.5] |
| naviloc | 58.1 | 27.5 | 307.3 | 1076.8 | 9.4 | 6.7 | 6.3 | [52.0, 487.7] |
| naviloc_yaw | 49.4 | 27.6 | 267.5 | 642.9 | 9.5 | 7.0 | 2.9 | [52.5, 318.5] |

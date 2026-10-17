Config: `{"feats": "feats/ft/merged/baseline_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 632.1 | 44.2 | 3094.5 | 4963.6 | 45.6 | 35.8 | 100.0 | [2948.4, 3169.0] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 213.6 | 30.9 | 1403.2 | 1848.0 | 22.4 | 18.3 | 20.1 | [1006.6, 1461.9] |
| pf_topk | 92.7 | 29.9 | 445.6 | 1691.0 | 19.2 | 12.4 | 21.3 | [228.3, 907.0] |
| mh_ekf | 51.7 | 26.8 | 76.7 | 1789.0 | 8.4 | 4.3 | 40.8 | [53.4, 238.8] |
| naviloc | 58.1 | 27.5 | 307.3 | 1076.8 | 9.4 | 6.7 | 6.3 | [52.0, 487.7] |
| naviloc_yaw | 49.4 | 27.6 | 267.5 | 642.9 | 9.5 | 7.0 | 2.9 | [52.5, 318.5] |

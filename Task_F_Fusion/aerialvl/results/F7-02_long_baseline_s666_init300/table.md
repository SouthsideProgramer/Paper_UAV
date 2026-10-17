Config: `{"feats": "feats/ft/merged/baseline_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s666_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 739.3 | 48.2 | 3404.1 | 5043.0 | 48.9 | 39.0 | 100.0 | [3193.2, 3588.9] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 197.6 | 31.0 | 1128.7 | 1680.3 | 27.8 | 22.1 | 22.4 | [721.9, 1413.4] |
| pf_topk | 129.5 | 32.0 | 807.5 | 1512.0 | 24.6 | 17.3 | 25.3 | [505.2, 963.7] |
| mh_ekf | 65.6 | 27.7 | 175.3 | 1801.2 | 10.7 | 6.0 | 42.0 | [63.4, 683.8] |
| naviloc | 95.2 | 28.8 | 550.1 | 2358.7 | 13.5 | 8.2 | 8.6 | [68.2, 887.2] |
| naviloc_yaw | 77.4 | 28.8 | 416.5 | 1564.9 | 13.7 | 8.5 | 4.6 | [70.3, 584.9] |

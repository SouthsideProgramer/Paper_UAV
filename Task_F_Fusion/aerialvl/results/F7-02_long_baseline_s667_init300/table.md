Config: `{"feats": "feats/ft/merged/baseline_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 823.3 | 55.6 | 3515.5 | 5030.2 | 53.1 | 44.2 | 100.0 | [3382.8, 3646.6] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 261.5 | 35.8 | 1339.5 | 1839.8 | 32.2 | 27.9 | 25.9 | [1124.6, 1516.0] |
| pf_topk | 124.4 | 33.4 | 711.0 | 1506.1 | 26.1 | 18.3 | 26.4 | [509.6, 906.1] |
| mh_ekf | 67.2 | 29.6 | 175.6 | 1687.2 | 11.1 | 5.9 | 45.4 | [62.3, 666.0] |
| naviloc | 107.1 | 33.6 | 555.5 | 2907.8 | 21.0 | 12.0 | 8.6 | [287.9, 839.0] |
| naviloc_yaw | 74.0 | 33.8 | 413.4 | 978.0 | 21.5 | 12.5 | 5.2 | [211.5, 516.1] |

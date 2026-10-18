Config: `{"feats": "feats/ft/merged/baseline_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 823.3 | 55.6 | 3515.5 | 5030.2 | 53.1 | 44.2 | 100.0 | [3382.8, 3646.6] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 35.6 | 28.5 | 60.1 | 404.0 | 8.4 | 4.0 | 0.0 | [53.0, 169.9] |
| pf_topk | 28.3 | 27.1 | 50.2 | 190.7 | 5.2 | 0.2 | 0.0 | [48.0, 52.9] |
| mh_ekf | 28.3 | 27.6 | 49.4 | 97.1 | 4.6 | 0.0 | 0.0 | [47.3, 52.2] |
| naviloc | 107.1 | 33.6 | 555.5 | 2907.8 | 21.0 | 12.0 | 8.6 | [287.9, 839.0] |
| naviloc_yaw | 74.0 | 33.8 | 413.4 | 978.0 | 21.5 | 12.5 | 5.2 | [211.5, 516.1] |

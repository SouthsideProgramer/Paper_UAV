Config: `{"feats": "feats/ft/merged/baseline_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 739.3 | 48.2 | 3404.1 | 5043.0 | 48.9 | 39.0 | 100.0 | [3193.2, 3588.9] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 29.0 | 26.4 | 52.8 | 231.7 | 6.6 | 1.3 | 0.0 | [50.2, 55.1] |
| pf_topk | 26.6 | 25.7 | 47.4 | 99.1 | 3.5 | 0.0 | 0.0 | [45.3, 49.5] |
| mh_ekf | 26.9 | 26.0 | 48.2 | 127.3 | 3.8 | 0.0 | 0.0 | [46.1, 50.2] |
| naviloc | 95.2 | 28.8 | 550.1 | 2358.7 | 13.5 | 8.2 | 8.6 | [68.2, 887.2] |
| naviloc_yaw | 77.4 | 28.8 | 416.5 | 1564.9 | 13.7 | 8.5 | 4.6 | [70.3, 584.9] |

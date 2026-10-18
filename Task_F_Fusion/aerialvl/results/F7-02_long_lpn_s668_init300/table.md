Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s668_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 586.2 | 42.9 | 3347.5 | 4928.9 | 43.8 | 32.3 | 100.0 | [3028.3, 3483.9] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 165.3 | 31.7 | 983.9 | 1711.9 | 25.2 | 19.4 | 17.2 | [621.2, 1159.0] |
| pf_topk | 85.4 | 30.7 | 375.1 | 1522.1 | 20.4 | 11.6 | 19.0 | [286.9, 773.2] |
| mh_ekf | 55.3 | 27.5 | 69.9 | 1637.0 | 9.2 | 4.1 | 39.1 | [55.9, 320.1] |
| naviloc | 135.8 | 29.3 | 1100.6 | 2684.7 | 14.7 | 10.3 | 9.8 | [482.8, 1245.7] |
| naviloc_yaw | 121.0 | 29.2 | 1071.7 | 1810.3 | 14.6 | 10.4 | 6.9 | [171.0, 1427.7] |

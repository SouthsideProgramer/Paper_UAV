Config: `{"feats": "feats/ft/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 522.4 | 38.2 | 2878.1 | 4589.3 | 39.9 | 29.6 | 100.0 | [2670.7, 2995.9] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 199.0 | 27.4 | 1191.2 | 1842.9 | 23.6 | 21.2 | 19.0 | [927.4, 1279.6] |
| pf_topk | 86.9 | 27.6 | 534.9 | 1564.3 | 14.2 | 8.5 | 20.7 | [105.1, 1086.7] |
| mh_ekf | 42.9 | 24.9 | 52.6 | 1816.1 | 5.8 | 2.8 | 41.4 | [48.0, 67.2] |
| naviloc | 65.9 | 25.7 | 69.4 | 2464.1 | 7.8 | 4.6 | 4.6 | [48.9, 444.6] |
| naviloc_yaw | 51.6 | 25.6 | 185.8 | 1058.7 | 8.2 | 5.3 | 1.7 | [49.5, 308.4] |

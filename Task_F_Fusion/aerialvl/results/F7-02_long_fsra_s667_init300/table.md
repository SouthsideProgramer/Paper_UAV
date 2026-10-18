Config: `{"feats": "feats/ft/merged/fsra_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s667_init300", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 657.1 | 46.4 | 3210.8 | 4961.4 | 47.3 | 36.6 | 100.0 | [3060.2, 3296.3] |
| dead_reckoning | 390.2 | 361.4 | 759.5 | 1040.9 | 99.0 | 96.1 | 31.0 | [681.6, 879.3] |
| ekf_gated | 150.9 | 31.6 | 915.9 | 1847.1 | 23.6 | 17.7 | 20.1 | [697.8, 967.3] |
| pf_topk | 106.2 | 30.9 | 721.9 | 1510.8 | 20.8 | 12.4 | 25.3 | [274.2, 970.4] |
| mh_ekf | 58.2 | 28.9 | 113.1 | 1789.1 | 11.3 | 5.2 | 45.4 | [58.3, 665.9] |
| naviloc | 88.7 | 29.3 | 583.5 | 2954.2 | 13.1 | 6.7 | 5.2 | [60.5, 986.1] |
| naviloc_yaw | 73.8 | 29.9 | 692.7 | 1110.2 | 13.4 | 6.7 | 5.2 | [60.9, 742.5] |

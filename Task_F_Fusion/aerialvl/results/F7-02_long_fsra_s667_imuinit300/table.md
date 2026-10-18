Config: `{"feats": "feats/ft/merged/fsra_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s667_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 657.1 | 46.4 | 3210.8 | 4961.4 | 47.3 | 36.6 | 100.0 | [3060.2, 3296.3] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 206.1 | 38.6 | 1053.7 | 6067.6 | 36.0 | 20.5 | 27.6 | [748.7, 1421.7] |
| pf_topk | 520.9 | 253.0 | 1884.1 | 4888.4 | 78.4 | 64.9 | 83.9 | [1646.9, 2082.1] |
| mh_ekf | 85.5 | 34.3 | 365.6 | 3759.3 | 25.6 | 11.0 | 50.0 | [198.0, 636.6] |
| naviloc | 387.1 | 219.6 | 1363.5 | 3435.9 | 85.0 | 70.2 | 73.6 | [1142.0, 1688.5] |
| naviloc_yaw | 404.4 | 269.9 | 1247.2 | 3452.2 | 88.0 | 75.8 | 76.4 | [1139.3, 1378.2] |

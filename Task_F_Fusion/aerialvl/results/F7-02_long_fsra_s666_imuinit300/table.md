Config: `{"feats": "feats/ft/merged/fsra_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 718.0 | 49.2 | 3392.6 | 4937.6 | 49.6 | 39.5 | 100.0 | [3323.1, 3499.1] |
| dead_reckoning | 700.7 | 537.5 | 1881.2 | 4357.1 | 98.9 | 97.0 | 93.7 | [1692.7, 2034.9] |
| ekf_gated | 271.8 | 35.6 | 1573.6 | 5696.6 | 33.9 | 22.0 | 27.6 | [1235.9, 1803.1] |
| pf_topk | 580.7 | 286.5 | 2097.8 | 7179.2 | 78.4 | 65.8 | 82.8 | [1879.7, 2370.1] |
| mh_ekf | 153.0 | 33.5 | 959.1 | 4078.5 | 29.1 | 15.7 | 48.9 | [524.8, 1342.3] |
| naviloc | 402.2 | 207.5 | 1533.4 | 4648.3 | 84.9 | 70.4 | 69.0 | [1264.4, 1819.4] |
| naviloc_yaw | 393.4 | 265.4 | 1249.8 | 3421.4 | 87.8 | 75.3 | 75.3 | [1109.8, 1358.3] |

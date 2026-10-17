Config: `{"feats": "feats/ft/merged/fsra_s666.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s666_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 718.0 | 49.2 | 3392.6 | 4937.6 | 49.6 | 39.5 | 100.0 | [3323.1, 3499.1] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 87.4 | 30.3 | 225.5 | 3723.4 | 21.7 | 8.4 | 6.9 | [108.0, 539.3] |
| pf_topk | 184.9 | 46.9 | 811.8 | 4519.7 | 47.8 | 31.3 | 37.4 | [657.1, 1004.8] |
| mh_ekf | 86.4 | 30.4 | 246.8 | 3424.4 | 22.3 | 9.5 | 9.8 | [135.8, 475.9] |
| naviloc | 402.2 | 207.5 | 1533.4 | 4648.3 | 84.9 | 70.4 | 69.0 | [1264.4, 1819.4] |
| naviloc_yaw | 393.4 | 265.4 | 1249.8 | 3421.4 | 87.8 | 75.3 | 75.3 | [1109.8, 1358.3] |

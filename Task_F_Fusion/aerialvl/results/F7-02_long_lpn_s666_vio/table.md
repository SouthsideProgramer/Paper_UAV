Config: `{"feats": "feats/ft/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s666_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 620.7 | 43.3 | 3237.3 | 4979.8 | 44.0 | 33.7 | 98.3 | [3015.6, 3411.0] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 32.2 | 28.2 | 58.5 | 315.3 | 7.4 | 1.3 | 0.0 | [51.8, 70.5] |
| pf_topk | 28.6 | 27.5 | 49.7 | 100.0 | 4.9 | 0.0 | 0.0 | [46.7, 52.6] |
| mh_ekf | 28.3 | 27.2 | 48.8 | 93.5 | 4.3 | 0.0 | 0.0 | [46.8, 51.6] |
| naviloc | 56.4 | 29.9 | 155.5 | 1476.8 | 10.9 | 5.5 | 1.7 | [56.7, 278.9] |
| naviloc_yaw | 51.1 | 30.0 | 124.3 | 994.6 | 11.3 | 5.4 | 1.7 | [57.4, 248.2] |

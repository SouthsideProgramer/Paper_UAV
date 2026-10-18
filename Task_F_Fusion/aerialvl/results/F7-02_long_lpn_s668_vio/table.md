Config: `{"feats": "feats/ft/merged/lpn_s668.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s668_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 586.2 | 42.9 | 3347.5 | 4928.9 | 43.8 | 32.3 | 100.0 | [3028.3, 3483.9] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 31.9 | 26.6 | 55.7 | 295.2 | 8.0 | 2.3 | 0.0 | [51.8, 65.3] |
| pf_topk | 28.4 | 26.6 | 50.6 | 100.2 | 5.4 | 0.0 | 0.0 | [47.8, 53.8] |
| mh_ekf | 28.2 | 26.7 | 49.0 | 149.6 | 4.4 | 0.2 | 0.0 | [46.8, 52.1] |
| naviloc | 135.8 | 29.3 | 1100.6 | 2684.7 | 14.7 | 10.3 | 9.8 | [482.8, 1245.7] |
| naviloc_yaw | 121.0 | 29.2 | 1071.7 | 1810.3 | 14.6 | 10.4 | 6.9 | [171.0, 1427.7] |

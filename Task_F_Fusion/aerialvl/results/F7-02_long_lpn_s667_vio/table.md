Config: `{"feats": "feats/ft/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_lpn_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 522.4 | 38.2 | 2878.1 | 4589.3 | 39.9 | 29.6 | 100.0 | [2670.7, 2995.9] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 30.8 | 23.9 | 54.0 | 268.2 | 6.0 | 3.6 | 0.0 | [47.9, 101.3] |
| pf_topk | 26.0 | 24.0 | 47.6 | 109.6 | 4.1 | 0.1 | 0.0 | [44.7, 52.6] |
| mh_ekf | 25.8 | 24.2 | 46.4 | 104.3 | 3.0 | 0.1 | 0.0 | [44.3, 48.8] |
| naviloc | 65.9 | 25.7 | 69.4 | 2464.1 | 7.8 | 4.6 | 4.6 | [48.9, 444.6] |
| naviloc_yaw | 51.6 | 25.6 | 185.8 | 1058.7 | 8.2 | 5.3 | 1.7 | [49.5, 308.4] |

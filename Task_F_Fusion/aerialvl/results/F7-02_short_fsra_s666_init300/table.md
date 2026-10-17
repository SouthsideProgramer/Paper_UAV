Config: `{"feats": "feats/ft/fsra_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s666_init300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 387.4 | 37.0 | 2466.3 | 4384.7 | 33.6 | 26.7 | 100.0 | [2441.1, 2660.8] |
| dead_reckoning | 380.7 | 351.3 | 753.2 | 1025.3 | 99.4 | 97.0 | 32.2 | [690.9, 830.9] |
| ekf_gated | 70.7 | 26.9 | 439.8 | 905.3 | 12.4 | 8.6 | 4.8 | [102.3, 782.0] |
| pf_topk | 61.3 | 27.9 | 356.4 | 1347.0 | 9.9 | 6.3 | 13.0 | [60.2, 439.8] |
| mh_ekf | 44.9 | 26.2 | 47.2 | 1378.5 | 4.1 | 3.0 | 32.6 | [42.8, 57.4] |
| naviloc | 26.6 | 26.2 | 43.7 | 88.9 | 2.3 | 0.0 | 0.0 | [42.5, 45.0] |
| naviloc_yaw | 26.6 | 26.1 | 43.4 | 88.9 | 2.1 | 0.0 | 0.0 | [42.2, 44.6] |

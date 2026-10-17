Config: `{"feats": "feats/ft/merged/baseline_s668.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_baseline_s668_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/baseline_s668.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 632.1 | 44.2 | 3094.5 | 4963.6 | 45.6 | 35.8 | 100.0 | [2948.4, 3169.0] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 130.0 | 32.7 | 604.3 | 3689.4 | 25.4 | 12.0 | 13.2 | [274.9, 1142.9] |
| pf_topk | 178.8 | 46.7 | 828.5 | 3811.1 | 47.3 | 30.8 | 33.9 | [616.8, 979.3] |
| mh_ekf | 74.5 | 31.3 | 167.1 | 3279.6 | 21.3 | 7.7 | 7.5 | [105.4, 318.5] |
| naviloc | 364.8 | 200.4 | 1294.0 | 3468.2 | 84.2 | 68.8 | 73.0 | [1132.9, 1418.2] |
| naviloc_yaw | 377.9 | 257.1 | 1172.2 | 3345.6 | 87.3 | 74.1 | 77.6 | [1042.3, 1278.7] |

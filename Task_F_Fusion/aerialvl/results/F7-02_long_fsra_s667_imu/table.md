Config: `{"feats": "feats/ft/merged/fsra_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s667_imu", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 657.1 | 46.4 | 3210.8 | 4961.4 | 47.3 | 36.6 | 100.0 | [3060.2, 3296.3] |
| dead_reckoning | 496.7 | 278.1 | 1734.1 | 4474.0 | 80.7 | 70.9 | 89.7 | [1580.1, 1892.1] |
| ekf_gated | 77.9 | 33.9 | 205.7 | 4551.5 | 26.2 | 9.0 | 9.8 | [125.8, 383.8] |
| pf_topk | 156.2 | 47.7 | 742.7 | 2476.8 | 47.9 | 30.4 | 35.6 | [616.2, 849.9] |
| mh_ekf | 67.4 | 32.5 | 161.9 | 2380.1 | 21.7 | 7.5 | 8.6 | [105.4, 299.4] |
| naviloc | 387.1 | 219.6 | 1363.5 | 3435.9 | 85.0 | 70.2 | 73.6 | [1142.0, 1688.5] |
| naviloc_yaw | 404.4 | 269.9 | 1247.2 | 3452.2 | 88.0 | 75.8 | 76.4 | [1139.3, 1378.2] |

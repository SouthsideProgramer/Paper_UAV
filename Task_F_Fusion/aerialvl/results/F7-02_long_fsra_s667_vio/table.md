Config: `{"feats": "feats/ft/merged/fsra_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_long_fsra_s667_vio", "cfg": "", "calib": "val", "calib_from": "feats/ft/fsra_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 657.1 | 46.4 | 3210.8 | 4961.4 | 47.3 | 36.6 | 100.0 | [3060.2, 3296.3] |
| dead_reckoning | 37.3 | 28.6 | 95.2 | 198.0 | 25.3 | 4.3 | 0.0 | [86.1, 107.4] |
| ekf_gated | 31.0 | 27.5 | 57.6 | 211.0 | 8.7 | 2.3 | 0.0 | [53.3, 62.5] |
| pf_topk | 28.8 | 27.1 | 51.4 | 167.1 | 6.0 | 0.5 | 0.0 | [49.0, 54.0] |
| mh_ekf | 28.7 | 27.4 | 50.7 | 100.4 | 5.6 | 0.0 | 0.0 | [48.9, 52.0] |
| naviloc | 88.7 | 29.3 | 583.5 | 2954.2 | 13.1 | 6.7 | 5.2 | [60.5, 986.1] |
| naviloc_yaw | 73.8 | 29.9 | 692.7 | 1110.2 | 13.4 | 6.7 | 5.2 | [60.9, 742.5] |

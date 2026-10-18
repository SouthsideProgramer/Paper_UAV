Config: `{"feats": "feats/ft/fsra_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s666_imu", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 387.4 | 37.0 | 2466.3 | 4384.7 | 33.6 | 26.7 | 100.0 | [2441.1, 2660.8] |
| dead_reckoning | 535.2 | 314.4 | 1841.9 | 4268.9 | 80.9 | 72.1 | 90.9 | [1716.3, 2000.1] |
| ekf_gated | 47.3 | 28.4 | 89.5 | 6258.8 | 10.7 | 4.7 | 1.7 | [64.1, 110.4] |
| pf_topk | 111.0 | 32.6 | 571.6 | 2139.9 | 29.3 | 19.4 | 31.3 | [480.1, 671.0] |
| mh_ekf | 31.3 | 27.8 | 53.0 | 716.7 | 6.4 | 1.7 | 0.9 | [50.7, 56.1] |
| naviloc | 354.8 | 203.4 | 1270.8 | 4188.1 | 82.5 | 68.4 | 74.3 | [1117.0, 1414.2] |
| naviloc_yaw | 368.4 | 258.2 | 1095.1 | 3184.0 | 85.5 | 74.0 | 77.8 | [1031.0, 1175.8] |

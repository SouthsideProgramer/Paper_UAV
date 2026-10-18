Config: `{"feats": "feats/ft/fsra_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf,naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F7-02_short_fsra_s666_imuinit300", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 387.4 | 37.0 | 2466.3 | 4384.7 | 33.6 | 26.7 | 100.0 | [2441.1, 2660.8] |
| dead_reckoning | 709.8 | 543.0 | 1922.9 | 4303.1 | 99.5 | 97.4 | 93.9 | [1795.4, 2079.0] |
| ekf_gated | 104.2 | 29.3 | 413.8 | 5917.0 | 15.3 | 9.5 | 7.4 | [138.7, 810.8] |
| pf_topk | 520.6 | 227.5 | 1977.8 | 6197.5 | 74.0 | 61.7 | 78.3 | [1783.7, 2170.3] |
| mh_ekf | 61.8 | 28.3 | 70.9 | 5372.1 | 9.2 | 4.3 | 33.5 | [57.6, 141.8] |
| naviloc | 354.8 | 203.4 | 1270.8 | 4188.1 | 82.5 | 68.4 | 74.3 | [1117.0, 1414.2] |
| naviloc_yaw | 368.4 | 258.2 | 1095.1 | 3184.0 | 85.5 | 74.0 | 77.8 | [1031.0, 1175.8] |

Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 1, "init_err": 10.0, "K": 10, "methods": "retrieval_top1,dead_reckoning,mh_ekf,naviloc,naviloc_causal", "seed": 0, "workers": 11, "n_boot": 100, "tag": "dev_nl_lpn_val_vio", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1262.7 | 887.4 | 3556.2 | 4704.1 | 77.6 | 74.5 | 100.0 | [2880.9, 3762.6] |
| dead_reckoning | 33.7 | 30.7 | 76.4 | 95.7 | 19.6 | 0.0 | 0.0 | [52.7, 89.5] |
| mh_ekf | 24.2 | 22.3 | 45.6 | 96.6 | 2.4 | 0.0 | 0.0 | [41.3, 48.8] |
| naviloc | 392.8 | 259.2 | 1202.1 | 1662.3 | 82.7 | 77.1 | 53.8 | [1088.7, 1305.7] |
| naviloc_causal | 441.0 | 282.7 | 1352.9 | 3590.0 | 65.7 | 63.4 | 84.6 | [1007.3, 1608.6] |

Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 1, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw", "seed": 0, "workers": 11, "n_boot": 50, "tag": "dev_nl_tmp", "cfg": "", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 392.8 | 259.2 | 1202.1 | 1662.3 | 82.7 | 77.1 | 53.8 | [1098.0, 1308.8] |
| naviloc_yaw | 209.0 | 210.7 | 479.7 | 511.6 | 87.1 | 82.3 | 7.7 | [278.5, 487.1] |

Config: `{"feats": "feats/lpn_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 2, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 10, "n_boot": 50, "tag": "sweep_tmp", "cfg": "{\"n_reacq\":60}", "calib": "val"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 513.4 | 116.5 | 2003.2 | 4414.5 | 59.0 | 52.9 | 80.8 | [1343.0, 2399.2] |

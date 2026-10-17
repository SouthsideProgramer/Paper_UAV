Config: `{"feats": "feats/lpn_s667.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortzs_bestchild_lpn_s667_imu", "cfg": "{\"mh_lost_rule\": \"best_child\"}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 76.9 | 29.6 | 79.8 | 7581.9 | 8.9 | 4.1 | 3.0 | [60.9, 117.5] |

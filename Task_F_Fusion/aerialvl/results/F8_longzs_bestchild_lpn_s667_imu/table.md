Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longzs_bestchild_lpn_s667_imu", "cfg": "{\"mh_lost_rule\": \"best_child\"}", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 80.3 | 32.1 | 248.3 | 3643.8 | 23.8 | 11.8 | 12.1 | [186.3, 428.7] |

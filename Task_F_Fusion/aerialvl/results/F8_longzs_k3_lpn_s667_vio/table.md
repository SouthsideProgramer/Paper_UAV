Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longzs_k3_lpn_s667_vio", "cfg": "{\"mh_topk\": 3}", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 28.0 | 25.8 | 47.9 | 185.8 | 4.2 | 1.3 | 0.0 | [45.0, 52.6] |

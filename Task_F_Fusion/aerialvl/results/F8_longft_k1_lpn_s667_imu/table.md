Config: `{"feats": "feats/ft/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_k1_lpn_s667_imu", "cfg": "{\"mh_topk\": 1}", "calib": "val", "calib_from": "feats/ft/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 60.8 | 27.5 | 204.9 | 2240.8 | 17.3 | 7.6 | 9.2 | [91.6, 363.4] |

Config: `{"feats": "feats/ft/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_gateinf_lpn_s667_imu", "cfg": "{\"mh_gate\": 1e12}", "calib": "val", "calib_from": "feats/ft/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 39.3 | 27.0 | 68.3 | 1673.6 | 13.0 | 2.9 | 3.4 | [62.2, 89.1] |

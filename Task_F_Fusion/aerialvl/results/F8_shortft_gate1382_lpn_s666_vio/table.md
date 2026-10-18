Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_gate1382_lpn_s666_vio", "cfg": "{\"mh_gate\": 13.82}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 24.1 | 24.4 | 38.9 | 63.4 | 0.3 | 0.0 | 0.0 | [37.4, 39.7] |

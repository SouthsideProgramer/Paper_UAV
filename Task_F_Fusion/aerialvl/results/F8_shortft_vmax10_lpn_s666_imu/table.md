Config: `{"feats": "feats/ft/lpn_s666.npz", "split": "test", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_shortft_vmax10_lpn_s666_imu", "cfg": "{\"v_max\": 10.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 33.7 | 29.4 | 54.7 | 1568.1 | 7.3 | 1.4 | 2.2 | [51.5, 58.3] |

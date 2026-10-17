Config: `{"feats": "feats/ft/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_noreacq_lpn_s666_vio", "cfg": "{\"n_reacq\": 1000000000}", "calib": "val", "calib_from": "feats/ft/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 28.3 | 27.2 | 48.8 | 93.5 | 4.3 | 0.0 | 0.0 | [47.1, 51.3] |

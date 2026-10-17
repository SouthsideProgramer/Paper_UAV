Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 10.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longzs_noreacq_lpn_s667_vio", "cfg": "{\"n_reacq\": 1000000000}", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 29.3 | 26.6 | 51.9 | 174.8 | 5.5 | 1.5 | 0.0 | [47.2, 65.7] |

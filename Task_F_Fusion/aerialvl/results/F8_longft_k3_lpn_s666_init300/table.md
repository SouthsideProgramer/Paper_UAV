Config: `{"feats": "feats/ft/merged/lpn_s666.npz", "split": "test_long", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longft_k3_lpn_s666_init300", "cfg": "{\"mh_topk\": 3}", "calib": "val", "calib_from": "feats/ft/lpn_s666.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 55.1 | 29.1 | 88.0 | 1541.6 | 9.5 | 4.5 | 41.4 | [62.3, 124.0] |

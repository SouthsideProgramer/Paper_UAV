Config: `{"feats": "feats/merged/lpn_s667.npz", "split": "test_long", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 60.0, "n_noise": 3, "init_err": 300.0, "K": 10, "methods": "mh_ekf", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_longzs_vmax10_lpn_s667_imuinit300", "cfg": "{\"v_max\": 10.0}", "calib": "val", "calib_from": "feats/lpn_s667.npz"}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| mh_ekf | 173.2 | 36.5 | 906.8 | 5516.5 | 33.8 | 22.2 | 61.5 | [727.2, 1086.7] |

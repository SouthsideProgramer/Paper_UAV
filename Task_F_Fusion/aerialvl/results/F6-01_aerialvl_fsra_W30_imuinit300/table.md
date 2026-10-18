Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "imu", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 300.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W30_imuinit300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 595.9 | 459.3 | 1589.7 | 3688.6 | 93.4 | 87.4 | 89.2 | [1319.8, 1867.9] |
| naviloc_yaw | 505.2 | 374.8 | 1410.0 | 3874.2 | 95.5 | 89.0 | 76.9 | [1148.7, 1578.7] |
| naviloc_causal | 661.5 | 469.0 | 1856.9 | 3690.4 | 87.1 | 78.6 | 100.0 | [1592.8, 2146.7] |
| mh_ekf | 603.4 | 189.9 | 2205.2 | 6888.9 | 66.2 | 59.4 | 70.8 | [1598.5, 2724.1] |

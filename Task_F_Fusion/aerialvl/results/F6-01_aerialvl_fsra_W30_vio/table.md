Config: `{"feats": "feats/fsra_s666.npz", "split": "val", "motion": "vio", "imu_grade": "consumer", "T": 240.0, "win_step": 20.0, "n_noise": 5, "init_err": 10.0, "K": 10, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_aerialvl_fsra_W30_vio", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}", "calib": "val", "calib_from": ""}`

| Method | mean | p50 | p95 | max | GFR@50 | GFR@100 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|
| naviloc | 369.3 | 242.9 | 1175.4 | 1674.0 | 84.1 | 76.5 | 50.8 | [1129.6, 1205.4] |
| naviloc_yaw | 171.3 | 161.9 | 351.9 | 402.1 | 87.2 | 78.5 | 0.0 | [302.3, 364.7] |
| naviloc_causal | 472.8 | 295.9 | 1354.8 | 3086.8 | 68.5 | 63.7 | 84.6 | [1273.2, 1587.1] |
| mh_ekf | 32.6 | 22.8 | 88.3 | 168.9 | 17.9 | 2.4 | 0.0 | [84.2, 96.5] |

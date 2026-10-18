Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-12_cfg10a_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 7.4 | 5.7 | 14.1 | 18.2 | 151.5 | 0.4 | 0.1 | 0.0 | 0.0 | [16.8, 20.1] |
| mh_ekf | 7.1 | 5.9 | 13.0 | 16.0 | 134.0 | 0.1 | 0.1 | 0.0 | 0.0 | [14.8, 17.6] |

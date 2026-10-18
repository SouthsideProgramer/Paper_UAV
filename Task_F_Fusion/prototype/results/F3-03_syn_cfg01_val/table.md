Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-03_syn_cfg01_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 3.8 | 3.2 | 6.7 | 8.3 | 41.1 | 0.0 | 0.0 | 0.0 | 0.0 | [7.8, 9.0] |
| mh_ekf | 3.9 | 3.4 | 7.0 | 8.4 | 30.3 | 0.0 | 0.0 | 0.0 | 0.0 | [7.9, 9.0] |

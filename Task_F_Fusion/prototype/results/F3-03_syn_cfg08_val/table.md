Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.9, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-03_syn_cfg08_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 7.0 | 3.4 | 10.4 | 17.1 | 290.5 | 2.1 | 1.0 | 0.0 | 0.0 | [14.0, 20.0] |
| mh_ekf | 4.4 | 3.4 | 8.1 | 10.4 | 101.5 | 0.3 | 0.1 | 0.0 | 0.0 | [9.3, 12.0] |

Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,ekf_dispgate", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F2-11_fsra_thr100_val", "cfg": "{\"disp_thr\": 100}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 3.8 | 3.2 | 6.7 | 8.3 | 41.1 | 0.0 | 0.0 | 0.0 | 0.0 | [7.7, 8.9] |
| ekf_dispgate | 7.7 | 6.4 | 14.5 | 18.0 | 43.5 | 0.0 | 0.0 | 0.0 | 0.0 | [16.4, 19.4] |

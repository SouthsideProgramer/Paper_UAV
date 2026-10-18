Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "baseline_vits_19", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,ekf_dispgate", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F2-11_baseline_vits_19_thr200_val", "cfg": "{\"disp_thr\": 200}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 14.0 | 8.3 | 27.0 | 49.3 | 203.5 | 4.9 | 1.3 | 0.0 | 0.0 | [35.0, 72.1] |
| ekf_dispgate | 11.0 | 9.3 | 20.5 | 25.4 | 67.2 | 0.3 | 0.0 | 0.0 | 0.0 | [23.2, 27.2] |

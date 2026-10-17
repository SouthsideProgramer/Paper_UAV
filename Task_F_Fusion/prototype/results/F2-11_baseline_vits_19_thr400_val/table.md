Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "baseline_vits_19", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,ekf_dispgate", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F2-11_baseline_vits_19_thr400_val", "cfg": "{\"disp_thr\": 400}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 14.0 | 8.3 | 27.0 | 49.3 | 203.5 | 4.9 | 1.3 | 0.0 | 0.0 | [35.0, 72.1] |
| ekf_dispgate | 10.1 | 8.5 | 18.9 | 23.7 | 66.6 | 0.2 | 0.0 | 0.0 | 0.0 | [22.0, 26.1] |

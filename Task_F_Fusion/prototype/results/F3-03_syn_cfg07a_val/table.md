Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "baseline_vits_19", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-03_syn_cfg07a_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 14.0 | 8.3 | 27.0 | 49.3 | 203.5 | 4.9 | 1.3 | 0.0 | 0.0 | [34.8, 72.3] |
| mh_ekf | 6.2 | 5.6 | 11.1 | 13.6 | 40.1 | 0.0 | 0.0 | 0.0 | 0.0 | [12.5, 14.6] |

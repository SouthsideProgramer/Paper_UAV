Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "vits_82", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-12_cfg07b_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 2.9 | 2.5 | 5.2 | 6.3 | 47.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.9] |
| pf_topk | 2.9 | 2.5 | 5.2 | 6.4 | 24.1 | 0.0 | 0.0 | 0.0 | 0.0 | [5.9, 7.3] |
| mh_ekf | 3.0 | 2.7 | 5.4 | 6.5 | 29.1 | 0.0 | 0.0 | 0.0 | 0.0 | [6.1, 7.2] |

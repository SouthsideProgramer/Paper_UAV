Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-12_cfg04_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 23.9 | 3.4 | 8.9 | 41.7 | 1183.2 | 4.9 | 4.3 | 1.4 | 4.0 | [10.6, 426.9] |
| pf_topk | 7.9 | 5.6 | 13.3 | 17.3 | 735.2 | 0.5 | 0.4 | 0.0 | 6.0 | [14.6, 22.9] |
| mh_ekf | 5.5 | 3.4 | 7.1 | 8.7 | 904.1 | 0.5 | 0.4 | 0.1 | 18.0 | [8.2, 9.3] |

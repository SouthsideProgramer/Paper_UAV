Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-02_syn_cfg10b_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 32.2 | 6.1 | 17.9 | 34.8 | 2016.5 | 4.4 | 3.8 | 1.8 | 6.0 | [21.1, 373.6] |
| mh_ekf | 8.6 | 5.9 | 13.3 | 16.7 | 903.7 | 0.7 | 0.5 | 0.1 | 18.0 | [15.4, 18.6] |

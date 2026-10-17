Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 40, "T": 1800.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,ekf_topk_nn,pf_topk", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-09_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 433.9 | 9.8 | 1937.8 | 3536.1 | 7064.8 | 31.0 | 19.8 | 12.5 | 100.0 | [3332.3, 3739.4] |
| dead_reckoning | 67.9 | 50.0 | 147.4 | 189.7 | 327.7 | 50.0 | 22.5 | 0.0 | 0.0 | [156.6, 221.4] |
| ekf_gated | 3.3 | 3.0 | 5.8 | 6.7 | 40.9 | 0.0 | 0.0 | 0.0 | 0.0 | [6.5, 7.1] |
| ekf_topk_nn | 3.5 | 3.1 | 6.1 | 7.2 | 35.7 | 0.0 | 0.0 | 0.0 | 0.0 | [6.9, 7.5] |
| pf_topk | 3.1 | 2.8 | 5.4 | 6.4 | 26.4 | 0.0 | 0.0 | 0.0 | 0.0 | [6.2, 6.7] |

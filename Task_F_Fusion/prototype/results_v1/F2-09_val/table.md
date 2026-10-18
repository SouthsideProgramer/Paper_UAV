Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 40, "T": 1800.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,ekf_topk_nn,pf_topk", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-09_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 433.9 | 9.8 | 1937.8 | 3536.1 | 7064.8 | 31.0 | 19.8 | 12.5 | 100.0 | [3332.3, 3739.4] |
| dead_reckoning | 18.0 | 15.7 | 32.2 | 36.7 | 96.2 | 1.2 | 0.0 | 0.0 | 0.0 | [32.8, 43.9] |
| ekf_gated | 2.4 | 2.1 | 4.3 | 5.3 | 40.9 | 0.0 | 0.0 | 0.0 | 0.0 | [5.0, 5.5] |
| ekf_topk_nn | 2.6 | 2.2 | 4.6 | 5.6 | 35.7 | 0.0 | 0.0 | 0.0 | 0.0 | [5.3, 6.1] |
| pf_topk | 2.3 | 2.0 | 4.2 | 5.1 | 26.3 | 0.0 | 0.0 | 0.0 | 0.0 | [4.8, 5.5] |

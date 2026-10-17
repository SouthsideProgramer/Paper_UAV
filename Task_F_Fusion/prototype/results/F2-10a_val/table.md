Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,ekf_topk_nn,pf_topk", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-10a_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 426.6 | 9.8 | 1848.0 | 3415.5 | 6972.1 | 31.4 | 20.0 | 12.5 | 100.0 | [3208.7, 3623.4] |
| dead_reckoning | 370.4 | 249.3 | 886.6 | 1186.5 | 3907.1 | 84.0 | 73.2 | 24.8 | 63.0 | [986.1, 1423.2] |
| ekf_gated | 7.4 | 5.7 | 14.1 | 18.2 | 151.5 | 0.4 | 0.1 | 0.0 | 0.0 | [16.8, 20.1] |
| ekf_topk_nn | 13.2 | 7.4 | 26.2 | 38.4 | 563.7 | 1.8 | 0.9 | 0.1 | 1.0 | [30.4, 45.2] |
| pf_topk | 30.9 | 8.4 | 50.2 | 182.1 | 793.9 | 10.0 | 7.3 | 0.6 | 2.0 | [64.2, 272.9] |

Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-03_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 426.6 | 9.8 | 1848.0 | 3415.5 | 6972.1 | 31.4 | 20.0 | 12.5 | 100.0 | [3208.7, 3623.4] |
| dead_reckoning | 370.4 | 249.3 | 886.6 | 1186.5 | 3907.1 | 84.0 | 73.2 | 24.8 | 63.0 | [986.1, 1423.2] |
| ekf_naive | 465.1 | 331.5 | 1046.8 | 1386.8 | 4068.5 | 91.9 | 84.5 | 32.8 | 100.0 | [1280.3, 1477.0] |
| ekf_gated | 7.4 | 5.7 | 14.1 | 18.2 | 151.5 | 0.4 | 0.1 | 0.0 | 0.0 | [16.8, 20.1] |
| ekf_disp_gated | 25.6 | 20.8 | 49.2 | 61.5 | 332.6 | 9.6 | 0.8 | 0.0 | 0.0 | [56.5, 68.6] |
| ekf_topk_nn | 13.2 | 7.4 | 26.2 | 38.4 | 563.7 | 1.8 | 0.9 | 0.1 | 1.0 | [30.4, 45.2] |

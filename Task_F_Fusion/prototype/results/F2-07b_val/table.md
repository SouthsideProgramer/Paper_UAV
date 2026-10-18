Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "vits_82", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-07b_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 222.8 | 8.8 | 116.7 | 1951.5 | 7129.2 | 16.3 | 10.7 | 6.4 | 100.0 | [1580.8, 2276.3] |
| dead_reckoning | 19.2 | 17.0 | 33.8 | 40.4 | 85.6 | 2.1 | 0.0 | 0.0 | 0.0 | [35.3, 47.6] |
| ekf_naive | 228.0 | 157.3 | 499.9 | 667.1 | 3736.4 | 82.6 | 66.4 | 10.0 | 67.0 | [569.3, 752.5] |
| ekf_gated | 2.9 | 2.5 | 5.2 | 6.3 | 47.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 6.9] |
| ekf_disp_gated | 9.5 | 8.3 | 17.3 | 21.6 | 46.7 | 0.0 | 0.0 | 0.0 | 0.0 | [18.7, 24.7] |
| ekf_topk_nn | 3.6 | 3.0 | 6.4 | 8.5 | 38.5 | 0.0 | 0.0 | 0.0 | 0.0 | [7.4, 9.8] |
| pf_topk | 2.9 | 2.5 | 5.2 | 6.4 | 24.4 | 0.0 | 0.0 | 0.0 | 0.0 | [5.8, 7.0] |

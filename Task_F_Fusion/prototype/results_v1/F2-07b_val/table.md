Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "vits_82", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F2-07b_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 222.8 | 8.8 | 116.7 | 1951.5 | 7129.2 | 16.3 | 10.7 | 6.4 | 100.0 | [1580.8, 2276.3] |
| dead_reckoning | 18.2 | 16.0 | 32.3 | 39.4 | 90.2 | 2.0 | 0.0 | 0.0 | 0.0 | [33.4, 47.3] |
| ekf_naive | 227.4 | 156.1 | 484.8 | 673.9 | 4598.9 | 83.6 | 66.6 | 9.4 | 61.0 | [550.3, 859.5] |
| ekf_gated | 2.5 | 2.0 | 4.9 | 6.1 | 47.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.5, 6.9] |
| ekf_disp_gated | 8.7 | 7.1 | 16.7 | 21.5 | 45.9 | 0.0 | 0.0 | 0.0 | 0.0 | [18.3, 24.6] |
| ekf_topk_nn | 3.3 | 2.5 | 6.3 | 8.6 | 38.6 | 0.0 | 0.0 | 0.0 | 0.0 | [7.4, 10.1] |
| pf_topk | 2.5 | 2.1 | 4.8 | 6.2 | 24.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.5, 7.1] |

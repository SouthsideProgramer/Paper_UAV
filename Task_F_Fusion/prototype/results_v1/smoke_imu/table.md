Config: `{"world": "synthetic", "result_mat": "", "gps_path": "", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 4, "T": 60.0, "meas_every": 1, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "", "seed": 0, "workers": 4, "n_boot": 50, "tag": "smoke_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 790.6 | 9.5 | 3557.2 | 7305.6 | 8180.8 | 25.8 | 15.8 | 12.5 | 100.0 | [403.0, 7909.0] |
| dead_reckoning | 52.4 | 24.7 | 130.4 | 220.8 | 347.5 | 27.9 | 16.7 | 0.0 | 0.0 | [47.8, 302.5] |
| ekf_naive | 885.0 | 479.2 | 2452.2 | 3021.2 | 4592.9 | 76.2 | 75.4 | 47.9 | 100.0 | [1444.8, 3422.0] |
| ekf_gated | 8.2 | 6.9 | 16.2 | 20.2 | 27.7 | 0.0 | 0.0 | 0.0 | 0.0 | [16.2, 24.3] |
| ekf_disp_gated | 23.6 | 11.5 | 71.1 | 90.8 | 116.4 | 15.0 | 3.8 | 0.0 | 0.0 | [13.9, 108.0] |
| ekf_topk_nn | 12.3 | 6.5 | 48.2 | 50.1 | 55.4 | 5.4 | 0.0 | 0.0 | 0.0 | [8.6, 52.4] |

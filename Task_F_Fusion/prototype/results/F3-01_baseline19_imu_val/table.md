Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-01_baseline19_imu_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1264.5 | 613.1 | 3803.1 | 4437.2 | 5436.5 | 67.2 | 60.3 | 51.9 | 100.0 | [4201.5, 4700.9] |
| dead_reckoning | 211.6 | 144.0 | 489.1 | 623.3 | 1663.7 | 79.2 | 62.2 | 9.3 | 38.0 | [536.9, 695.7] |
| ekf_naive | 1231.5 | 1049.7 | 2488.1 | 2952.7 | 5160.1 | 99.0 | 97.7 | 77.8 | 100.0 | [2765.3, 3122.2] |
| ekf_gated | 44.8 | 15.9 | 89.6 | 171.7 | 2231.2 | 14.5 | 9.5 | 0.7 | 2.0 | [128.5, 221.6] |
| ekf_disp_gated | 131.1 | 43.8 | 302.1 | 626.3 | 2907.1 | 45.3 | 26.4 | 5.9 | 14.0 | [340.0, 948.7] |
| ekf_dispgate | 76.2 | 24.3 | 198.4 | 328.5 | 1605.1 | 28.3 | 16.8 | 3.1 | 10.0 | [223.4, 535.6] |
| ekf_topk_nn | 20.0 | 11.4 | 32.7 | 52.1 | 866.1 | 5.2 | 2.7 | 0.3 | 1.0 | [38.3, 99.4] |
| pf_topk | 28.0 | 14.3 | 55.0 | 107.4 | 513.5 | 11.3 | 5.5 | 0.0 | 1.0 | [64.0, 162.1] |
| mh_ekf | 59.0 | 10.1 | 28.1 | 46.6 | 5119.0 | 4.7 | 3.3 | 2.5 | 24.0 | [34.3, 114.7] |

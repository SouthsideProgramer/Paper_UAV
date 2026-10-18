Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-01_baseline19_vio_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1264.5 | 613.1 | 3803.1 | 4437.2 | 5436.5 | 67.2 | 60.3 | 51.9 | 100.0 | [4201.5, 4700.9] |
| dead_reckoning | 15.0 | 14.4 | 25.1 | 29.2 | 47.6 | 0.0 | 0.0 | 0.0 | 0.0 | [26.0, 31.5] |
| ekf_naive | 1133.1 | 1017.9 | 1977.4 | 2305.7 | 6229.3 | 99.2 | 98.4 | 85.2 | 100.0 | [2136.7, 2516.6] |
| ekf_gated | 17.0 | 8.4 | 27.8 | 66.9 | 257.1 | 6.0 | 4.2 | 0.0 | 0.0 | [39.5, 121.3] |
| ekf_disp_gated | 14.9 | 13.4 | 26.8 | 32.5 | 82.6 | 0.6 | 0.0 | 0.0 | 0.0 | [28.4, 37.5] |
| ekf_dispgate | 9.5 | 8.4 | 17.2 | 21.4 | 49.6 | 0.0 | 0.0 | 0.0 | 0.0 | [19.1, 24.0] |
| ekf_topk_nn | 7.9 | 6.0 | 13.6 | 18.0 | 157.9 | 0.7 | 0.3 | 0.0 | 0.0 | [15.1, 20.6] |
| pf_topk | 6.7 | 5.8 | 12.1 | 14.7 | 45.1 | 0.0 | 0.0 | 0.0 | 0.0 | [13.9, 15.9] |
| mh_ekf | 53.9 | 5.9 | 13.0 | 18.5 | 5081.2 | 3.0 | 2.9 | 2.8 | 25.0 | [14.8, 32.7] |

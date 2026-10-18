Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-06_lpn86_test_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 76.7 | 8.6 | 24.7 | 77.9 | 4290.1 | 6.3 | 4.7 | 4.2 | 100.0 | [64.0, 119.1] |
| dead_reckoning | 230.9 | 162.5 | 521.5 | 712.8 | 1870.9 | 78.0 | 63.4 | 10.9 | 38.0 | [573.1, 870.6] |
| ekf_gated | 5.1 | 4.3 | 9.1 | 11.6 | 53.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 12.6] |
| pf_topk | 7.9 | 5.6 | 14.1 | 20.2 | 167.1 | 0.9 | 0.2 | 0.0 | 0.0 | [15.8, 29.1] |
| mh_ekf | 4.9 | 4.1 | 8.6 | 10.8 | 56.8 | 0.0 | 0.0 | 0.0 | 0.0 | [9.9, 11.8] |

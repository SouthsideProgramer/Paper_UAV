Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-06_lpn86_test_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 76.7 | 8.6 | 24.7 | 77.9 | 4290.1 | 6.3 | 4.7 | 4.2 | 100.0 | [64.0, 119.1] |
| dead_reckoning | 353.4 | 347.7 | 586.6 | 670.4 | 904.0 | 99.7 | 94.0 | 18.5 | 20.0 | [581.5, 716.0] |
| ekf_gated | 37.1 | 2.8 | 6.0 | 8.5 | 1294.1 | 3.1 | 3.1 | 3.0 | 3.0 | [6.6, 873.8] |
| pf_topk | 6.0 | 4.3 | 10.4 | 13.4 | 686.6 | 0.4 | 0.3 | 0.0 | 4.0 | [12.0, 15.3] |
| mh_ekf | 3.6 | 2.6 | 5.2 | 6.3 | 1277.7 | 0.1 | 0.1 | 0.1 | 18.0 | [5.8, 6.7] |

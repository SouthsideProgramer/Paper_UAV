Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-05_vits79_test_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 144.7 | 8.9 | 40.4 | 1306.3 | 4379.3 | 8.8 | 7.4 | 6.7 | 100.0 | [1082.7, 1341.8] |
| dead_reckoning | 353.4 | 347.7 | 586.6 | 670.4 | 904.0 | 99.7 | 94.0 | 18.5 | 20.0 | [581.5, 716.0] |
| ekf_gated | 71.4 | 3.2 | 8.3 | 682.2 | 1779.4 | 6.2 | 6.2 | 6.0 | 8.0 | [8.9, 1283.5] |
| pf_topk | 6.1 | 4.3 | 10.5 | 13.4 | 686.6 | 0.4 | 0.3 | 0.0 | 5.0 | [12.2, 14.6] |
| mh_ekf | 3.8 | 2.7 | 5.3 | 6.4 | 1263.5 | 0.2 | 0.1 | 0.1 | 20.0 | [6.0, 6.8] |

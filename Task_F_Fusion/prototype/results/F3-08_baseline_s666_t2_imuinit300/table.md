Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s666_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 129.6 | 8.9 | 35.9 | 1082.8 | 4379.0 | 8.2 | 6.8 | 6.0 | 100.0 | [592.6, 1283.8] |
| ekf_gated | 36.4 | 5.0 | 11.9 | 17.1 | 1526.0 | 2.4 | 2.4 | 2.3 | 4.0 | [13.9, 745.1] |
| pf_topk | 115.7 | 27.2 | 371.8 | 594.8 | 1386.2 | 34.7 | 26.4 | 6.8 | 23.0 | [455.8, 682.0] |
| mh_ekf | 5.8 | 4.3 | 9.3 | 11.5 | 929.9 | 0.2 | 0.2 | 0.1 | 23.0 | [10.8, 12.1] |

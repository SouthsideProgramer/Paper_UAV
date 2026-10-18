Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s666_t2_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 129.6 | 8.9 | 35.9 | 1082.8 | 4379.0 | 8.2 | 6.8 | 6.0 | 100.0 | [592.6, 1283.8] |
| ekf_gated | 5.7 | 4.8 | 10.7 | 13.4 | 54.6 | 0.0 | 0.0 | 0.0 | 0.0 | [12.7, 14.3] |
| pf_topk | 10.4 | 5.9 | 16.6 | 24.4 | 399.5 | 2.1 | 1.2 | 0.0 | 0.0 | [19.5, 45.7] |
| mh_ekf | 5.0 | 4.3 | 9.2 | 11.3 | 43.0 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.9] |

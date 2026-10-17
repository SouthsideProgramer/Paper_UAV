Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t0_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 84.1 | 8.8 | 30.4 | 75.8 | 4290.1 | 6.4 | 4.3 | 3.8 | 87.0 | [65.8, 98.2] |
| ekf_gated | 29.6 | 4.8 | 11.6 | 16.7 | 1367.2 | 2.3 | 2.1 | 2.0 | 2.0 | [13.4, 433.2] |
| pf_topk | 136.5 | 35.9 | 422.9 | 623.6 | 1815.6 | 41.4 | 30.9 | 8.0 | 29.0 | [501.7, 764.3] |
| mh_ekf | 6.0 | 4.4 | 9.8 | 12.5 | 903.6 | 0.3 | 0.1 | 0.1 | 18.0 | [11.5, 13.5] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t1_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 118.5 | 9.0 | 36.1 | 944.8 | 4459.1 | 8.4 | 6.7 | 5.7 | 100.0 | [537.5, 1208.0] |
| ekf_gated | 24.6 | 4.9 | 11.7 | 15.5 | 2208.4 | 1.8 | 1.6 | 1.3 | 4.0 | [13.3, 24.3] |
| pf_topk | 134.5 | 39.2 | 422.8 | 568.0 | 1712.2 | 43.5 | 32.6 | 7.0 | 30.0 | [469.8, 689.0] |
| mh_ekf | 6.3 | 4.6 | 10.0 | 12.3 | 925.7 | 0.3 | 0.2 | 0.1 | 27.0 | [11.6, 13.1] |

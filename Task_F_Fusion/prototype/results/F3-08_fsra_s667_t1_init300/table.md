Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t1_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 118.5 | 9.0 | 36.1 | 944.8 | 4459.1 | 8.4 | 6.7 | 5.7 | 100.0 | [537.5, 1208.0] |
| ekf_gated | 22.0 | 3.1 | 6.4 | 8.0 | 1301.1 | 2.1 | 2.0 | 2.0 | 4.0 | [7.0, 99.4] |
| pf_topk | 6.5 | 4.5 | 11.0 | 14.0 | 911.4 | 0.4 | 0.3 | 0.0 | 9.0 | [12.9, 15.3] |
| mh_ekf | 4.1 | 2.9 | 5.7 | 6.7 | 926.1 | 0.2 | 0.2 | 0.1 | 27.0 | [6.4, 7.0] |

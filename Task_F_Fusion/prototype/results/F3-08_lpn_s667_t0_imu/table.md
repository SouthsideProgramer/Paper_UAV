Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t0_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 84.1 | 8.8 | 30.4 | 75.8 | 4290.1 | 6.4 | 4.3 | 3.8 | 87.0 | [65.8, 98.2] |
| ekf_gated | 5.9 | 4.8 | 10.6 | 13.9 | 158.5 | 0.2 | 0.1 | 0.0 | 0.0 | [12.7, 15.0] |
| pf_topk | 12.5 | 6.1 | 20.2 | 36.9 | 691.7 | 3.1 | 1.5 | 0.1 | 1.0 | [23.8, 49.7] |
| mh_ekf | 5.4 | 4.5 | 9.6 | 12.3 | 120.0 | 0.1 | 0.0 | 0.0 | 0.0 | [11.3, 13.3] |

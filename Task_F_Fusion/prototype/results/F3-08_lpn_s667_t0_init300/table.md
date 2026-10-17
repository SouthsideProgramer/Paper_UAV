Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t0_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 84.1 | 8.8 | 30.4 | 75.8 | 4290.1 | 6.4 | 4.3 | 3.8 | 87.0 | [65.8, 98.2] |
| ekf_gated | 28.3 | 3.0 | 6.6 | 8.9 | 1287.7 | 2.1 | 2.1 | 2.0 | 2.0 | [7.5, 443.5] |
| pf_topk | 6.1 | 4.4 | 10.5 | 13.6 | 686.6 | 0.4 | 0.3 | 0.0 | 5.0 | [12.1, 15.7] |
| mh_ekf | 3.8 | 2.8 | 5.6 | 6.9 | 903.8 | 0.2 | 0.1 | 0.1 | 18.0 | [6.4, 7.3] |

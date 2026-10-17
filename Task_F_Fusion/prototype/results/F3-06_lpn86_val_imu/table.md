Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-06_lpn86_val_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 80.3 | 8.6 | 20.8 | 63.5 | 5200.7 | 6.6 | 3.8 | 2.4 | 76.0 | [59.8, 67.3] |
| dead_reckoning | 227.4 | 158.7 | 502.9 | 693.3 | 1857.2 | 78.5 | 63.3 | 10.1 | 33.0 | [550.1, 864.4] |
| ekf_gated | 5.1 | 4.3 | 9.7 | 12.3 | 42.2 | 0.0 | 0.0 | 0.0 | 0.0 | [11.5, 13.1] |
| pf_topk | 8.9 | 5.2 | 13.8 | 18.8 | 601.0 | 1.1 | 0.7 | 0.1 | 1.0 | [15.6, 25.8] |
| mh_ekf | 4.8 | 4.0 | 9.0 | 11.3 | 35.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 12.0] |

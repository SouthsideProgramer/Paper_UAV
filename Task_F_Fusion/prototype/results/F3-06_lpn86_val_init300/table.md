Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-06_lpn86_val_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 80.3 | 8.6 | 20.8 | 63.5 | 5200.7 | 6.6 | 3.8 | 2.4 | 76.0 | [59.8, 67.3] |
| dead_reckoning | 353.6 | 347.5 | 586.9 | 670.2 | 904.7 | 99.5 | 94.2 | 18.2 | 20.0 | [583.3, 715.3] |
| ekf_gated | 3.6 | 2.6 | 5.6 | 7.0 | 214.2 | 0.4 | 0.4 | 0.0 | 0.0 | [6.4, 7.6] |
| pf_topk | 6.1 | 4.3 | 10.2 | 13.2 | 741.8 | 0.4 | 0.3 | 0.0 | 5.0 | [11.9, 14.7] |
| mh_ekf | 3.4 | 2.5 | 5.2 | 6.3 | 903.8 | 0.1 | 0.1 | 0.1 | 18.0 | [5.9, 6.7] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-06_lpn86_val_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 80.3 | 8.6 | 20.8 | 63.5 | 5200.7 | 6.6 | 3.8 | 2.4 | 76.0 | [59.8, 67.3] |
| dead_reckoning | 15.2 | 14.5 | 25.5 | 29.5 | 75.1 | 0.4 | 0.0 | 0.0 | 0.0 | [26.2, 32.8] |
| ekf_gated | 3.0 | 2.6 | 5.5 | 6.9 | 37.1 | 0.0 | 0.0 | 0.0 | 0.0 | [6.4, 7.4] |
| pf_topk | 2.8 | 2.5 | 5.2 | 6.2 | 28.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.9, 6.6] |
| mh_ekf | 2.8 | 2.5 | 5.2 | 6.3 | 26.1 | 0.0 | 0.0 | 0.0 | 0.0 | [5.9, 6.7] |

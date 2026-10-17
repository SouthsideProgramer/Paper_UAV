Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "campuses": "val", "seed": 0, "workers": 6, "n_boot": 1000, "tag": "F3-06_lpn86_val_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 80.3 | 8.6 | 20.8 | 63.5 | 5200.7 | 6.6 | 3.8 | 2.4 | 76.0 | [59.8, 67.3] |
| dead_reckoning | 434.6 | 379.8 | 792.4 | 918.7 | 1831.1 | 99.5 | 96.9 | 32.5 | 55.0 | [835.8, 1004.4] |
| ekf_gated | 5.5 | 4.3 | 9.8 | 12.6 | 195.8 | 0.3 | 0.3 | 0.0 | 0.0 | [11.8, 13.4] |
| pf_topk | 140.3 | 39.0 | 382.9 | 622.9 | 2518.1 | 42.8 | 32.4 | 7.1 | 24.0 | [450.0, 789.3] |
| mh_ekf | 5.3 | 4.0 | 9.0 | 11.4 | 903.6 | 0.1 | 0.1 | 0.1 | 18.0 | [10.7, 12.1] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_fsra_W60_imuinit300", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 95.2 | 57.6 | 212.7 | 294.9 | 959.5 | 53.6 | 34.0 | 2.2 | 15.0 | [243.4, 366.3] |
| naviloc_yaw | 93.9 | 62.1 | 206.2 | 265.1 | 957.0 | 56.5 | 34.9 | 1.7 | 14.0 | [227.2, 353.2] |
| naviloc_causal | 110.5 | 67.4 | 246.6 | 337.1 | 4122.0 | 58.6 | 38.0 | 2.2 | 33.0 | [275.2, 425.8] |
| mh_ekf | 5.1 | 3.9 | 8.4 | 10.3 | 903.6 | 0.1 | 0.1 | 0.1 | 18.0 | [9.7, 10.9] |

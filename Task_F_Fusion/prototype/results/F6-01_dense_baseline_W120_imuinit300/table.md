Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_baseline_W120_imuinit300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 106.8 | 62.5 | 252.7 | 355.0 | 958.5 | 55.9 | 36.7 | 2.4 | 13.0 | [273.2, 466.1] |
| naviloc_yaw | 108.3 | 73.1 | 250.7 | 328.8 | 957.8 | 60.2 | 39.7 | 1.8 | 12.0 | [270.9, 408.7] |
| naviloc_causal | 123.2 | 79.2 | 282.1 | 379.2 | 3212.3 | 63.4 | 42.9 | 2.5 | 32.0 | [310.2, 467.2] |
| mh_ekf | 5.4 | 4.0 | 9.2 | 11.5 | 903.6 | 0.2 | 0.1 | 0.1 | 17.0 | [10.7, 12.3] |

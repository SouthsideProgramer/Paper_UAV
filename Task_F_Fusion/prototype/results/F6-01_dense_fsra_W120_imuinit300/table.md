Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_fsra_W120_imuinit300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 106.4 | 63.4 | 252.5 | 357.7 | 1072.1 | 56.8 | 36.1 | 2.2 | 14.0 | [282.3, 443.5] |
| naviloc_yaw | 108.4 | 71.3 | 255.2 | 340.9 | 967.7 | 60.0 | 39.0 | 2.0 | 13.0 | [278.7, 431.8] |
| naviloc_causal | 123.5 | 79.8 | 282.2 | 382.9 | 4122.0 | 62.8 | 43.1 | 2.5 | 32.0 | [311.1, 476.0] |
| mh_ekf | 5.1 | 3.9 | 8.4 | 10.3 | 903.6 | 0.1 | 0.1 | 0.1 | 18.0 | [9.7, 10.9] |

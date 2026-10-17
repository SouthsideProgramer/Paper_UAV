Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_fsra_W30_imuinit300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 94.8 | 63.9 | 201.1 | 270.0 | 962.3 | 56.7 | 35.2 | 2.0 | 15.0 | [226.9, 336.4] |
| naviloc_yaw | 97.9 | 71.0 | 200.5 | 261.1 | 927.6 | 61.2 | 36.8 | 2.0 | 14.0 | [222.8, 361.4] |
| naviloc_causal | 105.6 | 67.2 | 223.5 | 299.5 | 4122.0 | 57.8 | 37.4 | 3.0 | 35.0 | [242.6, 409.5] |
| mh_ekf | 5.1 | 3.9 | 8.4 | 10.3 | 903.6 | 0.1 | 0.1 | 0.1 | 18.0 | [9.7, 10.9] |

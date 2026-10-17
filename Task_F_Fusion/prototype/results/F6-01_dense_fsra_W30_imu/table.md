Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_fsra_W30_imu", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 94.8 | 63.9 | 201.1 | 270.0 | 962.3 | 56.7 | 35.2 | 2.0 | 15.0 | [226.9, 336.4] |
| naviloc_yaw | 97.9 | 71.0 | 200.5 | 261.1 | 927.6 | 61.2 | 36.8 | 2.0 | 14.0 | [222.8, 361.4] |
| naviloc_causal | 103.3 | 65.5 | 219.9 | 288.7 | 4122.0 | 57.1 | 36.8 | 2.9 | 19.0 | [236.1, 382.4] |
| mh_ekf | 4.5 | 3.9 | 8.4 | 10.3 | 41.4 | 0.0 | 0.0 | 0.0 | 0.0 | [9.7, 10.8] |

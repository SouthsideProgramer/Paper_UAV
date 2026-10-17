Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_baseline_W30_imuinit300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 92.7 | 61.6 | 201.7 | 264.0 | 921.8 | 55.5 | 34.5 | 1.9 | 14.0 | [222.0, 317.3] |
| naviloc_yaw | 97.6 | 69.4 | 200.7 | 261.2 | 922.6 | 60.7 | 36.7 | 1.9 | 14.0 | [219.8, 346.4] |
| naviloc_causal | 104.0 | 67.4 | 222.3 | 292.7 | 3212.3 | 57.6 | 37.5 | 2.8 | 37.0 | [246.1, 389.8] |
| mh_ekf | 5.4 | 4.0 | 9.2 | 11.5 | 903.6 | 0.2 | 0.1 | 0.1 | 17.0 | [10.7, 12.3] |

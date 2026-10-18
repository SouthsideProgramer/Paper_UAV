Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_baseline_W120_imu", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 106.8 | 62.5 | 252.7 | 355.0 | 958.5 | 55.9 | 36.7 | 2.4 | 13.0 | [273.2, 466.1] |
| naviloc_yaw | 108.3 | 73.1 | 250.7 | 328.8 | 957.8 | 60.2 | 39.7 | 1.8 | 12.0 | [270.9, 408.7] |
| naviloc_causal | 120.9 | 77.5 | 277.6 | 373.3 | 3212.3 | 62.7 | 42.3 | 2.4 | 17.0 | [300.8, 460.8] |
| mh_ekf | 4.8 | 4.0 | 9.1 | 11.3 | 41.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 12.1] |

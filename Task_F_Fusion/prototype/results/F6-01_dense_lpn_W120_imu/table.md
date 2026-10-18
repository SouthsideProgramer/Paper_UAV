Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_lpn_W120_imu", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 102.7 | 61.2 | 238.7 | 332.9 | 959.7 | 55.4 | 35.5 | 2.0 | 13.0 | [258.4, 421.3] |
| naviloc_yaw | 108.0 | 70.5 | 254.3 | 329.4 | 894.8 | 59.3 | 39.2 | 1.8 | 14.0 | [276.2, 397.2] |
| naviloc_causal | 120.4 | 78.0 | 273.4 | 372.0 | 4150.0 | 61.9 | 42.7 | 2.4 | 12.0 | [293.8, 468.0] |
| mh_ekf | 4.8 | 4.0 | 9.0 | 11.3 | 35.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.9] |

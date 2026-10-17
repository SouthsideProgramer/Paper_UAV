Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_lpn_W60_imu", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 93.1 | 55.7 | 210.1 | 287.5 | 938.8 | 52.7 | 32.7 | 2.1 | 16.0 | [235.7, 369.3] |
| naviloc_yaw | 96.5 | 62.6 | 213.3 | 286.3 | 927.8 | 55.8 | 34.6 | 2.0 | 15.0 | [240.7, 382.5] |
| naviloc_causal | 106.4 | 67.1 | 240.4 | 314.4 | 4150.0 | 57.5 | 37.9 | 2.0 | 16.0 | [260.1, 410.0] |
| mh_ekf | 4.8 | 4.0 | 9.0 | 11.3 | 35.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 11.9] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_lpn_W30_imuinit300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 91.8 | 60.4 | 199.4 | 255.8 | 940.6 | 55.0 | 33.4 | 2.0 | 16.0 | [220.5, 324.7] |
| naviloc_yaw | 97.0 | 68.0 | 201.5 | 254.8 | 884.6 | 59.0 | 36.6 | 2.2 | 14.0 | [219.1, 379.6] |
| naviloc_causal | 103.7 | 67.2 | 221.6 | 286.0 | 4150.0 | 56.8 | 37.8 | 3.0 | 35.0 | [239.3, 461.9] |
| mh_ekf | 5.3 | 4.0 | 9.0 | 11.4 | 903.6 | 0.1 | 0.1 | 0.1 | 18.0 | [10.7, 12.1] |

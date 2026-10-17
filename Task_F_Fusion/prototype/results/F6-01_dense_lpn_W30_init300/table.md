Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_lpn_W30_init300", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 5.0 | 4.4 | 8.8 | 10.5 | 38.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 10.9] |
| naviloc_yaw | 5.0 | 4.5 | 8.8 | 10.5 | 38.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 10.9] |
| naviloc_causal | 9.1 | 5.8 | 11.8 | 14.5 | 4149.8 | 0.8 | 0.7 | 0.1 | 19.0 | [14.0, 15.1] |
| mh_ekf | 3.4 | 2.5 | 5.2 | 6.3 | 903.8 | 0.1 | 0.1 | 0.1 | 18.0 | [6.0, 6.6] |

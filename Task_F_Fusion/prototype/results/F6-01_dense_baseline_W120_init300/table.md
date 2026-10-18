Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_baseline_W120_init300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 5.5 | 5.0 | 9.8 | 11.3 | 30.0 | 0.0 | 0.0 | 0.0 | 0.0 | [10.7, 11.9] |
| naviloc_yaw | 5.5 | 4.9 | 9.8 | 11.5 | 30.0 | 0.0 | 0.0 | 0.0 | 0.0 | [10.8, 12.2] |
| naviloc_causal | 9.2 | 5.7 | 11.3 | 13.6 | 3212.4 | 0.8 | 0.7 | 0.2 | 23.0 | [13.0, 14.5] |
| mh_ekf | 3.4 | 2.5 | 5.1 | 6.2 | 903.8 | 0.2 | 0.1 | 0.1 | 17.0 | [5.9, 6.5] |

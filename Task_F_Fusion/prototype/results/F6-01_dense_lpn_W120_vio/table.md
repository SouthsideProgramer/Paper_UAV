Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_lpn_W120_vio", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 5.2 | 4.7 | 9.1 | 10.5 | 30.2 | 0.0 | 0.0 | 0.0 | 0.0 | [9.9, 11.1] |
| naviloc_yaw | 5.2 | 4.8 | 9.2 | 10.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.0, 11.3] |
| naviloc_causal | 6.7 | 5.8 | 11.1 | 13.1 | 4149.8 | 0.1 | 0.0 | 0.0 | 2.0 | [12.6, 13.5] |
| mh_ekf | 2.8 | 2.5 | 5.2 | 6.3 | 26.1 | 0.0 | 0.0 | 0.0 | 0.0 | [6.0, 6.6] |

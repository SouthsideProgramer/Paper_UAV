Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_fsra_W30_vio", "cfg": "{\"nl_W\": 30, \"nl_O\": 15, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 5.1 | 4.6 | 9.2 | 11.0 | 38.1 | 0.0 | 0.0 | 0.0 | 0.0 | [10.7, 11.5] |
| naviloc_yaw | 5.2 | 4.6 | 9.3 | 11.3 | 43.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.9, 11.6] |
| naviloc_causal | 7.9 | 5.9 | 12.1 | 14.6 | 4121.1 | 0.2 | 0.1 | 0.0 | 4.0 | [14.2, 15.0] |
| mh_ekf | 2.7 | 2.4 | 4.8 | 5.6 | 19.5 | 0.0 | 0.0 | 0.0 | 0.0 | [5.3, 5.9] |

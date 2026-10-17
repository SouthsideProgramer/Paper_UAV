Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_fsra_W120_init300", "cfg": "{\"nl_W\": 120, \"nl_O\": 60, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 5.3 | 4.7 | 9.5 | 11.4 | 26.5 | 0.0 | 0.0 | 0.0 | 0.0 | [10.7, 12.0] |
| naviloc_yaw | 5.2 | 4.7 | 9.5 | 11.2 | 22.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.5, 11.8] |
| naviloc_causal | 9.9 | 5.8 | 11.6 | 13.8 | 4121.1 | 0.9 | 0.7 | 0.2 | 21.0 | [13.2, 14.5] |
| mh_ekf | 3.3 | 2.4 | 4.7 | 5.6 | 903.8 | 0.1 | 0.1 | 0.1 | 18.0 | [5.3, 6.0] |

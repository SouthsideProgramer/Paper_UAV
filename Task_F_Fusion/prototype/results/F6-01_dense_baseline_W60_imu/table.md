Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "naviloc,naviloc_yaw,naviloc_causal,mh_ekf", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-01_dense_baseline_W60_imu", "cfg": "{\"nl_W\": 60, \"nl_O\": 30, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| naviloc | 91.3 | 56.5 | 208.2 | 282.4 | 888.7 | 52.8 | 32.6 | 1.5 | 12.0 | [235.7, 334.7] |
| naviloc_yaw | 95.0 | 63.4 | 204.6 | 272.5 | 892.0 | 56.5 | 34.1 | 2.0 | 12.0 | [228.3, 357.8] |
| naviloc_causal | 107.5 | 66.4 | 243.0 | 317.5 | 3212.3 | 58.2 | 37.7 | 1.8 | 20.0 | [264.9, 398.9] |
| mh_ekf | 4.8 | 4.0 | 9.1 | 11.3 | 41.9 | 0.0 | 0.0 | 0.0 | 0.0 | [10.6, 12.1] |

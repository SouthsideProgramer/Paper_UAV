Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "mh_ekf", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 50, "tag": "F8_dense_gate1382_lpn_s667_t0_imuinit300", "cfg": "{\"mh_gate\": 13.82, \"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| mh_ekf | 6.1 | 4.4 | 10.0 | 12.8 | 1483.0 | 0.2 | 0.1 | 0.1 | 19.0 | [11.8, 13.8] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 200, "tag": "F3-09_baseline_s667_t2_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 6.0 | 4.9 | 11.2 | 14.4 | 55.1 | 0.0 | 0.0 | 0.0 | 0.0 | [13.6, 15.1] |
| mh_ekf | 5.1 | 4.4 | 9.2 | 11.4 | 50.3 | 0.0 | 0.0 | 0.0 | 0.0 | [10.8, 12.1] |

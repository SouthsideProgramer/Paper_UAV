Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F3-09_baseline_s668_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 55.3 | 4.9 | 13.1 | 28.8 | 1667.5 | 4.7 | 4.6 | 4.5 | 5.0 | [14.6, 1211.3] |
| mh_ekf | 5.6 | 4.1 | 8.6 | 10.6 | 903.6 | 0.2 | 0.2 | 0.1 | 18.0 | [10.1, 11.3] |

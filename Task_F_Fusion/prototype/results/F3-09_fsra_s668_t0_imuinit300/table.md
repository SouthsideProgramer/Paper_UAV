Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F3-09_fsra_s668_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 38.2 | 4.6 | 11.3 | 17.4 | 1780.6 | 3.1 | 3.1 | 3.0 | 5.0 | [12.6, 812.4] |
| mh_ekf | 5.3 | 3.9 | 8.3 | 10.3 | 1169.1 | 0.2 | 0.2 | 0.1 | 19.0 | [9.7, 11.2] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F3-09_lpn_s668_t0_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 28.5 | 2.7 | 5.8 | 7.4 | 1557.3 | 2.1 | 2.0 | 2.0 | 2.0 | [6.4, 428.7] |
| mh_ekf | 3.5 | 2.5 | 5.2 | 6.2 | 1548.4 | 0.1 | 0.1 | 0.1 | 19.0 | [5.9, 6.7] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 200, "tag": "F3-09_fsra_s666_t0_init300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 9.4 | 3.1 | 6.6 | 8.5 | 572.9 | 1.1 | 1.1 | 1.0 | 2.0 | [7.5, 12.0] |
| mh_ekf | 3.8 | 2.7 | 5.6 | 6.9 | 903.8 | 0.1 | 0.1 | 0.1 | 19.0 | [6.1, 7.6] |

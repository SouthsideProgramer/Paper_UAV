Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 200, "tag": "F3-09_fsra_s668_t2_vio", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 3.4 | 3.1 | 5.9 | 7.1 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | [6.8, 7.4] |
| mh_ekf | 2.9 | 2.6 | 4.9 | 6.0 | 28.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.6, 6.4] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,mh_ekf", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 200, "tag": "F3-09_baseline_s666_t1_vio", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 3.8 | 3.4 | 6.7 | 8.0 | 33.1 | 0.0 | 0.0 | 0.0 | 0.0 | [7.4, 8.5] |
| mh_ekf | 3.3 | 3.0 | 5.7 | 6.8 | 33.1 | 0.0 | 0.0 | 0.0 | 0.0 | [6.5, 7.3] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s666_t1_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 6.0 | 4.9 | 11.4 | 14.1 | 71.0 | 0.0 | 0.0 | 0.0 | 0.0 | [13.5, 14.9] |
| naviloc | 82.7 | 58.2 | 188.0 | 230.7 | 954.3 | 54.7 | 31.1 | 0.7 | 10.0 | [215.8, 257.0] |
| naviloc_yaw | 90.3 | 66.3 | 196.1 | 247.4 | 1094.8 | 59.5 | 33.8 | 0.9 | 11.0 | [224.3, 290.3] |
| naviloc_causal | 90.2 | 62.3 | 201.2 | 254.8 | 4423.2 | 55.8 | 35.3 | 0.7 | 11.0 | [229.0, 282.4] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s668_t1_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.6 | 4.7 | 10.6 | 13.1 | 39.4 | 0.0 | 0.0 | 0.0 | 0.0 | [12.5, 13.7] |
| naviloc | 85.8 | 60.5 | 189.0 | 236.6 | 1082.6 | 55.7 | 32.2 | 0.9 | 8.0 | [216.7, 270.3] |
| naviloc_yaw | 91.5 | 67.7 | 194.5 | 242.8 | 1049.0 | 60.0 | 34.5 | 0.8 | 9.0 | [223.5, 294.1] |
| naviloc_causal | 90.3 | 63.1 | 200.1 | 251.1 | 1521.9 | 56.2 | 35.1 | 0.8 | 9.0 | [230.7, 284.6] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s668_t1_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 27.7 | 4.8 | 11.5 | 15.1 | 1648.3 | 2.0 | 2.0 | 2.0 | 5.0 | [13.0, 20.4] |
| naviloc | 85.8 | 60.5 | 189.0 | 236.6 | 1082.6 | 55.7 | 32.2 | 0.9 | 8.0 | [216.7, 270.3] |
| naviloc_yaw | 91.5 | 67.7 | 194.5 | 242.8 | 1049.0 | 60.0 | 34.5 | 0.8 | 9.0 | [223.5, 294.1] |
| naviloc_causal | 92.7 | 64.5 | 203.9 | 258.9 | 1521.9 | 56.9 | 35.8 | 1.0 | 34.0 | [237.3, 296.5] |

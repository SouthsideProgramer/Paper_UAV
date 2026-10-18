Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s666_t1_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 18.6 | 4.9 | 11.8 | 15.1 | 1418.3 | 1.0 | 1.0 | 1.0 | 2.0 | [13.6, 18.8] |
| naviloc | 82.7 | 58.2 | 188.0 | 230.7 | 954.3 | 54.7 | 31.1 | 0.7 | 10.0 | [215.8, 257.0] |
| naviloc_yaw | 90.3 | 66.3 | 196.1 | 247.4 | 1094.8 | 59.5 | 33.8 | 0.9 | 11.0 | [224.3, 290.3] |
| naviloc_causal | 92.7 | 63.7 | 204.8 | 262.3 | 4423.2 | 56.5 | 36.0 | 0.9 | 33.0 | [239.2, 289.4] |

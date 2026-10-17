Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 1, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s667_t1_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 6.0 | 4.8 | 11.1 | 14.3 | 137.8 | 0.2 | 0.0 | 0.0 | 0.0 | [13.3, 15.4] |
| naviloc | 85.6 | 58.6 | 190.5 | 235.3 | 1214.5 | 54.4 | 32.0 | 0.9 | 9.0 | [216.7, 270.0] |
| naviloc_yaw | 90.0 | 66.5 | 194.6 | 242.3 | 1062.0 | 59.4 | 33.3 | 1.0 | 8.0 | [222.2, 282.3] |
| naviloc_causal | 92.3 | 63.9 | 205.3 | 259.6 | 1253.5 | 56.8 | 35.9 | 0.9 | 33.0 | [239.1, 290.1] |

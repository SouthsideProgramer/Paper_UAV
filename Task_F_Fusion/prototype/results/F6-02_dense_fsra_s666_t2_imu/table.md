Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s666_t2_imu", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 5.8 | 4.9 | 10.7 | 13.6 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | [12.9, 14.3] |
| naviloc | 91.5 | 60.3 | 194.6 | 252.6 | 1183.9 | 55.4 | 32.9 | 1.7 | 11.0 | [220.9, 320.4] |
| naviloc_yaw | 90.4 | 66.5 | 195.5 | 247.0 | 859.5 | 58.3 | 34.7 | 0.9 | 6.0 | [222.5, 292.1] |
| naviloc_causal | 93.0 | 65.5 | 204.0 | 255.0 | 4064.2 | 57.3 | 36.0 | 1.0 | 17.0 | [228.7, 281.8] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_fsra_s666_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 27.6 | 5.0 | 11.8 | 16.0 | 1318.7 | 2.0 | 2.0 | 2.0 | 5.0 | [13.8, 20.5] |
| naviloc | 91.5 | 60.3 | 194.6 | 252.6 | 1183.9 | 55.4 | 32.9 | 1.7 | 11.0 | [220.9, 320.4] |
| naviloc_yaw | 90.4 | 66.5 | 195.5 | 247.0 | 859.5 | 58.3 | 34.7 | 0.9 | 6.0 | [222.5, 292.1] |
| naviloc_causal | 95.3 | 66.9 | 207.7 | 262.0 | 4064.2 | 58.0 | 36.6 | 1.2 | 34.0 | [234.5, 289.3] |

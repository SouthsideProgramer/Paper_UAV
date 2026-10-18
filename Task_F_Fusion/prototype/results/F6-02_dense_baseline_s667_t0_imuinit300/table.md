Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 0, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_baseline_s667_t0_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 34.9 | 4.9 | 12.0 | 17.1 | 3539.5 | 2.3 | 2.1 | 2.0 | 3.0 | [13.9, 124.5] |
| naviloc | 106.2 | 66.4 | 225.4 | 356.0 | 1117.0 | 58.0 | 36.2 | 3.5 | 16.0 | [255.3, 541.4] |
| naviloc_yaw | 99.0 | 70.1 | 208.5 | 280.1 | 992.3 | 61.0 | 36.7 | 1.4 | 10.0 | [233.4, 368.3] |
| naviloc_causal | 104.0 | 67.3 | 224.4 | 301.3 | 1784.3 | 57.3 | 37.7 | 2.3 | 38.0 | [250.1, 386.0] |

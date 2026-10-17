Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "ekf_gated,naviloc,naviloc_yaw,naviloc_causal", "campuses": "test", "seed": 2, "workers": 11, "n_boot": 100, "tag": "F6-02_dense_lpn_s666_t2_imuinit300", "cfg": "{\"v_max\": 0.0}"}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| ekf_gated | 34.5 | 4.5 | 10.6 | 16.6 | 1318.7 | 3.3 | 3.3 | 2.9 | 4.0 | [11.7, 552.6] |
| naviloc | 91.0 | 58.5 | 195.7 | 261.6 | 973.1 | 54.6 | 32.8 | 1.7 | 12.0 | [224.3, 318.6] |
| naviloc_yaw | 91.5 | 64.7 | 192.1 | 252.1 | 1047.5 | 57.5 | 35.0 | 1.2 | 7.0 | [223.0, 307.5] |
| naviloc_causal | 94.4 | 66.5 | 203.7 | 259.4 | 3204.7 | 57.7 | 36.8 | 1.2 | 32.0 | [232.9, 296.8] |

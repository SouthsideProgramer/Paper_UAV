Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t1_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 106.7 | 9.0 | 37.4 | 603.9 | 4270.1 | 8.4 | 5.9 | 5.5 | 100.0 | [502.2, 868.0] |
| ekf_gated | 6.0 | 5.0 | 11.2 | 14.1 | 51.7 | 0.0 | 0.0 | 0.0 | 0.0 | [13.3, 14.9] |
| pf_topk | 9.6 | 5.9 | 16.4 | 24.8 | 282.8 | 1.9 | 0.9 | 0.0 | 0.0 | [18.6, 36.3] |
| mh_ekf | 5.0 | 4.4 | 9.2 | 11.3 | 52.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.5, 12.4] |

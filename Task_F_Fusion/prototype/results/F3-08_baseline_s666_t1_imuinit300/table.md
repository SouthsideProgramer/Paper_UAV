Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s666_t1_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 136.6 | 9.0 | 39.4 | 1174.4 | 4379.8 | 8.7 | 7.1 | 5.9 | 99.0 | [686.4, 1299.3] |
| ekf_gated | 35.2 | 5.1 | 13.0 | 20.5 | 1513.2 | 3.6 | 3.5 | 3.0 | 4.0 | [14.7, 695.7] |
| pf_topk | 121.1 | 35.4 | 368.2 | 535.2 | 1375.5 | 42.0 | 30.5 | 6.0 | 27.0 | [423.7, 659.4] |
| mh_ekf | 6.0 | 4.4 | 9.8 | 12.1 | 925.7 | 0.2 | 0.1 | 0.1 | 26.0 | [11.5, 12.7] |

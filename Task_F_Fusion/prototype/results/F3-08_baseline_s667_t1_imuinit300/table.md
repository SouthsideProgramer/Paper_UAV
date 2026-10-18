Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t1_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 106.7 | 9.0 | 37.4 | 603.9 | 4270.1 | 8.4 | 5.9 | 5.5 | 100.0 | [502.2, 868.0] |
| ekf_gated | 15.2 | 5.1 | 11.9 | 15.8 | 916.2 | 1.4 | 1.3 | 1.0 | 2.0 | [14.0, 20.0] |
| pf_topk | 129.3 | 37.1 | 396.9 | 557.8 | 1408.8 | 41.9 | 31.4 | 6.3 | 26.0 | [437.8, 748.7] |
| mh_ekf | 5.8 | 4.4 | 9.2 | 11.3 | 925.7 | 0.2 | 0.1 | 0.1 | 26.0 | [10.5, 12.7] |

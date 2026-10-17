Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s668_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 85.2 | 8.7 | 22.9 | 44.6 | 4272.7 | 4.5 | 3.7 | 3.5 | 98.0 | [37.9, 50.2] |
| ekf_gated | 20.4 | 4.5 | 9.8 | 12.6 | 1364.9 | 1.3 | 1.3 | 1.3 | 3.0 | [11.2, 19.4] |
| pf_topk | 124.6 | 26.3 | 439.2 | 642.3 | 1490.9 | 33.6 | 25.6 | 8.4 | 29.0 | [533.8, 732.8] |
| mh_ekf | 5.6 | 4.2 | 8.7 | 10.8 | 1365.5 | 0.1 | 0.1 | 0.1 | 25.0 | [10.3, 11.5] |

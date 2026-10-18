Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s668_t1_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 85.6 | 8.7 | 23.8 | 45.0 | 4270.1 | 4.6 | 3.7 | 3.6 | 99.0 | [37.4, 53.8] |
| ekf_gated | 5.2 | 4.4 | 9.6 | 11.8 | 47.0 | 0.0 | 0.0 | 0.0 | 0.0 | [11.2, 12.5] |
| pf_topk | 11.7 | 5.9 | 22.3 | 42.6 | 312.2 | 3.8 | 1.4 | 0.0 | 0.0 | [25.8, 59.9] |
| mh_ekf | 4.9 | 4.2 | 9.0 | 10.9 | 54.0 | 0.0 | 0.0 | 0.0 | 0.0 | [10.2, 11.6] |

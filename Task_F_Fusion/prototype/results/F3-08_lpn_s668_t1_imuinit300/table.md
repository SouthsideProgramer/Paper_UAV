Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s668_t1_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 85.6 | 8.7 | 23.8 | 45.0 | 4270.1 | 4.6 | 3.7 | 3.6 | 99.0 | [37.4, 53.8] |
| ekf_gated | 18.8 | 4.5 | 10.1 | 12.8 | 1423.1 | 1.1 | 1.0 | 1.0 | 3.0 | [11.5, 15.8] |
| pf_topk | 120.1 | 36.9 | 368.3 | 534.3 | 1593.6 | 40.9 | 29.3 | 5.9 | 26.0 | [404.4, 672.7] |
| mh_ekf | 5.5 | 4.2 | 9.0 | 11.1 | 925.7 | 0.2 | 0.1 | 0.1 | 26.0 | [10.4, 11.8] |

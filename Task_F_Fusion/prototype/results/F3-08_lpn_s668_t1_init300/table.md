Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s668_t1_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 85.6 | 8.7 | 23.8 | 45.0 | 4270.1 | 4.6 | 3.7 | 3.6 | 99.0 | [37.4, 53.8] |
| ekf_gated | 16.3 | 2.9 | 5.8 | 7.2 | 1361.3 | 1.1 | 1.0 | 1.0 | 3.0 | [6.5, 8.4] |
| pf_topk | 6.2 | 4.2 | 10.5 | 13.5 | 911.5 | 0.4 | 0.3 | 0.0 | 8.0 | [12.5, 14.9] |
| mh_ekf | 3.6 | 2.7 | 5.3 | 6.3 | 926.1 | 0.2 | 0.1 | 0.1 | 26.0 | [5.9, 6.7] |

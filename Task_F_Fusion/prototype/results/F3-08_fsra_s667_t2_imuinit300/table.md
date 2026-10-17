Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 123.8 | 9.0 | 37.8 | 1190.7 | 4458.3 | 8.6 | 7.0 | 6.2 | 100.0 | [837.9, 1287.3] |
| ekf_gated | 79.8 | 5.2 | 14.7 | 559.2 | 1900.5 | 6.2 | 6.2 | 5.7 | 7.0 | [16.3, 1424.0] |
| pf_topk | 124.7 | 26.8 | 394.4 | 620.2 | 2128.5 | 34.5 | 25.3 | 7.0 | 23.0 | [462.5, 849.4] |
| mh_ekf | 6.5 | 4.5 | 9.8 | 12.1 | 1465.2 | 0.3 | 0.2 | 0.1 | 26.0 | [11.6, 12.9] |

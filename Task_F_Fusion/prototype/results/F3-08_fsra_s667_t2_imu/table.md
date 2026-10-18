Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t2_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 123.8 | 9.0 | 37.8 | 1190.7 | 4458.3 | 8.6 | 7.0 | 6.2 | 100.0 | [837.9, 1287.3] |
| ekf_gated | 5.9 | 4.9 | 10.8 | 13.6 | 173.4 | 0.1 | 0.0 | 0.0 | 0.0 | [12.7, 14.4] |
| pf_topk | 10.4 | 5.9 | 17.4 | 29.4 | 332.1 | 2.4 | 1.2 | 0.0 | 0.0 | [20.2, 45.5] |
| mh_ekf | 6.5 | 4.5 | 9.9 | 12.3 | 469.0 | 0.6 | 0.4 | 0.0 | 0.0 | [11.4, 14.4] |

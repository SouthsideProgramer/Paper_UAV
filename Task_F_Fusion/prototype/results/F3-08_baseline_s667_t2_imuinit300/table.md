Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 109.2 | 8.9 | 37.5 | 632.3 | 4272.7 | 8.3 | 6.2 | 5.8 | 100.0 | [586.2, 939.8] |
| ekf_gated | 33.1 | 5.0 | 13.1 | 20.3 | 1262.1 | 3.2 | 3.2 | 3.2 | 4.0 | [14.8, 596.5] |
| pf_topk | 112.6 | 25.3 | 394.2 | 605.3 | 1477.0 | 32.9 | 23.7 | 7.2 | 25.0 | [472.8, 698.8] |
| mh_ekf | 5.9 | 4.4 | 9.3 | 11.6 | 929.9 | 0.2 | 0.1 | 0.1 | 25.0 | [11.0, 12.4] |

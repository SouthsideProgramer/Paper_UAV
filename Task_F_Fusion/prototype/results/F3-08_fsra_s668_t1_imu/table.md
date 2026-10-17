Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t1_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 126.5 | 8.9 | 30.5 | 578.0 | 4459.1 | 7.5 | 5.4 | 5.1 | 100.0 | [87.5, 898.3] |
| ekf_gated | 5.6 | 4.7 | 10.6 | 13.1 | 39.4 | 0.0 | 0.0 | 0.0 | 0.0 | [12.4, 13.7] |
| pf_topk | 9.3 | 5.5 | 15.1 | 27.0 | 332.7 | 2.2 | 0.9 | 0.0 | 0.0 | [17.3, 48.3] |
| mh_ekf | 4.7 | 4.0 | 8.8 | 10.8 | 40.7 | 0.0 | 0.0 | 0.0 | 0.0 | [10.3, 11.5] |

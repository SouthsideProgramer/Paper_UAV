Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t2_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 118.0 | 8.8 | 29.2 | 69.4 | 4429.6 | 6.2 | 4.6 | 4.3 | 99.0 | [60.8, 90.0] |
| ekf_gated | 5.8 | 4.9 | 10.7 | 13.6 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | [12.9, 14.3] |
| pf_topk | 9.5 | 6.0 | 17.6 | 25.9 | 277.1 | 1.7 | 0.5 | 0.0 | 0.0 | [20.0, 34.4] |
| mh_ekf | 5.1 | 4.4 | 9.3 | 11.7 | 29.4 | 0.0 | 0.0 | 0.0 | 0.0 | [10.9, 12.6] |

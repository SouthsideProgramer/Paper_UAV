Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t0_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 119.6 | 8.8 | 29.8 | 78.7 | 4428.3 | 6.5 | 4.9 | 4.6 | 100.0 | [65.5, 586.5] |
| ekf_gated | 5.6 | 4.7 | 10.6 | 13.5 | 41.0 | 0.0 | 0.0 | 0.0 | 0.0 | [12.7, 14.3] |
| pf_topk | 10.5 | 5.8 | 16.5 | 27.6 | 527.2 | 2.4 | 0.9 | 0.0 | 1.0 | [18.5, 43.4] |
| mh_ekf | 5.0 | 4.2 | 9.4 | 11.8 | 53.9 | 0.0 | 0.0 | 0.0 | 0.0 | [11.1, 12.8] |

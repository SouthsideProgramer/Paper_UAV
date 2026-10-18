Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t1_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 124.0 | 8.9 | 29.8 | 70.9 | 4428.9 | 6.3 | 4.6 | 4.2 | 99.0 | [63.9, 102.9] |
| ekf_gated | 6.0 | 4.9 | 11.4 | 14.1 | 71.0 | 0.0 | 0.0 | 0.0 | 0.0 | [13.5, 14.8] |
| pf_topk | 10.4 | 5.7 | 17.8 | 30.8 | 374.0 | 2.7 | 1.3 | 0.0 | 0.0 | [19.7, 47.6] |
| mh_ekf | 5.4 | 4.5 | 10.1 | 12.7 | 48.5 | 0.0 | 0.0 | 0.0 | 0.0 | [11.9, 13.5] |

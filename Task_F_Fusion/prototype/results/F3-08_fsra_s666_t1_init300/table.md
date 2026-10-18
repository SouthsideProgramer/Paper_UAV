Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t1_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 124.0 | 8.9 | 29.8 | 70.9 | 4428.9 | 6.3 | 4.6 | 4.2 | 99.0 | [63.9, 102.9] |
| ekf_gated | 18.1 | 3.4 | 7.1 | 8.5 | 1437.2 | 1.0 | 1.0 | 1.0 | 2.0 | [7.6, 9.9] |
| pf_topk | 6.5 | 4.6 | 11.0 | 13.9 | 909.8 | 0.3 | 0.3 | 0.0 | 8.0 | [12.9, 15.1] |
| mh_ekf | 4.1 | 3.0 | 6.1 | 7.3 | 926.1 | 0.1 | 0.1 | 0.1 | 26.0 | [6.7, 7.9] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t2_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 118.0 | 8.8 | 29.2 | 69.4 | 4429.6 | 6.2 | 4.6 | 4.3 | 99.0 | [60.8, 90.0] |
| ekf_gated | 32.9 | 3.2 | 7.2 | 10.1 | 1301.0 | 3.0 | 3.0 | 2.9 | 5.0 | [7.7, 585.8] |
| pf_topk | 6.4 | 4.3 | 10.7 | 13.5 | 1033.8 | 0.4 | 0.3 | 0.1 | 7.0 | [12.2, 15.3] |
| mh_ekf | 4.0 | 2.8 | 5.8 | 7.0 | 1128.3 | 0.2 | 0.2 | 0.1 | 25.0 | [6.6, 7.3] |

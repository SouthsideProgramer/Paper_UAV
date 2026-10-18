Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 118.0 | 8.8 | 29.2 | 69.4 | 4429.6 | 6.2 | 4.6 | 4.3 | 99.0 | [60.8, 90.0] |
| ekf_gated | 27.6 | 5.0 | 11.8 | 16.0 | 1318.7 | 2.0 | 2.0 | 2.0 | 5.0 | [13.7, 20.9] |
| pf_topk | 117.6 | 26.0 | 399.7 | 597.9 | 1474.4 | 33.8 | 25.5 | 7.0 | 23.0 | [456.9, 712.8] |
| mh_ekf | 6.0 | 4.4 | 9.4 | 12.0 | 1128.7 | 0.2 | 0.2 | 0.1 | 25.0 | [11.1, 12.8] |

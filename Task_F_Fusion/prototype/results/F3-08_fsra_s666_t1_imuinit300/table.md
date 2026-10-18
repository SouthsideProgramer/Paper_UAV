Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t1_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 124.0 | 8.9 | 29.8 | 70.9 | 4428.9 | 6.3 | 4.6 | 4.2 | 99.0 | [63.9, 102.9] |
| ekf_gated | 18.6 | 4.9 | 11.8 | 15.1 | 1418.3 | 1.0 | 1.0 | 1.0 | 2.0 | [13.6, 18.8] |
| pf_topk | 128.0 | 37.3 | 398.8 | 568.6 | 1564.4 | 41.8 | 30.2 | 6.7 | 29.0 | [450.7, 699.0] |
| mh_ekf | 6.1 | 4.5 | 10.2 | 12.9 | 925.7 | 0.2 | 0.1 | 0.1 | 26.0 | [12.0, 13.7] |

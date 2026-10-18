Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 74.2 | 8.8 | 28.0 | 65.8 | 4442.3 | 5.9 | 3.8 | 3.3 | 87.0 | [53.0, 74.5] |
| ekf_gated | 22.1 | 4.8 | 11.3 | 16.1 | 1262.1 | 2.1 | 2.0 | 2.0 | 3.0 | [13.3, 27.8] |
| pf_topk | 109.6 | 25.9 | 375.8 | 572.0 | 1446.9 | 32.6 | 24.2 | 6.4 | 24.0 | [427.6, 661.4] |
| mh_ekf | 6.1 | 4.5 | 9.7 | 12.4 | 929.9 | 0.2 | 0.2 | 0.1 | 25.0 | [11.7, 13.4] |

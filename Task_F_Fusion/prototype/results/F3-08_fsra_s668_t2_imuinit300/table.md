Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 126.4 | 8.9 | 32.5 | 712.8 | 4458.9 | 7.8 | 5.7 | 5.4 | 100.0 | [100.8, 927.0] |
| ekf_gated | 49.1 | 4.9 | 12.7 | 23.8 | 1617.7 | 4.3 | 4.3 | 4.3 | 5.0 | [13.9, 934.5] |
| pf_topk | 120.0 | 26.4 | 405.7 | 600.0 | 1491.7 | 34.4 | 25.7 | 7.3 | 27.0 | [464.6, 712.1] |
| mh_ekf | 5.4 | 4.0 | 8.3 | 10.4 | 932.6 | 0.2 | 0.2 | 0.1 | 24.0 | [9.8, 11.0] |

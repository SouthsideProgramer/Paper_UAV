Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 8, "n_boot": 200, "tag": "F3-08_lpn_s666_t2_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 73.4 | 8.6 | 23.7 | 65.4 | 4294.0 | 5.8 | 4.4 | 3.8 | 100.0 | [55.6, 75.6] |
| ekf_gated | 34.5 | 4.5 | 10.6 | 16.6 | 1318.7 | 3.3 | 3.3 | 2.9 | 4.0 | [11.9, 607.2] |
| pf_topk | 102.8 | 26.3 | 332.3 | 526.0 | 1518.5 | 32.7 | 22.8 | 5.5 | 21.0 | [387.7, 650.8] |
| mh_ekf | 5.6 | 4.2 | 8.9 | 11.1 | 929.9 | 0.1 | 0.1 | 0.1 | 24.0 | [10.4, 11.9] |

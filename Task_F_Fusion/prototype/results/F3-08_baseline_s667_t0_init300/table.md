Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t0_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 122.3 | 8.9 | 44.0 | 987.9 | 4269.0 | 9.2 | 6.8 | 6.5 | 100.0 | [859.6, 1260.9] |
| ekf_gated | 23.2 | 3.2 | 6.8 | 9.4 | 1291.0 | 2.1 | 2.1 | 2.0 | 3.0 | [7.7, 180.3] |
| pf_topk | 6.1 | 4.4 | 10.5 | 13.5 | 686.6 | 0.4 | 0.3 | 0.0 | 6.0 | [12.2, 15.2] |
| mh_ekf | 3.8 | 2.7 | 5.4 | 6.5 | 1557.3 | 0.2 | 0.1 | 0.1 | 19.0 | [6.1, 6.8] |

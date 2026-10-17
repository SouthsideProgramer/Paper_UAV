Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s668_t1_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 119.5 | 8.9 | 29.3 | 114.2 | 4459.1 | 7.1 | 5.3 | 4.7 | 100.0 | [77.3, 604.3] |
| ekf_gated | 30.3 | 3.3 | 6.6 | 8.3 | 1409.5 | 2.1 | 2.0 | 2.0 | 3.0 | [7.1, 633.8] |
| pf_topk | 6.4 | 4.5 | 10.9 | 13.9 | 911.5 | 0.4 | 0.3 | 0.0 | 9.0 | [12.8, 15.1] |
| mh_ekf | 3.8 | 2.8 | 5.2 | 6.1 | 926.1 | 0.2 | 0.1 | 0.1 | 26.0 | [5.8, 6.5] |

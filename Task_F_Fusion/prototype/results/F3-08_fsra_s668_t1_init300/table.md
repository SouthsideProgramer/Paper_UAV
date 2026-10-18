Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s668/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s668_t1_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 126.5 | 8.9 | 30.5 | 578.0 | 4459.1 | 7.5 | 5.4 | 5.1 | 100.0 | [87.5, 898.3] |
| ekf_gated | 27.8 | 3.2 | 6.4 | 7.8 | 1651.6 | 2.0 | 2.0 | 2.0 | 5.0 | [6.9, 537.9] |
| pf_topk | 6.4 | 4.4 | 10.7 | 13.6 | 911.4 | 0.4 | 0.3 | 0.0 | 9.0 | [12.5, 15.0] |
| mh_ekf | 3.9 | 2.7 | 5.2 | 6.2 | 926.1 | 0.2 | 0.2 | 0.1 | 27.0 | [5.8, 6.5] |

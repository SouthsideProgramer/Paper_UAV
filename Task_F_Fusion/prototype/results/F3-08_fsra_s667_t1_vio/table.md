Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t1_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 118.5 | 9.0 | 36.1 | 944.8 | 4459.1 | 8.4 | 6.7 | 5.7 | 100.0 | [537.5, 1208.0] |
| ekf_gated | 3.4 | 3.0 | 6.0 | 7.2 | 21.8 | 0.0 | 0.0 | 0.0 | 0.0 | [6.8, 7.5] |
| pf_topk | 3.2 | 2.9 | 5.6 | 6.6 | 21.0 | 0.0 | 0.0 | 0.0 | 0.0 | [6.3, 6.9] |
| mh_ekf | 3.3 | 3.0 | 5.7 | 6.7 | 20.8 | 0.0 | 0.0 | 0.0 | 0.0 | [6.4, 6.9] |

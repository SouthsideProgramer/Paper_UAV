Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/baseline_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_baseline_s667_t2_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 109.2 | 8.9 | 37.5 | 632.3 | 4272.7 | 8.3 | 6.2 | 5.8 | 100.0 | [586.2, 939.8] |
| ekf_gated | 3.4 | 3.0 | 6.0 | 7.2 | 29.1 | 0.0 | 0.0 | 0.0 | 0.0 | [6.9, 7.7] |
| pf_topk | 3.0 | 2.6 | 5.2 | 6.2 | 26.2 | 0.0 | 0.0 | 0.0 | 0.0 | [5.9, 6.5] |
| mh_ekf | 3.0 | 2.7 | 5.3 | 6.2 | 25.7 | 0.0 | 0.0 | 0.0 | 0.0 | [5.9, 6.5] |

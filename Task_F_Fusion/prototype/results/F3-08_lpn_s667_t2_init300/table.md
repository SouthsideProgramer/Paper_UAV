Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t2_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 74.2 | 8.8 | 28.0 | 65.8 | 4442.3 | 5.9 | 3.8 | 3.3 | 87.0 | [53.0, 74.5] |
| ekf_gated | 26.9 | 3.0 | 6.3 | 8.4 | 1262.1 | 2.9 | 2.9 | 2.9 | 3.0 | [6.9, 571.6] |
| pf_topk | 12.0 | 4.2 | 10.7 | 15.0 | 888.2 | 1.5 | 1.3 | 1.0 | 7.0 | [12.3, 21.6] |
| mh_ekf | 4.0 | 2.8 | 5.5 | 6.7 | 930.4 | 0.2 | 0.2 | 0.1 | 25.0 | [6.2, 7.2] |

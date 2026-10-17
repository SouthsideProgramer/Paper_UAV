Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t1_init300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 60.8 | 8.8 | 27.7 | 55.4 | 4443.2 | 5.4 | 3.1 | 2.6 | 82.0 | [48.2, 69.2] |
| ekf_gated | 3.7 | 3.1 | 6.3 | 7.4 | 83.8 | 0.2 | 0.0 | 0.0 | 0.0 | [7.1, 7.8] |
| pf_topk | 6.4 | 4.5 | 10.7 | 14.0 | 911.5 | 0.4 | 0.3 | 0.0 | 6.0 | [12.7, 15.6] |
| mh_ekf | 3.9 | 3.0 | 5.9 | 6.9 | 926.1 | 0.1 | 0.1 | 0.1 | 26.0 | [6.5, 7.3] |

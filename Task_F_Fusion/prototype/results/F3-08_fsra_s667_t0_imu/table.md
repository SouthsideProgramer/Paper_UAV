Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 4, "n_boot": 200, "tag": "F3-08_fsra_s667_t0_imu", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 140.0 | 9.0 | 47.8 | 1290.8 | 4458.7 | 9.7 | 7.9 | 7.1 | 100.0 | [1220.0, 1302.9] |
| ekf_gated | 5.8 | 4.8 | 10.7 | 13.6 | 69.8 | 0.0 | 0.0 | 0.0 | 0.0 | [12.7, 14.5] |
| pf_topk | 9.6 | 6.2 | 15.9 | 24.1 | 322.1 | 1.6 | 0.7 | 0.0 | 0.0 | [18.4, 35.9] |
| mh_ekf | 5.3 | 4.5 | 9.6 | 11.9 | 37.6 | 0.0 | 0.0 | 0.0 | 0.0 | [11.2, 12.7] |

Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 1, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t1_imuinit300", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 60.8 | 8.8 | 27.7 | 55.4 | 4443.2 | 5.4 | 3.1 | 2.6 | 82.0 | [48.2, 69.2] |
| ekf_gated | 6.0 | 4.8 | 11.1 | 14.3 | 137.8 | 0.2 | 0.0 | 0.0 | 0.0 | [13.2, 15.4] |
| pf_topk | 129.0 | 38.7 | 406.4 | 567.4 | 1446.1 | 42.6 | 31.0 | 6.7 | 29.0 | [442.1, 725.1] |
| mh_ekf | 6.2 | 4.6 | 10.2 | 12.8 | 925.7 | 0.2 | 0.2 | 0.1 | 26.0 | [12.1, 13.7] |

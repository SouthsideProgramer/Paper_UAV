Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/lpn_s667/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 4, "n_boot": 200, "tag": "F3-08_lpn_s667_t2_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 74.2 | 8.8 | 28.0 | 65.8 | 4442.3 | 5.9 | 3.8 | 3.3 | 87.0 | [53.0, 74.5] |
| ekf_gated | 3.4 | 3.0 | 5.8 | 6.9 | 25.7 | 0.0 | 0.0 | 0.0 | 0.0 | [6.5, 7.2] |
| pf_topk | 3.0 | 2.7 | 5.3 | 6.5 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | [6.1, 6.9] |
| mh_ekf | 3.1 | 2.8 | 5.4 | 6.5 | 31.9 | 0.0 | 0.0 | 0.0 | 0.0 | [6.1, 7.0] |

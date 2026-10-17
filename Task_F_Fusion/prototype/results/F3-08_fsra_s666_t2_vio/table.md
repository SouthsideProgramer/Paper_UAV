Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 2, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t2_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 118.0 | 8.8 | 29.2 | 69.4 | 4429.6 | 6.2 | 4.6 | 4.3 | 99.0 | [60.8, 90.0] |
| ekf_gated | 3.6 | 3.1 | 6.4 | 7.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | [7.3, 8.3] |
| pf_topk | 3.1 | 2.7 | 5.7 | 7.0 | 25.2 | 0.0 | 0.0 | 0.0 | 0.0 | [6.5, 7.5] |
| mh_ekf | 3.2 | 2.8 | 5.7 | 6.8 | 26.0 | 0.0 | 0.0 | 0.0 | 0.0 | [6.5, 7.3] |

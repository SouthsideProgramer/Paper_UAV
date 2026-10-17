Config: `{"world": "real", "result_mat": "../../../DenseUAV_b8de187/checkpoints/fsra/pytorch_result_1.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "campuses": "test", "seed": 0, "workers": 8, "n_boot": 200, "tag": "F3-08_fsra_s666_t0_vio", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 119.6 | 8.8 | 29.8 | 78.7 | 4428.3 | 6.5 | 4.9 | 4.6 | 100.0 | [65.5, 586.5] |
| ekf_gated | 3.6 | 3.1 | 6.4 | 7.8 | 27.1 | 0.0 | 0.0 | 0.0 | 0.0 | [7.3, 8.5] |
| pf_topk | 3.1 | 2.7 | 5.6 | 6.9 | 24.1 | 0.0 | 0.0 | 0.0 | 0.0 | [6.4, 7.3] |
| mh_ekf | 3.2 | 2.8 | 5.5 | 6.8 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | [6.1, 7.6] |

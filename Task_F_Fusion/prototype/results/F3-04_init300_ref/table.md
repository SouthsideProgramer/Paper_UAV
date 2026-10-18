Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 300, "tag": "F3-04_init300_ref", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1610.2 | 772.0 | 4608.6 | 4919.3 | 5428.3 | 67.9 | 63.1 | 54.4 | 100.0 | [4879.8, 4964.3] |
| ekf_gated | 251.4 | 9.7 | 954.5 | 1336.6 | 1576.0 | 28.6 | 27.7 | 23.3 | 30.0 | [947.6, 1381.3] |
| pf_topk | 51.1 | 7.6 | 126.4 | 490.1 | 1345.2 | 12.3 | 11.1 | 4.2 | 22.0 | [124.1, 607.2] |

Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 300, "tag": "F3-04_imu_ref", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1610.2 | 772.0 | 4608.6 | 4919.3 | 5428.3 | 67.9 | 63.1 | 54.4 | 100.0 | [4879.8, 4964.3] |
| ekf_gated | 29.4 | 13.7 | 53.1 | 128.4 | 875.9 | 10.7 | 6.3 | 0.3 | 2.0 | [75.2, 173.6] |
| pf_topk | 24.4 | 11.3 | 35.3 | 50.6 | 1342.3 | 5.1 | 2.6 | 0.6 | 1.0 | [40.0, 138.4] |

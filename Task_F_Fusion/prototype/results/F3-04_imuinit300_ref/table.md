Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk", "campuses": "val", "seed": 0, "workers": 11, "n_boot": 300, "tag": "F3-04_imuinit300_ref", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1610.2 | 772.0 | 4608.6 | 4919.3 | 5428.3 | 67.9 | 63.1 | 54.4 | 100.0 | [4879.8, 4964.3] |
| ekf_gated | 291.0 | 20.1 | 1043.3 | 1393.5 | 3177.5 | 33.9 | 30.4 | 23.9 | 33.0 | [1038.1, 1572.1] |
| pf_topk | 206.9 | 66.0 | 650.4 | 845.8 | 1721.1 | 56.3 | 43.3 | 14.2 | 46.0 | [710.8, 1022.8] |

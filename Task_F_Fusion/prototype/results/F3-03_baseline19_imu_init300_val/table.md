Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,dead_reckoning,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-03_baseline19_imu_init300_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1264.5 | 613.1 | 3803.1 | 4437.2 | 5436.5 | 67.2 | 60.3 | 51.9 | 100.0 | [4201.5, 4700.9] |
| dead_reckoning | 438.8 | 415.3 | 735.4 | 860.5 | 1637.0 | 99.3 | 96.9 | 34.7 | 66.0 | [756.7, 955.5] |
| ekf_gated | 292.9 | 24.9 | 1071.1 | 1383.0 | 2816.0 | 38.0 | 34.0 | 23.4 | 34.0 | [1070.4, 1576.7] |
| pf_topk | 242.0 | 96.8 | 724.0 | 1033.3 | 1978.8 | 61.6 | 49.5 | 16.8 | 49.0 | [762.7, 1167.3] |
| mh_ekf | 65.5 | 11.0 | 38.6 | 149.9 | 2424.4 | 8.2 | 5.9 | 3.9 | 44.0 | [49.8, 1196.9] |

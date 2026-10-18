Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "imu", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-02_baseline19_imu_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1264.5 | 613.1 | 3803.1 | 4437.2 | 5436.5 | 67.2 | 60.3 | 51.9 | 100.0 | [4201.5, 4700.9] |
| ekf_gated | 44.8 | 15.9 | 89.6 | 171.7 | 2231.2 | 14.5 | 9.5 | 0.7 | 2.0 | [128.5, 221.6] |
| pf_topk | 28.0 | 14.3 | 55.0 | 107.4 | 513.5 | 11.3 | 5.5 | 0.0 | 1.0 | [64.0, 162.1] |
| mh_ekf | 47.5 | 10.1 | 27.3 | 43.2 | 5119.0 | 4.4 | 2.6 | 1.5 | 14.0 | [32.5, 80.5] |

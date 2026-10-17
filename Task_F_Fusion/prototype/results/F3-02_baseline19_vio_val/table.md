Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 10.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-02_baseline19_vio_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1264.5 | 613.1 | 3803.1 | 4437.2 | 5436.5 | 67.2 | 60.3 | 51.9 | 100.0 | [4201.5, 4700.9] |
| ekf_gated | 17.0 | 8.4 | 27.8 | 66.9 | 257.1 | 6.0 | 4.2 | 0.0 | 0.0 | [39.5, 121.3] |
| pf_topk | 6.7 | 5.8 | 12.1 | 14.7 | 45.1 | 0.0 | 0.0 | 0.0 | 0.0 | [13.9, 15.9] |
| mh_ekf | 37.5 | 5.9 | 12.3 | 15.3 | 5081.2 | 1.5 | 1.4 | 1.4 | 16.0 | [13.8, 17.9] |

Config: `{"world": "real", "result_mat": "../../Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat", "gps_path": "../../datasets/DenseUAV/Dense_GPS_ALL.txt", "preset": "fsra", "motion": "vio", "imu_grade": "consumer", "n_traj": 100, "T": 300.0, "meas_every": 1, "init_err": 300.0, "snap": 20.0, "K": 10, "persist": 0.5, "p_true_in_topk": 0.5, "anchor_truth": 0.5, "methods": "retrieval_top1,ekf_gated,pf_topk,mh_ekf", "seed": 0, "workers": 11, "n_boot": 1000, "tag": "F3-02_baseline19_init300_val", "cfg": ""}`

| Method | mean | p50 | p90 | p95 | max | GFR@50 | GFR@100 | GFR@500 | traj_catastrophic_pct | p95 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval_top1 | 1264.5 | 613.1 | 3803.1 | 4437.2 | 5436.5 | 67.2 | 60.3 | 51.9 | 100.0 | [4201.5, 4700.9] |
| ekf_gated | 267.5 | 12.2 | 975.3 | 1284.3 | 1628.2 | 33.2 | 31.5 | 25.0 | 32.0 | [972.7, 1489.9] |
| pf_topk | 72.9 | 8.3 | 183.0 | 644.7 | 1415.2 | 15.0 | 13.8 | 7.3 | 30.0 | [184.3, 842.2] |
| mh_ekf | 53.6 | 6.1 | 14.2 | 30.3 | 5081.2 | 4.3 | 4.0 | 2.8 | 51.0 | [18.6, 156.2] |

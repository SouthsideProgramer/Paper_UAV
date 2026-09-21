# Task K: Evaluation Track Workspace (Khải)

Thư mục chứa toàn bộ mã nguồn, dữ liệu thực nghiệm và báo cáo phân tích cho **5 Task đánh giá (Evaluation Track)**:

---

### Cấu trúc thư mục:

```
Task_K/
├── Task_K1/    # Script đánh giá metric không gian & CIs (eval_metrics.py)
│   ├── eval_metrics.py
│   ├── results.json
│   ├── errors.npy
│   └── results.txt
│
├── Task_K2/    # Đánh giá 4 Baseline & Vẽ biểu đồ CDF dải K > s
│   ├── run_baseline_eval.py
│   ├── plot_fig1_cdf.py
│   └── baseline_summary.json
│
├── Task_K3/    # Phân tích địa hình (Texture Proxy) & Hồi quy Logistic
│   ├── texture_analysis.py
│   └── texture_analysis_results.json
│
├── Task_K4/    # Khảo sát mô hình SQCLoc & Ghi chú Limitations
│   └── sqcloc_survey_notes.md
│
└── Task_K5/    # Spatial Confidence Gating (Section 8.1) & FPI Continuous Loader
    ├── spatial_confidence_gating.py
    ├── spatial_gating_results.json
    ├── fpi_loader.py
    └── weighted_centroid_results.json
```

---

### Hướng dẫn chạy nhanh:

1. **Task K1 (Tính Metric cho 1 model)**:
   ```bash
   python Task_K/Task_K1/eval_metrics.py --result_mat checkpoints/baseline_vits_single/pytorch_result_1.mat
   ```

2. **Task K2 (Đánh giá toàn bộ 4 baseline & vẽ CDF)**:
   ```bash
   python Task_K/Task_K2/run_baseline_eval.py
   python Task_K/Task_K2/plot_fig1_cdf.py --lang en
   ```

3. **Task K3 (Hồi quy Logistic địa hình)**:
   ```bash
   python Task_K/Task_K3/texture_analysis.py --model all
   ```

4. **Task K5 (Spatial Confidence Gating)**:
   ```bash
   python Task_K/Task_K5/spatial_confidence_gating.py
   ```

# Tests & Evaluation Scripts Directory

Thư mục chứa các script kiểm thử và đánh giá benchmark truyền thống:

---

### Cấu trúc phân nhóm:

```
tests/
├── retrieval/                      # Đánh giá truy hồi đặc trưng
│   └── evaluate_gpu.py             # Tính CMC, Recall@1, Recall@5, Recall@10, mAP
│
├── distance/                       # Đánh giá khoảng cách không gian
│   ├── evaluateDistance.py         # Tính SDM & Euclidean distance giữa query và gallery
│   ├── evaluateDistance_DifHeight.py # Đánh giá SDM phân tách theo từng độ cao bay
│   ├── evaluateMA.py               # Tính Meter Accuracy (MA@K)
│   └── evaluateMA_dense.py         # Tính MA@K trên tập DenseUAV
│
├── continuous/                     # Đánh giá tọa độ liên tục
│   └── evaluate_RDS.py             # Tính Relative Distance Score (RDS) trên FPI/SiamUAV
│
└── experimental/                   # Các thử nghiệm & trực quan hóa
    ├── eval_weighted_centroid.py   # Thử nghiệm giải mã trọng tâm có trọng số
    └── heatmap.py                  # Trực quan hóa bản đồ nhiệt (Heatmap)
```

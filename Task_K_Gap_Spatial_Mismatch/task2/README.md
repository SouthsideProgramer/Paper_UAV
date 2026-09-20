# Task 2: Đo lường Độ Phân Tán Không Gian trong Top-K (Spatial Dispersion Analysis)

## 1. Mục tiêu Nghiên cứu & Giả thuyết
Thực nghiệm Task 2 nhằm kiểm chứng luận điểm thứ hai của **Research Gap 1 (Spatial Mismatch)**:
* **Hiện tượng Phân mảnh Không gian (Spatial Dispersion / Fragmentation):** Trong các mô hình UAV Visual Geo-localization truyền thống, các ứng viên trong Top-$K$ ($K=3, 5, 10$) tuy có điểm số tương đồng thị giác xấp xỉ nhau ($s_i \approx s_j$), nhưng thực tế ngoài thực địa lại **bị phân tán rải rác trên khắp bản đồ** với bán kính hàng kilomet thay vì gom tụ chặt chẽ thành cụm cục bộ (compact spatial cluster) quanh vị trí thực tế của UAV.
* **Hậu quả:** Sự phân tán này là nguyên nhân trực tiếp khiến các phương pháp gán tọa độ hoặc kết hợp Top-$K$ (như Weighted Centroid) bị kéo lệch vào các tọa độ "ảo" ở giữa các cụm cách xa nhau.

---

## 2. Phương pháp luận & Công thức Toán học

### 2.1. Đường kính Phân tán Cụm Tối đa ($D_{max}^{(K)}$)
Với mỗi truy vấn query ảnh drone, tập Top-$K$ ứng viên có điểm tương đồng thị giác cao nhất tương ứng với các tọa độ địa lý $\{p_1, p_2, \dots, p_K\}$ trên bản đồ:
$$D_{max}^{(K)} = \max_{i, j \in \{1, \dots, K\}} \text{Haversine}(p_i, p_j)$$
* $D_{max}^{(K)}$ đo khoảng cách vật lý xa nhất giữa hai ứng viên bất kỳ trong cùng một nhóm Top-$K$.
* Nếu các ứng viên cùng nhận diện đúng một khu vực cảnh quan: $D_{max}^{(K)} < 100\text{ m}$.
* Nếu các ứng viên bị phân mảnh liên trường đại học (Cross-Campus Mismatch): $D_{max}^{(K)} > 1000\text{ m}$.

### 2.2. Độ Lệch Chuẩn Cự ly Địa lý ($\sigma_{geo}^{(K)}$)
Đo độ phân tán của $K$ ứng viên so với tâm hình học của cụm ($\bar{p} = (\bar{\text{lat}}, \bar{\text{lon}})$):
$$\sigma_{geo}^{(K)} = \sqrt{\frac{1}{K} \sum_{i=1}^K \text{Haversine}(p_i, \bar{p})^2}$$
Giá trị $\sigma_{geo}$ càng lớn chứng tỏ cụm ứng viên càng loãng và thiếu tính tập trung địa lý.

### 2.3. Tỷ lệ Ứng viên Nằm Ngoài Bán kính An toàn
Thống kê tỷ lệ phần trăm các ứng viên trong Top-$K$ có khoảng cách trắc địa tới vị trí thực tế của drone ($p_{query}$) vượt ngưỡng an toàn ($100\text{ m}$, $500\text{ m}$, $1000\text{ m}$):
$$P(d > \text{threshold}) = \frac{\sum_{q=1}^{N_q} \sum_{i=1}^K \mathbb{I}(\text{Haversine}(p_{query}, p_i) > \text{threshold})}{N_q \times K} \times 100\%$$

---

## 3. Cấu trúc Thư mục Task 2
```text
Task_K_Gap_Spatial_Mismatch/task2/
├── README.md                          # Tài liệu báo cáo và phân tích kết quả thực nghiệm
├── task2_topk_dispersion.py           # Mã nguồn phân tích độ phân tán không gian Top-K
└── results/
    ├── dispersion_metrics.csv         # Bảng tổng hợp số liệu phân vị (Median, Mean, p90, p95)
    └── dispersion_report.json         # File JSON chi tiết đầy đủ 2.331 query test
```

---

## 4. Hướng dẫn Thực thi

### Lệnh chạy mặc định trên Checkpoint Chuẩn (Baseline ViT-S):
```bash
python task2/task2_topk_dispersion.py \
    --mat_path ../data/pytorch_result.mat \
    --gps_path ../data/Dense_GPS_ALL.txt \
    --ks "3,5,10" \
    --output_dir task2/results
```

---

## 5. Kết quả Thực nghiệm Nghiệm thu trên Benchmark DenseUAV

Thực nghiệm được thực hiện trên toàn bộ **2.331 query ảnh drone** và **18.198 gallery tiles vệ tinh** thuộc tập test của benchmark DenseUAV sử dụng checkpoint chuẩn `DenseUAV Baseline ViT-S` ($D=512$).

### 5.1. Bảng Thống kê Độ Phân tán Không gian (`dispersion_metrics.csv`)

| Top-$K$ | Mean Đường kính $D_{max}$ | Median $D_{max}$ | Phân vị 90% (p90) | Phân vị 95% (p95) | Độ lệch chuẩn cự ly $\sigma_{geo}$ | % Ứng viên văng ngoài 100m | % Ứng viên văng ngoài 500m | % Cụm bị xé lẻ $> 1000\text{ m}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Top-3** | **1,199.29 m** | 283.41 m | **3,715.93 m** | **4,152.29 m** | 553.83 m | **64.69%** | **56.11%** | **42.73%** |
| **Top-5** | **1,806.23 m** | **1,512.78 m** | **4,067.01 m** | **4,692.77 m** | **764.72 m** | **66.31%** | **57.93%** | **62.21%** |
| **Top-10** | **2,745.07 m** | **2,982.15 m** | **4,837.66 m** | **5,127.19 m** | **1,033.00 m** | **69.47%** | **60.78%** | **84.73%** |

---

### 5.2. Đối chiếu Tiêu chuẩn Nghiệm thu GAP 1

| Tiêu chí Kiểm định (Criteria) | Ngưỡng yêu cầu trong README | Giá trị Thực nghiệm Đạt được | Kết luận |
| :--- | :---: | :---: | :---: |
| **Tiêu chí 1: Đường kính cụm trung bình Top-5** | Mean $D_{max}^{(5)} > 300\text{ m}$ | **1,806.23 m** *(gấp 6 lần ngưỡng yêu cầu!)* | **ĐẠT (CONFIRMED)** |
| **Tiêu chí 2: Hiện tượng cụm xé lẻ sang trường khác** | Xuất hiện nhiều cụm $D_{max} > 1000\text{ m}$ | **62.21%** số cụm Top-5 có $D_{max} > 1000\text{ m}$ | **ĐẠT (CONFIRMED)** |
| **Tiêu chí Bổ trợ: Cực hạn sai số đuôi p95** | Rủi ro đuôi nghiêm trọng | $D_{max}^{(5)}$ tại $p95$ đạt **4,692.77 m** | **ĐẠT (CONFIRMED)** |

> **KẾT LUẬN NGHIỆM THU:** **Luận điểm Spatial Dispersion của Research Gap 1 là HOÀN TOÀN CHÍNH XÁC.**
> Các ứng viên có điểm số thị giác bám đuổi nhau sít sao trong Top-5 không hề gom cụm quanh drone mà bị phân tán với đường kính trung bình lên tới **1.8 km**. Có tới **62.21%** số trường hợp các ứng viên Top-5 bị rơi rải rác sang các khuôn viên đại học khác nhau.

---

## 6. Phân tích Định tính Các Ca Điển hình (Case Studies)

Trích xuất trực tiếp từ file `dispersion_report.json`:

### Ca 1: Query Index #1 (Class ID: 2256)
* **Top-5 Visual Similarities:** `[0.6275, 0.6124, 0.6091, 0.6022, 0.5841]` (Điểm cosine chênh lệch nhau chưa tới 0.04)
* **Khoảng cách từ các ứng viên tới Drone:** `[5219.22m, 5238.92m, 5013.17m, 5219.22m, 5238.92m]`
* **Đường kính phân tán $D_{max}^{(5)}$:** **1,512.78 mét**.
* **Phân tích:** Dù 5 ứng viên đều có điểm tương đồng rất cao (> 0.58), cụm ứng viên trải dài trên phạm vi hơn 1.5 km, chứng tỏ mô hình bị đánh lừa bởi kết cấu thị giác chung của trường học và kéo các ứng viên từ nhiều địa điểm xa xôi vào Top-5.

### Ca 2: Hiện tượng bùng nổ phân tán khi mở rộng từ Top-3 lên Top-5 và Top-10
* Tại $K=3$: Đường kính phân tán trung bình đã là **1,199.29 m** với 42.73% cụm vượt 1 km.
* Tại $K=5$: Đường kính vọt lên **1,806.23 m** với 62.21% cụm vượt 1 km.
* Tại $K=10$: Đường kính trung bình lên tới **2,745.07 m** và có tới **84.73%** số cụm có ứng viên cách nhau trên 1 km.
* **Ý nghĩa:** Điều này giải thích tại sao bất kỳ thuật toán nội suy nào dựa trên việc mở rộng Top-$K$ (như $K=5, 10$) mà không có bộ lọc địa lý (spatial constraint) đều sẽ kéo sai số định vị bùng nổ thảm khốc (dẫn tới Task 3: Naive Centroid Crash).

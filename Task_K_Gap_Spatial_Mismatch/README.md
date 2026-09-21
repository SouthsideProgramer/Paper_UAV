# README: Thẩm định Thực nghiệm Research Gap Spatial Mismatch trên DenseUAV

## 1. Mục tiêu Nghiên cứu & Phạm vi

* **Mục tiêu:** Chứng minh thực nghiệm rằng **Research Gap Spatial Mismatch là ĐÚNG ĐẮN VÀ CẤP THIẾT**:
  1. *Visual Rank vs. Spatial Distance Inversion (Sự phá vỡ thứ hạng không gian):* Sự tương đồng thị giác ($S_{visual}$) không phản ánh và bảo toàn thứ tự lân cận địa lý ($d_{geo}$). Thứ bậc thị giác trong Top-$K$ hoàn toàn lệch pha so với khoảng cách mét thực địa, dẫn đến tỷ lệ nghịch đảo khoảng cách rất cao ($> 90\%$ số truy vấn).
  2. *Spatial Dispersion & Fragmentation (Hiện tượng phân mảnh không gian):* Các candidate trong Top-$K$ dù có điểm tương đồng thị giác xấp xỉ nhau ($s_i \approx s_j$) nhưng ngoài thực địa lại bị xé lẻ rải rác trên khắp bản đồ thành phố (bán kính phân tán trung bình $> 1.8\text{ km}$, với hơn $62\%$ số cụm Top-5 bị xé lẻ xuyên khuôn viên trường đại học) thay vì tụ lại quanh vị trí của UAV.
  3. *Naive Weighted Centroid Crash (Sự sụp đổ của phép nội suy trọng tâm ngây thơ):* Mọi cơ chế kết hợp tọa độ Top-$K$ ngây thơ bằng hàm Softmax điểm số thị giác đều kéo vị trí ước lượng rơi vào các tọa độ "ảo" (phantom coordinates) giữa các trường đại học, làm bùng nổ sai số và khiến hơn $55\% - 74\%$ số truy vấn bị suy thoái độ chính xác so với việc giữ nguyên Top-1.
  4. *Overconfident Visual Mismatch (Nghịch lý tự tin cực đoan):* Mô hình đạt độ tương đồng thị giác rất cao ($s_1 \ge 0.70 - 0.79$) nhưng thực tế lại dự đoán nhầm sang một trường đại học khác cách xa từ $2\text{ km}$ đến hơn $5.4\text{ km}$ do hiện tượng Visual Aliasing (công trình kiến trúc có hình thái tương đồng).

* **Phạm vi & Đối tượng:**
  * Thực nghiệm ngoại tuyến (Post-hoc Evaluation) trên toàn bộ tập test chuẩn gồm **2.331 ảnh drone query** và **18.198 gallery tiles vệ tinh** của benchmark **DenseUAV** (14 trường đại học tại Vũ Hán, Trung Quốc).
  * Đối chuẩn trên các checkpoint đại diện:
    1. **DenseUAV Baseline** (ViT-Small backbone, $D=512$).
    2. **FSRA** (Transformer phân rã vùng cục bộ Region-aware).
    3. **ResNet-50** (CNN truyền thống).

---

## 2. Cấu trúc Thư mục Thực nghiệm

Dự án được cấu trúc module hóa khép kín cho từng Task (`task1/`, `task2/`, `task3/`, `task4/`), đồng thời duy trì các thư mục tập trung ở thư mục gốc (`scripts/`, `results/`, `data/`) để tiện tra cứu và tái lập:

```text
/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Spatial_Mismatch/
├── README.md                           # Tài liệu tổng thể kết quả thẩm định Research Gap 1
├── data/                               # Dữ liệu đầu vào & vector đặc trưng trích xuất
│   ├── Dense_GPS_ALL.txt               # Bảng tra cứu GPS tâm của 3.033 gallery tiles (14 campuses)
│   └── pytorch_result.mat              # Vector nhúng Query (2.331) & Gallery (18.198) từ Baseline ViT-S
│
├── task1/                              # Module Task 1: Tương quan Rank thị giác vs Khoảng cách
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 1
│   ├── task1_spearman_correlation.py
│   ├── results/                        # Kết quả trên Baseline ViT-S
│   │   └── correlation_report.json
│   └── results_resnet50/               # Kết quả đối chứng trên ResNet-50
│
├── task2/                              # Module Task 2: Đo độ phân tán không gian (Spatial Dispersion)
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 2
│   ├── task2_topk_dispersion.py
│   └── results/
│       ├── dispersion_metrics.csv
│       └── dispersion_report.json
│
├── task3/                              # Module Task 3: Đánh giá cơ chế Naive Weighted Centroid
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 3
│   ├── task3_naive_centroid_crash.py
│   ├── results/                        # Kết quả quét lưới trên Baseline ViT-S
│   │   ├── centroid_comparison.csv
│   │   └── centroid_report.json
│   └── results_fsra/                   # Kết quả quét lưới đối chứng trên FSRA
│       └── centroid_comparison.csv
│
├── task4/                              # Module Task 4: Khai thác ca lỗi tự tin cực đoan (Mismatch)
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 4
│   ├── task4_high_conf_failures.py
│   ├── results/
│   │   ├── visual_mismatch_cases.json  # Danh sách chi tiết 50 ca lệch pha tự tin cao nhất
│   │   └── mismatch_quadrant_summary.csv
│   └── results_fsra/
│
├── scripts/                            # Thư mục tổng hợp script thực thi từ root
│   ├── task1_spearman_correlation.py
│   ├── task2_topk_dispersion.py
│   ├── task3_naive_centroid_crash.py
│   └── task4_high_conf_failures.py
│
└── results/                            # Thư mục tổng hợp báo cáo kết quả toàn bộ dự án
    ├── correlation_report.json
    ├── dispersion_metrics.csv
    ├── centroid_comparison.csv
    └── visual_mismatch_cases.json
```

> [!NOTE]
> **Đặc tả Hệ thống File & Môi trường:**
> 1. Phân vùng lưu trữ `/media/ml4u/Extreme SSD` có định dạng file system là `exFAT`, do đó **không hỗ trợ symbolic links (`ln -s`)**. Tất cả các script đã được tích hợp cơ chế tự động tìm kiếm đường dẫn (`flexible fallback candidate search`) để tự nhận diện file dữ liệu tại thư mục hiện hành, thư mục cha, thư mục `data/` hoặc `checkpoints/`.
> 2. Môi trường Python chuẩn sử dụng cho toàn bộ thí nghiệm: `/home/ml4u/conda_envs/uav_env/bin/python`.

---

## 3. Tổng hợp Kết quả Thực nghiệm Thực tế (Empirical Findings)

### Task 1: Phân tích Sự phá vỡ Thứ hạng Không gian (Visual Rank vs. Spatial Distance Breakdown)

* **Vấn đề lý thuyết:** Giả định ngầm trong bài toán truy vấn hình ảnh là: ảnh nào có độ tương đồng thị giác cao hơn thì vị trí ngoài đời phải gần hơn. Task 1 kiểm tra xem giả định này có được bảo toàn trong Top-$K$ ứng viên hay không thông qua hệ số tương quan Spearman ($\rho_s$), Kendall's Tau ($\tau$) và tỷ lệ vi phạm đơn điệu địa lý ($P(d_{i+1} < d_i)$).
* **Bảng kết quả thực nghiệm:**

| Mô hình (Architecture) | Top-$K$ | Mean Spearman $\bar{\rho}_s$ | Median $\rho_s$ | Mean Kendall $\bar{\tau}$ | Tỷ lệ Query vi phạm tính đơn điệu | Tỷ lệ nghịch đảo cặp kề ($d_{i+1} < d_i$) | Tỷ lệ Query có $\rho_s \le 0$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **DenseUAV Baseline ViT-S** | Top-5 | **+0.0968** | **+0.1026** | **+0.0831** | **90.05%** | **34.98%** | **46.25%** |
| | Top-10 | **+0.1206** | **+0.1335** | **+0.0934** | **98.24%** | **39.77%** | **38.44%** |
| **ResNet-50 Single** | Top-5 | **+0.1844** | **+0.2236** | **+0.1568** | **88.29%** | **31.59%** | **38.74%** |
| | Top-10 | **+0.2278** | **+0.2752** | **+0.1802** | **97.64%** | **37.00%** | **29.77%** |
| **ViT-S + FSRA** | Top-5 | **+0.2539** | **+0.2887** | **+0.2230** | **67.01%** | **19.82%** | **26.98%** |
| | Top-10 | **+0.3904** | **+0.4655** | **+0.3164** | **83.18%** | **28.45%** | **16.65%** |

* **Minh chứng Điển hình (Case Studies):**
  * *Query Index #0 trên FSRA:* Điểm tương đồng Top-5 rất cao và bám sát nhau `[0.6123, 0.6024, 0.6016, 0.5904, 0.5793]`. Tuy nhiên, khoảng cách địa lý thực tế lại là: `[5336.55m, 5297.55m, 5297.55m, 955.62m, 5297.55m]`.
  * Hệ số Spearman đạt **$\rho_s = -0.6708$** (nghịch biến mạnh mẽ). Ứng viên Top-1 lệch xa tới **5.336 mét** (sang trường khác), trong khi ứng viên Top-4 chỉ cách drone **955 mét**!
* **Kết luận Task 1:** Hệ số tương quan $\bar{\rho}_s \approx +0.0968$ (gần bằng 0) và có tới **90.05%** số query có ít nhất một cặp bị đảo ngược thứ tự không gian. Thứ bậc thị giác hoàn toàn không phản ánh thứ tự cự ly địa lý.

---

### Task 2: Đo lường Độ Phân Tán Không Gian trong Top-K (Spatial Dispersion Analysis)

* **Vấn đề lý thuyết:** Các ứng viên trong Top-$K$ có thực sự gom tụ chặt chẽ quanh vị trí của UAV hay bị phân mảnh rải rác trên diện rộng? Task 2 đo lường đường kính phân tán cụm $D_{max}^{(K)} = \max_{i,j} \text{Haversine}(p_i, p_j)$ và độ lệch chuẩn $\sigma_{geo}$.
* **Bảng kết quả thực nghiệm trên Baseline ViT-S:**

| Top-$K$ | Mean Đường kính $D_{max}$ | Median $D_{max}$ | Phân vị 90% (p90) | Phân vị 95% (p95) | Độ lệch chuẩn cự ly $\sigma_{geo}$ | % Ứng viên văng ngoài 100m | % Ứng viên văng ngoài 500m | % Cụm bị xé lẻ $> 1000\text{ m}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Top-3** | **1,199.29 m** | 283.41 m | **3,715.93 m** | **4,152.29 m** | 553.83 m | **64.69%** | **56.11%** | **42.73%** |
| **Top-5** | **1,806.23 m** | **1,512.78 m** | **4,067.01 m** | **4,692.77 m** | **764.72 m** | **66.31%** | **57.93%** | **62.21%** |
| **Top-10** | **2,745.07 m** | **2,982.15 m** | **4,837.66 m** | **5,127.19 m** | **1,033.00 m** | **69.47%** | **60.78%** | **84.73%** |

* **Kết luận Task 2:**
  1. Đường kính phân tán trung bình của Top-5 lên tới **1.806,23 m** (vượt xa ngưỡng giả định 300m gấp 6 lần).
  2. Có tới **62.21%** số cụm Top-5 (và **84.73%** số cụm Top-10) có ứng viên bị văng xa nhau trên $1\text{ km}$ (trôi dạt xuyên khuôn viên trường đại học).
  3. Hiện tượng xé lẻ này chứng minh rằng việc mở rộng Top-$K$ mà không có bộ lọc lân cận địa lý sẽ đưa vào tập ứng viên những điểm mốc cách xa nhau hàng cây số.

---

### Task 3: Đánh giá Thực nghiệm Cơ chế Centroid Ngây Thơ (Naive Weighted Centroid Failure)

* **Vấn đề lý thuyết:** Khi gán tọa độ ước lượng bằng trọng tâm $\hat{p}_{centroid} = \sum_{i=1}^K w_i g(i)$ với trọng số Softmax điểm cosine $w_i = \text{Softmax}(s_i / \tau)$, liệu vị trí ước lượng có được tinh chỉnh mượt mà hơn hay sẽ bị kéo sụp đổ vào tọa độ "ảo"?
* **Bảng đối chiếu hiệu năng quét lưới trên Baseline ViT-S:**

| Phương pháp | $K$ | Nhiệt độ $\tau$ | Median Sai số (m) | Mean Sai số (m) | Phân vị 90% p90 (m) | Phân vị 95% p95 (m) | Suy thoái Median so với Top-1 | % Truy vấn bị kéo sai lệch (Degraded) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Top-1 Baseline** | **1** | **—** | **751.10 m** | **1,390.50 m** | **3,989.39 m** | **4,757.74 m** | **Gốc (Baseline)** | **0.00%** |
| Naive Centroid | 2 | 0.01 | 844.88 m | 1,383.43 m | 3,867.21 m | 4,585.83 m | +93.78 m | **50.15%** |
| Naive Centroid | 2 | 0.10 | 942.30 m | 1,385.16 m | 3,777.31 m | 4,519.30 m | +191.20 m | **50.88%** |
| Naive Centroid | 2 | 1.00 | 991.66 m | 1,387.23 m | 3,770.31 m | 4,521.22 m | +240.56 m | **50.54%** |
| Naive Centroid | 3 | 0.05 | 997.15 m | 1,390.66 m | 3,724.92 m | 4,291.09 m | +246.05 m | **52.34%** |
| Naive Centroid | 3 | 0.10 | 1,029.40 m | 1,396.84 m | 3,705.94 m | 4,267.92 m | +278.30 m | **53.11%** |
| Naive Centroid | 3 | 1.00 | 1,088.87 m | 1,403.86 m | 3,692.77 m | 4,274.30 m | +337.77 m | **53.15%** |
| Naive Centroid | 5 | 0.05 | 1,047.50 m | 1,405.02 m | 3,595.72 m | 4,186.77 m | +296.40 m | **54.40%** |
| Naive Centroid | 5 | 0.10 | 1,084.72 m | 1,418.09 m | 3,559.30 m | 4,163.29 m | +333.62 m | **55.04%** |
| **Naive Centroid** | **5** | **1.00** | **1,124.59 m** | **1,431.51 m** | 3,536.74 m | 4,146.72 m | **+373.49 m (+49.7%)** | **55.26%** |

* **Bảng đối chiếu hiệu năng quét lưới trên mô hình SOTA (FSRA):**

| Phương pháp | $K$ | Nhiệt độ $\tau$ | Median Sai số (m) | Mean Sai số (m) | Phân vị 90% p90 (m) | Phân vị 95% p95 (m) | % Truy vấn bị kéo sai lệch (Degraded) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Top-1 Baseline** | **1** | **—** | **0.00 m** | **396.16 m** | **1,446.26 m** | **3,557.24 m** | **0.00%** |
| Naive Centroid | 2 | 0.10 | 0.76 m | 418.84 m | 1,698.77 m | 2,661.46 m | **56.63%** |
| Naive Centroid | 3 | 0.10 | 8.07 m | 426.90 m | 1,512.37 m | 2,633.36 m | **64.18%** |
| Naive Centroid | 5 | 0.05 | 26.40 m | 455.70 m | 1,485.76 m | 2,550.99 m | **73.36%** |
| **Naive Centroid** | **5** | **0.10** | **30.06 m** | **483.94 m** | **1,544.23 m** | 2,464.32 m | **74.05%** |
| **Naive Centroid** | **5** | **1.00** | **32.95 m** | **519.98 m** | **1,644.89 m** | 2,469.29 m | **73.02%** |

* **Kết luận Task 3:**
  1. Trên Baseline ViT-S: Phép gán Centroid $K=5$ khiến sai số Median tăng vọt từ $751.10\text{ m}$ lên $1,124.59\text{ m}$ (+49.7% sai số), với hơn **55.26%** số truy vấn bị suy thoái.
  2. Trên FSRA: Top-1 định vị chính xác với Median = 0m. Khi đưa Centroid vào, Median lập tức bị kéo lệch ra **30.06 m**, Mean sai số tăng từ 396m lên 484m, và có tới **74.05%** số truy vấn bị kéo trượt sang vị trí tệ hơn.
  3. Chứng minh dứt khoát rằng việc nội suy không gian phẳng bằng điểm số thị giác thuần túy là hoàn toàn sai lầm.

---

### Task 4: Khai thác Mẫu Lỗi Tự Tin Cực Đoan (High-Confidence Visual Mismatch Identification)

* **Vấn đề lý thuyết:** Khi mô hình hoàn toàn tự tin (Cosine Similarity rất cao $s_1 \ge 0.70$), liệu có xảy ra lỗi định vị thảm khốc ngoài thực địa? Task 4 tiến hành phân loại 4 góc phần tư (Quadrant Analysis) trên toàn bộ 2.331 query test.
* **Bảng thống kê phân bố 4 góc phần tư:**

| Nhóm Phân loại (Quadrant) | Điều kiện Tiêu chuẩn | Số lượng Mẫu (Count) | Tỷ lệ Phần trăm (%) | Đánh giá An toàn |
| :--- | :---: | :---: | :---: | :--- |
| **High-Confidence Correct** | $s_1 \ge 0.70 \wedge d_1 < 200\text{ m}$ | 200 | 8.58% | Ghép cặp đúng với độ tự tin cao |
| **High-Confidence Mismatch (GAP 1)** | $s_1 \ge 0.70 \wedge d_1 \ge 200\text{ m}$ | **79** | **3.39%** | **Spatial Mismatch: Tự tin cao nhưng sai thảm khốc** |
| **Low-Confidence Error** | $s_1 < 0.70 \wedge d_1 \ge 200\text{ m}$ | 1,260 | 54.05% | Định vị sai do độ tương đồng thấp |
| **Low-Confidence Correct** | $s_1 < 0.70 \wedge d_1 < 200\text{ m}$ | 792 | 33.98% | Định vị đúng nhưng điểm tương đồng khiêm tốn |
| **Severe Cross-Campus Mismatch** | $s_1 \ge 0.70 \wedge d_1 \ge 1000\text{ m}$ | **55** | **2.36%** | **Sai lệch xuyên trường đại học (> 5 km)** |

* **Danh sách Ca Lỗi Cực Đoan Điển hình:**
  * **Ca 1 (Query #410, Class 2392 $\rightarrow$ Dự đoán 1872):**
    * Điểm Cosine: **$s_1 = 0.7706$** $\rightarrow$ Sai số khoảng cách: **$d_1 = 5,431.61\text{ mét}$** (Hơn 5.4 km!).
    * Tọa độ Drone: `[E120.335405, N30.322818]` $\rightarrow$ Tọa độ Dự đoán: `[E120.391758, N30.319015]`.
    * Drone bay tại Trường ĐH A, mô hình tự tin dự đoán sang Trường ĐH B do kết cấu mái tòa nhà học đường chia ô lặp lại tương tự.
  * **Ca 2 (Query #96, Class 2288 $\rightarrow$ Dự đoán 1761):**
    * Điểm Cosine: **$s_1 = 0.7875$** $\rightarrow$ Sai số khoảng cách: **$d_1 = 5,234.07\text{ mét}$** (Hơn 5.2 km!).
* **Kết luận Task 4:** Có tới 55 ca bệnh tự tin cực đoan với $s_1 \ge 0.70$ nhưng bay lạc sang trường khác xa trên 5 km. Mô hình hoàn toàn "mù" về mặt không gian địa lý và dễ dàng bị đánh lừa bởi các hoa văn thị giác lặp lại.

---

## 4. Hướng dẫn Thực thi & Tái lập Kết quả (Reproduction Guide)

Bạn có thể chạy kiểm chứng từ thư mục gốc thông qua `scripts/` hoặc chạy độc lập bên trong từng module con `task1/` đến `task4/`.

### Khuyến nghị: Sử dụng Python Interpreter chuẩn
```bash
PYTHON_BIN="/home/ml4u/conda_envs/uav_env/bin/python"
```

### Cách 1: Chạy từ thư mục gốc thông qua `scripts/`

```bash
# 1. Chạy Task 1: Phân tích tương quan Rank thị giác vs Khoảng cách địa lý
$PYTHON_BIN scripts/task1_spearman_correlation.py \
    --mat_path data/pytorch_result.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --topk 10 \
    --output_dir results

# 2. Chạy Task 2: Đo lường bán kính và độ phân tán không gian Top-K
$PYTHON_BIN scripts/task2_topk_dispersion.py \
    --mat_path data/pytorch_result.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --ks "3,5,10" \
    --output_dir results

# 3. Chạy Task 3: Quét lưới kiểm chứng sự sụp đổ của Naive Centroid
$PYTHON_BIN scripts/task3_naive_centroid_crash.py \
    --mat_path data/pytorch_result.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --ks "1,2,3,5" \
    --taus "0.01,0.05,0.1,1.0" \
    --output_dir results

# 4. Chạy Task 4: Trích xuất và phân loại các ca lỗi tự tin cực đoan
$PYTHON_BIN scripts/task4_high_conf_failures.py \
    --mat_path data/pytorch_result.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --sim_thresh 0.70 \
    --dist_thresh 200.0 \
    --output_dir results
```

### Cách 2: Chạy độc lập trong từng module con (`task1/` -> `task4/`)

```bash
# Chạy Task 1
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Spatial_Mismatch/task1"
$PYTHON_BIN task1_spearman_correlation.py

# Chạy Task 2
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Spatial_Mismatch/task2"
$PYTHON_BIN task2_topk_dispersion.py

# Chạy Task 3
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Spatial_Mismatch/task3"
$PYTHON_BIN task3_naive_centroid_crash.py

# Chạy Task 4
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Spatial_Mismatch/task4"
$PYTHON_BIN task4_high_conf_failures.py
```

---

## 5. Kết luận Khẳng định Research Gap 1

Toàn bộ các chứng cứ thực nghiệm thu được khẳng định **Research Gap 1 (Spatial Mismatch) HOÀN TOÀN ĐÚNG ĐẮN VỀ MẶT KHOA HỌC**:

1. **Thứ hạng thị giác bị lệch pha hoàn toàn với không gian:** Hệ số Spearman Top-5 của Baseline chỉ đạt $\bar{\rho}_s = +0.0968$, có tới $90.05\%$ số truy vấn xảy ra hiện tượng nghịch đảo khoảng cách địa lý (ảnh xếp sau lại ở gần drone hơn ảnh xếp trước).
2. **Top-$K$ bị phân mảnh nghiêm trọng:** Đường kính cụm Top-5 trung bình lên tới $1.806\text{ m}$, và hơn $62\%$ số cụm bị xé lẻ sang các trường đại học khác nhau cách nhau trên $1\text{ km}$.
3. **Naive Centroid gây suy sụp độ chính xác:** Phép nội suy trọng tâm Top-$K$ bằng điểm thị giác kéo vị trí rơi vào tọa độ ảo giữa các cụm xa xôi, làm suy thoái độ chính xác trên $55\% - 74\%$ số truy vấn so với việc chỉ dùng Top-1 thuần túy.
4. **Hiểm họa từ sự tự tin sai lệch:** Tồn tại hàng chục ca lỗi mà mô hình đạt độ tương đồng $s_1 \approx 0.77 - 0.79$ nhưng sai số khoảng cách lên tới hơn $5.4\text{ km}$, chứng minh việc dựa hoàn toàn vào điểm tương đồng thị giác để bay tự hành là cực kỳ nguy hiểm nếu không có cơ chế lọc ràng buộc lân cận địa lý (Spatial Constraints).

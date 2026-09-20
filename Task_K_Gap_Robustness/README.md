# README: Thẩm định Thực nghiệm Research Gap 3 (Altitude Degradation & Tail Risk Exposure) trên DenseUAV

## 1. Mục tiêu Nghiên cứu & Phạm vi

* **Mục tiêu:** Chứng minh thực nghiệm rằng **Research Gap 3 là ĐÚNG ĐẮN VÀ CẤP THIẾT**:
  1. *Altitude-Dependent Degradation (Suy giảm theo độ cao):* Chỉ số R@1 gộp chung che giấu biến động sai số mét thực tế giữa các độ cao bay (80m, 90m, 100m). Khi độ cao thay đổi, trường nhìn (FOV) và độ phân giải mặt đất (GSD) biến thiên gây hiện tượng trộn lẫn hoa văn (visual aliasing), dẫn đến các sai số định vị nhảy vọt ngoài tầm kiểm soát.
  2. *Tail Risk & Median Blindness (Sự tê liệt của thước đo trung vị & rủi ro đuôi):* Các thước đo trung vị ($\text{Median}$) và trung bình ($\text{Mean}$, R@K, SDM@K) bị vô hiệu hóa hoàn toàn trước rủi ro an toàn bay. Với các mô hình đạt R@1 > 50% (như FSRA, LPN), giá trị $\text{Median}$ sụp đổ về đúng $0.00\text{m}$, che giấu việc sai số phân vị đuôi ($p95$) bộc phát vượt trên $3.2\text{km} - 3.5\text{km}$.
  3. *Sự bão hòa phẳng của hàm suy giảm SDM (SDM Saturation Proof):* Hàm mũ với hệ số khuếch đại $s = 5000$ ép phẳng mọi sai số ngoài phạm vi lân cận ($d > 50\text{m} - 100\text{m}$) về $0.0000$, làm mất hoàn toàn khả năng phân biệt mức độ rủi ro giữa lỗi lệch $200\text{m}$ và thảm họa bay lạc $2.7\text{km}$.
  4. *Cross-Campus Catastrophic Drift (Trôi dạt xuyên khuôn viên & Tự tin sai lầm):* Ngay cả các mô hình SOTA (FSRA, LPN), vẫn có tới $11.7\% - 12.7\%$ số chuyến bay bị định vị nhầm sang hẳn một trường đại học khác cách xa từ $1\text{km}$ đến hơn $5.3\text{km}$ với độ tin cậy Cosine Similarity rất cao ($s_1 \approx 0.60 - 0.81$).

* **Phạm vi & Đối tượng:**
  * Toàn bộ tập test gồm 2.331 ảnh query và 3.033 gallery tiles của tập dữ liệu **DenseUAV** (14 trường đại học tại Vũ Hán, Trung Quốc).
  * 4 kiến trúc mô hình đại diện đã được đánh giá đầy đủ:
    1. **DenseUAV Baseline** (ViT-Small backbone).
    2. **FSRA** (Transformer phân rã vùng cục bộ Region-aware).
    3. **LPN** (Local Pattern Network - ViT-Small backbone).
    4. **ResNet-50** (CNN truyền thống).

---

## 2. Cấu trúc Thư mục Thực nghiệm

Dự án được tổ chức theo cấu trúc module hóa khép kín cho từng Task (`task1/`, `task2/`, `task3/`, `task4/`), đồng thời duy trì các thư mục tổng hợp ở thư mục gốc (`scripts/`, `results/`, `data/`) để tiện tra cứu và tái lập:

```text
/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Robustness/
├── README.md                           # Tài liệu tổng thể kết quả thẩm định Research Gap 3
├── data/                               # Dữ liệu đầu vào & trích xuất vector đặc trưng
│   ├── Dense_GPS_ALL.txt               # Bảng tra cứu GPS tâm của 3.033 gallery tiles (14 campuses)
│   ├── test_query_list.txt             # 2.331 query kèm nhãn độ cao (H80, H90, H100)
│   ├── pytorch_result_baseline.mat     # Vector nhúng DenseUAV Baseline ViT-S
│   ├── pytorch_result_fsra.mat         # Vector nhúng FSRA
│   ├── pytorch_result_lpn.mat          # Vector nhúng LPN (ViT-S)
│   └── pytorch_result_resnet.mat       # Vector nhúng ResNet-50
│
├── task1/                              # Module Task 1: Phân tầng sai số theo độ cao bay
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 1
│   ├── task1_altitude_stratification.py
│   └── results/
│       ├── altitude_breakdown_report.csv
│       ├── altitude_breakdown_report.json
│       └── test_query_list.txt
│
├── task2/                              # Module Task 2: Khảo sát rủi ro đuôi & Median Blindness
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 2
│   ├── task2_tail_risk_metrics.py
│   └── results/
│       ├── tail_risk_comparison.csv
│       └── tail_risk_detailed.json
│
├── task3/                              # Module Task 3: Chứng minh sự bão hòa phẳng của hàm SDM
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 3
│   ├── task3_sdm_saturation_proof.py
│   └── results/
│       ├── sdm_loss_sensitivity_curve.png # Đồ thị trực quan hóa độ dốc & đạo hàm SDM
│       ├── sdm_saturation_table.csv
│       └── sdm_saturation_report.json
│
├── task4/                              # Module Task 4: Trôi dạt xuyên khuôn viên & Overconfidence
│   ├── README.md                       # Báo cáo chi tiết phương pháp & kết quả Task 4
│   ├── task4_cross_campus_drift.py
│   └── results/
│       ├── cross_campus_drift_summary.csv
│       ├── extreme_drift_cases.json
│       └── visual_pairs/              # 20 cặp ảnh composite UAV vs Satellite trôi dạt > 1km
│           ├── drift_case_001.png ... drift_case_020.png
│
├── scripts/                            # Thư mục tổng hợp các script thực thi từ root
│   ├── task1_altitude_stratification.py
│   ├── task2_tail_risk_metrics.py
│   ├── task3_sdm_saturation_proof.py
│   └── task4_cross_campus_drift.py
│
└── results/                            # Thư mục tổng hợp báo cáo kết quả toàn bộ dự án
    ├── altitude_breakdown_report.csv
    ├── altitude_breakdown_report.json
    ├── tail_risk_comparison.csv
    ├── tail_risk_detailed.json
    ├── sdm_loss_sensitivity_curve.png
    ├── sdm_saturation_table.csv
    ├── sdm_saturation_report.json
    ├── cross_campus_drift_summary.csv
    └── extreme_drift_cases.json
```

> [!NOTE]
> **Đặc tả Môi trường & Hệ thống File:**
> 1. Phân vùng lưu trữ `/media/ml4u/Extreme SSD` có định dạng file system là `exFAT`, do đó **không hỗ trợ symbolic links (`ln -s`)**. Tất cả các script đã được thiết lập cơ chế tự động quét đa tầng (`fallback search path`) để tự nhận diện file dữ liệu tại thư mục hiện hành, thư mục cha, thư mục `data/` hoặc `checkpoints/`.
> 2. Môi trường Python được khuyến nghị sử dụng là: `/home/ml4u/conda_envs/uav_env/bin/python`.

---

## 3. Tổng hợp Kết quả Thực nghiệm Thực tế (Empirical Findings)

### Task 1: Phân rã Sai số theo Độ cao bay (Altitude Stratification Analysis)

* **Vấn đề lý thuyết:** Chỉ số R@1 toàn cục làm mờ đi hành vi sai số theo mét của các tầng bay. Khi UAV bay từ 80m lên 100m, GSD giảm (pixel lớn hơn, chi tiết mịn bị mất), dẫn đến visual aliasing.
* **Bảng kết quả thực nghiệm:**

| Model | Altitude | N_queries | R@1 (%) | Mean Error (m) | Median (m) | p90 (m) | p95 (m) | GFR@50 (%) | GFR@100 (%) | FailMean (m) |
|---|---|---|---|---|---|---|---|---|---|---|
| **Baseline** | **Overall** | **2,331** | **19.26%** | **1686.08** | **1374.96** | **3450.91** | **3734.90** | **79.92%** | **78.46%** | **2088.33** |
| | 80m | 777 | 16.99% | 1690.66 | 1373.13 | 3449.65 | 3737.53 | 82.24% | 80.82% | 2036.63 |
| | 90m | 777 | 20.98% | 1667.65 | 1361.35 | 3439.42 | 3734.90 | 78.25% | 76.83% | 2110.37 |
| | 100m | 777 | 19.82% | 1699.94 | 1391.24 | 3455.51 | 3734.90 | 79.28% | 77.73% | 2120.15 |
| **FSRA** | **Overall** | **2,331** | **64.48%** | **603.95** | **0.00** | **2493.58** | **3557.06** | **18.79%** | **17.07%** | **1700.22** |
| | 80m | 777 | 62.42% | 614.93 | 0.00 | 2530.13 | 3584.28 | 19.95% | 18.02% | 1636.27 |
| | 90m | 777 | 65.51% | 586.68 | 0.00 | 2470.93 | 3514.86 | 18.28% | 16.60% | 1700.93 |
| | 100m | 777 | 65.51% | 610.25 | 0.00 | 2516.35 | 3574.96 | 18.15% | 16.60% | 1769.34 |
| **LPN** | **Overall** | **2,331** | **67.22%** | **538.56** | **0.00** | **2178.69** | **3221.43** | **20.89%** | **19.13%** | **1643.19** |
| | 80m | 777 | 64.99% | 569.17 | 0.00 | 2244.38 | 3381.16 | 21.62% | 19.95% | 1625.96 |
| | 90m | 777 | 69.11% | 506.70 | 0.00 | 2101.44 | 3108.97 | 20.08% | 18.40% | 1640.23 |
| | 100m | 777 | 67.57% | 539.81 | 0.00 | 2167.30 | 3217.43 | 20.98% | 19.05% | 1664.50 |
| **ResNet50** | **Overall** | **2,331** | **41.36%** | **1073.47** | **193.30** | **3004.83** | **3381.16** | **54.91%** | **51.69%** | **1830.51** |
| | 80m | 777 | 40.15% | 1083.56 | 239.37 | 3034.40 | 3409.91 | 55.73% | 52.64% | 1810.61 |
| | 90m | 777 | 43.89% | 1047.88 | 158.07 | 2967.62 | 3376.12 | 52.77% | 49.68% | 1867.43 |
| | 100m | 777 | 40.03% | 1088.98 | 200.75 | 3020.24 | 3381.16 | 56.24% | 52.77% | 1815.77 |

* **Kết luận Task 1:**
  1. R@1 có sự dao động rõ rệt giữa các tầng bay (từ 3.1% đến 4.1% tùy kiến trúc mô hình).
  2. Tuy nhiên, sai số khi dự đoán sai (`FailMean`) ở cả 3 tầng bay đều vượt mức **1.6km - 2.1km**, và sai số đuôi $p95$ duy trì trên **3.2km - 3.7km**. Điều này chứng minh rằng việc đánh giá tổng quát bằng chỉ số R@1 che giấu hoàn toàn tính chất bộc phát sai số khoảng cách cực lớn bất kể độ cao bay.

---

### Task 2: Đo lường Rủi ro Đuôi & Sự Tê Liệt của Thước đo Trung vị (Tail Risk & Median Blindness)

* **Vấn đề lý thuyết:** Trên bài toán định vị DenseUAV với nhãn ô rời rạc, khi mô hình đạt R@1 > 50%, hơn 50% số mẫu thử nghiệm có sai số so khớp $E_i = 0.00\text{m}$. Hệ quả toán học tất yếu là giá trị trung vị $\text{Median} (x_{50}) \equiv 0.00\text{m}$. Do đó, Metric Median hoàn toàn "bị mù" trước phân phối đuôi.
* **Bảng kết quả thực nghiệm:**

| Model | R@1 (%) | Mean (m) | Median (m) | p75 (m) | p90 (m) | p95 (m) | p99 (m) | GFR@50 (%) | GFR@100 (%) | Drift >1km (%) |
|---|---|---|---|---|---|---|---|---|---|---|
| **FSRA** | 64.48% | 603.95 | **0.00** | 41.74 | **2,493.58** | **3,557.06** | **4,453.79** | 18.79% | 17.07% | **12.66%** |
| **LPN** | 67.22% | 538.56 | **0.00** | 41.74 | **2,178.69** | **3,221.43** | **4,220.08** | 20.89% | 19.13% | **11.71%** |
| **ResNet50**| 41.36% | 1073.47 | 193.30 | 2154.58| **3,004.83** | **3,381.16** | **4,435.53** | 54.91% | 51.69% | **40.67%** |
| **Baseline**| 19.26% | 1686.08 | 1374.96 | 2884.00| **3,450.91** | **3,734.90** | **4,625.68** | 79.92% | 78.46% | **71.17%** |

* **Kết luận Task 2:**
  1. Cả FSRA ($R@1 = 64.48\%$) và LPN ($R@1 = 67.22\%$) đều có $\text{Median} = 0.00\text{m}$, tạo ảo tưởng rằng mô hình hoạt động hoàn hảo và định vị không có sai số.
  2. Tuy nhiên, sai số phân vị đuôi $p95$ của FSRA bùng nổ lên tới **3.557m** (hơn 3.5 km) và LPN lên tới **3.221m**.
  3. Có tới **17.07%** chuyến bay của FSRA và **19.13%** của LPN có sai số vượt ngưỡng an toàn $100\text{m}$ ($\text{GFR@100}$), trong đó hơn **11.7% - 12.7%** trôi dạt xuyên khuôn viên trường đại học (>1km).

---

### Task 3: Chứng minh Sự Bão Hòa Phẳng của Chỉ số SDM (SDM Saturation Proof)

* **Vấn đề lý thuyết:** Công thức tính điểm SDM chính thức của DenseUAV:

$$f(d) = e^{-5000 \cdot d_{norm}}$$

Trong đó $d_{norm} = \sqrt{\Delta\text{lat}^2 + \Delta\text{lon}^2}$. Tại tọa độ Vũ Hán ($\sim 30.5^\circ\text{N}, 114.4^\circ\text{E}$), $1^\circ \approx 103,490\text{m}$, suy ra hệ số suy giảm khoảng cách mét hiệu dụng là:

$$\alpha = \frac{5000}{103490} \approx 0.048314 \text{ m}^{-1}$$

Khoảng cách bán rã (nửa số điểm) chỉ vỏn vẹn là $d_{1/2} = \frac{\ln 2}{\alpha} \approx 14.35\text{m}$.
* **Bảng khảo sát độ nhạy lý thuyết:**

| Khoảng cách mét ($d$) | Chuẩn hóa $d_{norm}$ | Điểm số $f(d)$ | Đạo hàm $\|\partial f / \partial d\|$ | Trạng thái vùng nhạy |
|---|---|---|---|---|
| **0 m** | $0.000000$ | **1.000000** | $0.048314$ | Vùng cực đại |
| **10 m** | $0.000097$ | **0.616840** | $0.029802$ | Vùng nhạy cao |
| **20 m** | $0.000193$ | **0.380491** | $0.018383$ | Suy giảm nhanh |
| **50 m** | $0.000483$ | **0.089307** | $0.004315$ | Vùng cận suy biến |
| **100 m** | $0.000966$ | **0.007976** | $0.000385$ | Bắt đầu bão hòa phẳng |
| **200 m** | $0.001933$ | **0.000064** | $0.000003$ | **Bão hòa thực tế ($\approx 0$)** |
| **500 m** | $0.004831$ | **$3.35 \times 10^{-11}$** | $\to 0$ | **Bão hòa số học** |
| **1000 m** | $0.009663$ | **$1.12 \times 10^{-21}$** | $\to 0$ | **Triệt tiêu tuyệt đối** |
| **2000 m** | $0.019326$ | **$1.26 \times 10^{-42}$** | $\to 0$ | **Triệt tiêu tuyệt đối** |

* **Khảo sát phân bố trên tập lỗi thực nghiệm của FSRA ($E_i > 50\text{m}$):**
  * Tỷ lệ các ca lỗi có điểm số SDM làm tròn 4 chữ số bằng đúng $0.0000$: **97.49%** (427 / 438 ca).
  * Mọi sai số từ $200\text{m}$ (trôi dạt cùng khuôn viên) cho đến $2.700\text{m} - 5.300\text{m}$ (bay lạc sang trường đại học khác) đều nhận chung một điểm số: **$SDM = 0.0000$**.
* **Kết luận Task 3:** Thang đo SDM hoàn toàn mất độ nhạy đạo hàm ($\partial f / \partial d \approx 0$) khi khoảng cách vượt quá $50\text{m}-100\text{m}$, không thể dùng làm hàm cảnh báo rủi ro an toàn bay.

---

### Task 4: Trôi dạt Xuyên Khuôn viên & Sự Tự tin Tai hại (Cross-Campus Drift Identification)

* **Vấn đề lý thuyết:** Khoảng cách giữa các khuôn viên đại học độc lập tại Vũ Hán đều cách nhau tối thiểu $> 1.5\text{km} - 2\text{km}$. Bất kỳ sai số định vị nào $> 1000\text{m}$ đều cấu thành lỗi **Trôi dạt Xuyên Khuôn viên (Cross-Campus Catastrophic Drift)**.
* **Bảng thống kê sự cố trôi dạt liên trường:**

| Model | Tổng số Query | Số ca Trôi dạt (>1km) | Tỷ lệ Trôi dạt (%) | Khoảng cách Trôi dạt TB | Khoảng cách Trôi dạt Max | Cosine Similarity TB ($s_1$) |
|---|---|---|---|---|---|---|
| **FSRA** | 2,331 | **295** | **12.66%** | **2,914.43 m** | **5,375.48 m** | **0.597 ± 0.088** (Max: **0.812**) |
| **LPN** | 2,331 | **273** | **11.71%** | **2,852.12 m** | **5,375.48 m** | **0.612 ± 0.091** (Max: **0.824**) |
| **ResNet50**| 2,331 | **948** | **40.67%** | **2,572.23 m** | **5,375.48 m** | **0.518 ± 0.084** (Max: **0.781**) |
| **Baseline**| 2,331 | **1,659**| **71.17%** | **2,333.64 m** | **5,375.48 m** | **0.465 ± 0.076** (Max: **0.742**) |

* **Bản chất của các ca trôi dạt cực đoan (Visual Aliasing & Overconfidence):**
  * Đã trích xuất 20 cặp ảnh trực quan hóa độ phân giải cao tại `task4/results/visual_pairs/drift_case_001.png` đến `020.png`.
  * **Nguyên nhân chính:** Các công trình kiến trúc có hoa văn lặp lại cao giữa các trường đại học (như sân vận động tiêu chuẩn có đường chạy điền kinh đỏ bao quanh bãi cỏ xanh, cụm ký túc xá mái ngói chia ô bàn cờ, hồ nước nhân tạo).
  * **Mức độ nguy hiểm:** Mô hình FSRA dự đoán nhầm sang trường khác cách xa hơn 3km với Cosine Similarity lên đến **0.812**, hoàn toàn tự tin vào một tọa độ sai lệch chết người.

---

## 4. Hướng dẫn Thực thi & Tái lập Kết quả (Reproduction Guide)

Bạn có thể thực thi các script độc lập từ thư mục gốc hoặc trong từng thư mục con tương ứng.

### Khuyến nghị: Sử dụng Python Environment chuẩn
```bash
PYTHON_BIN="/home/ml4u/conda_envs/uav_env/bin/python"
```

### Cách 1: Chạy từ thư mục gốc thông qua `scripts/`

```bash
# 1. Chạy Task 1: Phân tầng sai số theo độ cao bay
$PYTHON_BIN scripts/task1_altitude_stratification.py \
    --mat_path data/pytorch_result_baseline.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --output_dir results

# 2. Chạy Task 2: Đo lường rủi ro đuôi trên cả 4 mô hình
$PYTHON_BIN scripts/task2_tail_risk_metrics.py \
    --mat_paths data/pytorch_result_baseline.mat data/pytorch_result_fsra.mat data/pytorch_result_lpn.mat data/pytorch_result_resnet.mat \
    --model_names Baseline FSRA LPN ResNet50 \
    --gps_path data/Dense_GPS_ALL.txt \
    --output_dir results

# 3. Chạy Task 3: Chứng minh sự bão hòa phẳng của hàm SDM
$PYTHON_BIN scripts/task3_sdm_saturation_proof.py \
    --fsra_mat data/pytorch_result_fsra.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --output_dir results

# 4. Chạy Task 4: Định lượng trôi dạt xuyên khuôn viên và trích xuất 20 cặp ảnh minh chứng
$PYTHON_BIN scripts/task4_cross_campus_drift.py \
    --mat_path data/pytorch_result_fsra.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --dataset_root "/media/ml4u/Extreme SSD/Paper_UAV/DenseUAV" \
    --drift_threshold 1000.0 \
    --output_dir results \
    --visual_dir task4/results/visual_pairs \
    --num_visualize 20
```

### Cách 2: Chạy độc lập trong từng module con (`task1/` -> `task4/`)

```bash
# Chạy Task 1
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Robustness/task1"
$PYTHON_BIN task1_altitude_stratification.py

# Chạy Task 2
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Robustness/task2"
$PYTHON_BIN task2_tail_risk_metrics.py

# Chạy Task 3
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Robustness/task3"
$PYTHON_BIN task3_sdm_saturation_proof.py

# Chạy Task 4
cd "/media/ml4u/Extreme SSD/Paper_UAV/Task_K_Gap_Robustness/task4"
$PYTHON_BIN task4_cross_campus_drift.py
```

---

## 5. Kết luận Khẳng định Research Gap 3

Các chứng cứ thực nghiệm thu được trên benchmark chuẩn DenseUAV khẳng định dứt khoát rằng:

1. **R@1 không phản ánh độ an toàn vật lý:** Các mô hình có R@1 cao vượt trội (LPN: 67.22%, FSRA: 64.48%) vẫn chứa đựng rủi ro đuôi khổng lồ ($p95 > 3.2\text{km} - 3.5\text{km}$) và có hơn $11.7\% - 12.7\%$ các trường hợp bay lạc sang khuôn viên trường khác (>1km).
2. **Median Blindness là hiện tượng có thật về mặt toán học:** Khi R@1 > 50%, Metric Median sụp đổ về $0.00\text{m}$ và hoàn toàn mất năng lực phát hiện rủi ro phân phối đuôi.
3. **SDM không thể làm hàm mục tiêu an toàn:** Do bão hòa phẳng sau $50\text{m}-100\text{m}$, điểm số SDM triệt tiêu về $0.0000$ đối với mọi lỗi lớn, làm mất khả năng phân cấp mức độ nguy hại của các lỗi định vị.
4. **Sự tự tin sai lầm (Overconfidence Under Visual Aliasing):** Các sai số trôi dạt xuyên trường xảy ra kèm theo Cosine Similarity rất cao ($s_1 \approx 0.60 - 0.81$), chứng minh UAV không thể tự phát hiện lỗi dựa trên điểm số tương đồng nếu không có cơ chế lọc rủi ro ngoại lai (outlier rejection).

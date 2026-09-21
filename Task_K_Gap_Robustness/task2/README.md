# Task 2: Đo lường Rủi ro Đuôi và Sự Tê Liệt của Thước đo Trung vị (Tail Risk & Median Blindness)

## 1. Mục tiêu Nghiên cứu
Thực nghiệm Task 2 nhằm kiểm chứng thực nghiệm hai luận điểm cốt lõi của **Research Gap 3**:
1. **Sự tê liệt của thước đo trung vị ($\text{Median} / p50$):** Đối với bất kỳ mô hình nào đạt độ chính xác $R@1 > 50\%$ trên nhãn rời rạc (chẳng hạn như FSRA đạt $64.48\%$ và LPN đạt $67.22\%$), giá trị trung vị sai số địa lý bị ép phẳng hoàn toàn về **$0.00\text{ m}$**, tạo ra ảo ảnh đánh lừa rằng mô hình gần như không có sai số.
2. **Nguy cơ rủi ro đuôi bị che giấu (Tail Risk Exposure):** Dù trung vị bằng $0.00\text{ m}$, các thước đo phân vị đuôi ($p90, p95, p99$) và tỷ lệ rủi ro vượt ngưỡng ($\text{GFR@100}$) phơi bày nguy cơ an toàn bay nghiêm trọng: $p95$ nổ tung lên **$> 3.200\text{ m} - 3.500\text{ m}$** (máy bay trôi dạt sang hẳn trường đại học khác) và có tới **$17\% - 19\%$** số chuyến bay gặp sự cố sai số vượt quá $100\text{ m}$.

---

## 2. Cấu trúc Thư mục Task 2
```text
Task_K_Gap_Robustness/task2/
├── README.md                          # Báo cáo phương pháp luận và kết quả thực nghiệm Task 2
├── task2_tail_risk_metrics.py         # Script tính toán phân vị đuôi và khoảng tin cậy Bootstrap 95%
└── results/
    ├── tail_risk_comparison.csv       # Bảng đối chiếu chéo chỉ số rủi ro đuôi giữa các mô hình (CSV)
    └── tail_risk_detailed.json        # Báo cáo chi tiết đầy đủ phân vị và khoảng tin cậy (JSON)
```

---

## 3. Phương pháp luận & Công thức Toán học

### 3.1. Sai số Khoảng cách Top-1
Với mỗi query $q$, trích xuất ứng viên Top-1 $\hat{p}_1$ trong 18.198 ô vệ tinh gallery:
$$E_q = \text{Haversine}(p_q, \hat{p}_1)$$
trên toàn bộ $N_q = 2.331$ ảnh test.

### 3.2. Phân vị Thống kê & Khoảng Tin cậy Bootstrap 95%
Xác định phân vị $p_k$:
$$p_k = \text{Percentile}(E, k), \quad k \in \{50, 75, 90, 95, 99\}$$
Với mỗi phân vị, tính khoảng tin cậy 95% Bootstrap phi tham số (Non-parametric Bootstrap Confidence Interval) qua $B = 1.000$ lần tái lấy mẫu (resamples).

### 3.3. Tỷ lệ Lỗi Nghiêm trọng (Gross Failure Rate) & Khoảng Tin cậy Wilson
$$\text{GFR@}\rho = \frac{1}{N_q} \sum_{q=1}^{N_q} \mathbb{I}(E_q > \rho\text{m}) \times 100\%$$
Khoảng tin cậy $95\%$ cho tỷ lệ nhị thức $\text{GFR@}\rho$ được tính bằng công thức Wilson score interval:
$$\text{CI}_{95} = \frac{\hat{p} + \frac{z^2}{2n} \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}$$
với $z = 1.95996$.

### 3.4. Tỷ lệ Trôi dạt Xuyên Khuôn viên (Cross-Campus Catastrophic Drift)
Do các cụm trường đại học trong DenseUAV cách nhau từ $1\text{km}$ đến hơn $5\text{km}$, mọi sai số $E_q > 1.000\text{m}$ đại diện cho việc UAV định vị nhầm sang một khuôn viên đại học khác:
$$\text{Drift Rate (>1km)} = \frac{1}{N_q} \sum_{q=1}^{N_q} \mathbb{I}(E_q > 1000\text{m}) \times 100\%$$

---

## 4. Bảng Kết quả Thực nghiệm Đối chiếu Đa Mô hình

Trích xuất từ [tail_risk_comparison.csv](file:///media/ml4u/Extreme%20SSD/Paper_UAV/Task_K_Gap_Robustness/task2/results/tail_risk_comparison.csv):

| Mô hình | $R@1$ (%) | $\text{SDM@1}$ (%) | $\text{Median } p50$ (m) | $p90$ (m) | $p95$ (m) [Bootstrap 95% CI] | $\text{GFR@50}$ (%) | $\text{GFR@100}$ (%) [Wilson 95% CI] | Lỗi $> 1\text{km}$ (Trôi liên trường) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Baseline (ViT-S)** | 19.26% | 23.53% | 751.10m | 3989.39m | 4757.74m [4596.2, 4857.4] | 67.70% | 63.02% [61.04, 64.96] | **46.42%** (1.082 ảnh) |
| **ResNet-50** | 41.36% | 48.33% | 20.07m | 2351.40m | 3756.63m [3437.6, 3883.5] | 37.02% | 33.50% [31.62, 35.45] | **24.45%** (570 ảnh) |
| **FSRA (ViT-S)** | 64.48% | 68.51% | **0.00m** | 1446.26m | **3557.24m [3080.2, 3789.8]** | 22.48% | **19.05% [17.50, 20.69]** | **12.66%** (295 ảnh) |
| **LPN (ViT-S)** | 67.22% | 71.04% | **0.00m** | 1318.72m | **3220.78m [2698.3, 3606.9]** | 20.51% | **17.12% [15.64, 18.70]** | **11.67%** (272 ảnh) |

---

## 5. Phát hiện Khoa học Chứng minh Research Gap 3

1. **Thước đo Trung vị ($x_{50}$) bị tê liệt và vô hiệu hóa trước mô hình tốt:**
   * Cả FSRA ($R@1 = 64.48\%$) và LPN ($R@1 = 67.22\%$) đều có giá trị trung vị **$\text{Median} = 0.00\text{ m}$**. 
   * Nếu chỉ nhìn vào trung vị, người vận hành sẽ lầm tưởng hệ thống có độ chính xác tuyệt đối ở đa số các điểm đo.
2. **Sự bùng nổ của Rủi ro Đuôi (Tail Risk Exposure):**
   * Mặc dù $\text{Median} = 0.00\text{m}$, nhưng ở phân vị $95\%$, sai số của FSRA vọt lên tới **$3.557\text{ m}$** ($3.5\text{ km}$), và của LPN là **$3.220\text{ m}$** ($3.2\text{ km}$).
   * Tỷ lệ lỗi nguy hiểm vượt ngưỡng an toàn bay $\text{GFR@100}$ của FSRA là **$19.05\%$** (gần $1/5$ số lần định vị) và có tới **$12.66\%$** số truy vấn (295 ảnh) định vị lạc sang hẳn một trường đại học khác ($> 1\text{km}$).
3. **Thước đo SDM@1 che giấu độ lớn thảm họa:**
   * Điểm số $\text{SDM@1}$ của FSRA vẫn hiển thị rất cao (**$68.51\%$**), hoàn toàn không đưa ra bất kỳ cảnh báo nào về các ca lỗi đuôi $3.5\text{km}$, vì hàm mũ $e^{-5000 \times d}$ đã ép phẳng điểm số của mọi ca lệch ngoài $50\text{m}$ về $0.0000$.

---

## 6. Hướng dẫn Tái hiện Thực nghiệm
```bash
# Chạy đánh giá tự động trên tất cả checkpoint:
python task2/task2_tail_risk_metrics.py

# Hoặc chỉ định các checkpoint cụ thể:
python task2/task2_tail_risk_metrics.py \
    --mat_paths data/pytorch_result_baseline.mat data/pytorch_result_fsra.mat data/pytorch_result_resnet.mat \
    --model_names Baseline FSRA ResNet50 \
    --gps_path data/Dense_GPS_ALL.txt
```

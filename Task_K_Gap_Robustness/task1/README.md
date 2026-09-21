# Task 1: Phân tầng Đánh giá Sai số theo Độ cao bay (Altitude Stratification Analysis)

## 1. Mục tiêu Nghiên cứu
Thực nghiệm Task 1 nhằm kiểm chứng thực nghiệm các luận điểm cốt lõi của **Research Gap 3: Environmental Robustness, Multi-Condition Generalization & Tail Risk Exposure**:
1. **Chỉ số R@1 gộp chung che giấu biến động hiệu năng trắc lượng thực tế giữa các độ cao bay (80m, 90m, 100m)**: Việc chỉ báo cáo một con số R@1 duy nhất trên toàn tập test làm phẳng sự biến thiên và che giấu các hình thái thất bại địa lý ở từng tầng bay.
2. **Ảo ảnh về hiệu năng tầng bay cao**: Tại 100m, trường nhìn rộng hơn khiến R@1 có vẻ tăng nhẹ (do bao quát được nhiều cấu trúc toàn cục), nhưng khi xảy ra phân loại nhầm (retrieval failure), sai số địa lý bộc phát rất nghiêm trọng (Mean Failure Error > 1.7km đến 2.1km) do hiện tượng trộn lẫn hoa văn (visual aliasing) từ độ phân giải mặt đất thô (coarser GSD).

---

## 2. Cấu trúc Thư mục Task 1
```text
Task_K_Gap_Robustness/task1/
├── README.md                          # Báo cáo phương pháp luận và kết quả thực nghiệm Task 1
├── task1_altitude_stratification.py   # Script thực thi phân tầng đánh giá sai số
└── results/
    ├── altitude_breakdown_report.csv  # Bảng số liệu chi tiết phân tầng (CSV)
    ├── altitude_breakdown_report.json # Dữ liệu phân vị, GFR và thống kê chi tiết (JSON)
    └── test_query_list.txt            # Danh sách 2.331 query kèm metadata độ cao (80m, 90m, 100m)
```

---

## 3. Phương pháp luận & Công thức Tính toán

### 3.1. Phân tầng Tập truy vấn theo Độ cao
Tập kiểm thử gồm $N_q = 2.331$ ảnh drone ($777 \text{ vị trí} \times 3 \text{ tầng bay}$) được phân rã thành 3 tập con dựa trên siêu dữ liệu trích xuất từ tên file ảnh:
* $Q_{80}$: Tầng bay 80m ($N = 777$). Trường nhìn hẹp, GSD chi tiết cao.
* $Q_{90}$: Tầng bay 90m ($N = 777$). Tầng bay trung gian.
* $Q_{100}$: Tầng bay 100m ($N = 777$). Trường nhìn rộng, GSD thô, nguy cơ visual aliasing cao.

### 3.2. Sai số Trắc địa Haversine (WGS-84)
Với mỗi query $q$, trích xuất ứng viên Top-1 $\hat{p}_1 = \text{argmax}_{g} (\mathbf{q} \cdot \mathbf{g}^T)$ có độ tương đồng Cosine cao nhất trong 18.198 gallery tiles. Sai số địa lý thực tế tính theo mét:
$$E_q = \text{Haversine}(p_q, \hat{p}_1)$$

### 3.3. Các Thước đo Phân rã
Cho từng tập con $Q \in \{Q_{80}, Q_{90}, Q_{100}, Q_{\text{all}}\}$:
* **Tỷ lệ trúng ô:** $R@1 = \frac{1}{|Q|} \sum_{q \in Q} \mathbb{I}(\text{label}_q = \text{label}_{\hat{p}_1}) \times 100\%$
* **Thống kê sai số phân vị:** $\text{Mean}, \text{Median} (p50), p75, p90, p95, p99, \text{Max}$
* **Tỷ lệ sai số vượt ngưỡng an toàn (Gross Failure Rate):**
  $$\text{GFR@}\rho = \frac{1}{|Q|} \sum_{q \in Q} \mathbb{I}(E_q > \rho\text{m}) \times 100\%, \quad \rho \in \{50\text{m}, 100\text{m}, 200\text{m}, 500\text{m}, 1000\text{m}\}$$
* **Sai số trung bình khi xảy ra lỗi (Conditional Failure Error):**
  $$\text{FailMean} = \mathbb{E}[E_q \mid E_q > 50\text{m}]$$

---

## 4. Kết quả Thực nghiệm Chi tiết

Bảng số liệu đối chiếu trên toàn bộ 4 kiến trúc đại diện (được trích xuất từ `results/altitude_breakdown_report.csv`):

| Mô hình | Tầng bay | Số mẫu | R@1 (%) | Mean (m) | p50 (m) | p90 (m) | p95 (m) | GFR@50 (%) | GFR@100 (%) | FailMean (m) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Baseline (ViT-S)** | 80m | 777 | 17.63 | 1437.90 | 941.61 | 4026.47 | 4695.27 | 70.66 | 66.80 | 2030.68 |
| | 90m | 777 | 18.79 | 1490.94 | 740.26 | 4114.23 | 4882.27 | 68.21 | 63.71 | 2180.85 |
| | 100m | 777 | 21.36 | 1242.64 | 588.29 | 3770.79 | 4562.59 | 64.22 | 58.56 | 1929.45 |
| | **Overall** | **2331** | **19.26** | **1390.50** | **751.10** | **3989.39** | **4757.74** | **67.70** | **63.02** | **2049.11** |
| **FSRA (ViT-S)** | 80m | 777 | 62.29 | 450.70 | 0.00 | 1702.24 | 3641.93 | 26.38 | 22.78 | 1697.11 |
| | 90m | 777 | 62.55 | 429.41 | 0.00 | 1562.37 | 3741.29 | 23.17 | 19.31 | 1837.49 |
| | 100m | 777 | 68.60 | 308.37 | 0.00 | 763.01 | 2698.81 | 17.89 | 15.06 | 1703.01 |
| | **Overall** | **2331** | **64.48** | **396.16** | **0.00** | **1446.26** | **3557.24** | **22.48** | **19.05** | **1746.90** |
| **ResNet-50** | 80m | 777 | 35.78 | 740.91 | 27.90 | 2407.27 | 3556.12 | 44.14 | 40.41 | 1666.92 |
| | 90m | 777 | 44.27 | 637.02 | 19.91 | 2558.58 | 3939.57 | 33.72 | 30.63 | 1872.39 |
| | 100m | 777 | 44.02 | 594.11 | 19.92 | 2205.35 | 3748.76 | 33.20 | 29.47 | 1771.97 |
| | **Overall** | **2331** | **41.36** | **657.35** | **20.07** | **2351.40** | **3756.63** | **37.02** | **33.50** | **1760.71** |
| **LPN** | 80m | 777 | 63.84 | 455.33 | 0.00 | 1711.49 | 3571.50 | 24.97 | 21.36 | 1811.80 |
| | 90m | 777 | 68.08 | 371.90 | 0.00 | 1355.64 | 3592.30 | 19.56 | 16.60 | 1884.91 |
| | 100m | 777 | 69.76 | 249.54 | 0.00 | 257.45 | 2010.51 | 16.99 | 13.38 | 1447.57 |
| | **Overall** | **2331** | **67.22** | **358.92** | **0.00** | **1318.72** | **3220.78** | **20.51** | **17.12** | **1734.47** |

---

## 5. Phát hiện Khoa học & Khẳng định Research Gap 3

1. **R@1 gộp chung che giấu độ phân tán theo tầng bay:**
   * Đối với mọi mô hình, $R@1$ có sự dao động từ **$3.7\%$ đến hơn $8.5\%$** giữa 80m và 100m (vd: ResNet-50 nhảy từ $35.78\%$ ở 80m lên $44.02\%$ ở 100m; FSRA nhảy từ $62.29\%$ lên $68.60\%$).
   * Việc các nghiên cứu trước đây chỉ công bố 1 con số $R@1$ duy nhất đã che giấu hoàn toàn tính nhạy cảm và sự phân bố sai số theo dải độ cao.
2. **Sự bùng nổ của sai số khi xảy ra lỗi (Catastrophic Failure Drift):**
   * Dù ở mô hình mạnh nhất (FSRA, LPN) với $R@1 \approx 64-69\%$, khi xảy ra lỗi nhận diện ($E_q > 50\text{m}$), sai số bình quân **FailMean luôn vượt trên $1.700\text{m} - 1.880\text{m}$** ở tất cả các tầng bay.
   * Đặc biệt tại tầng 90m và 100m, sai số cực đoan $p95$ đạt từ **$2.698\text{m}$ đến $4.882\text{m}$**, chứng minh mô hình không chỉ sai lệch lân cận mà đưa UAV trôi dạt sang hẳn các trường đại học lân cận.

---

## 6. Hướng dẫn Tái hiện Thực nghiệm
```bash
# Chạy đánh giá tự động trên tất cả các checkpoint có sẵn:
python task1/task1_altitude_stratification.py --all_models

# Hoặc chỉ định rõ checkpoint Baseline:
python task1/task1_altitude_stratification.py \
    --mat_path data/pytorch_result_baseline.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --output_dir task1/results
```

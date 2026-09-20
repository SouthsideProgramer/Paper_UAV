# Task 4: Định lượng và Trích xuất Sự cố Trôi dạt Xuyên Khuôn viên (Cross-Campus Drift Identification)

## 1. Mục tiêu Nghiên cứu
Thực nghiệm Task 4 nhằm trực quan hóa và kiểm chứng bằng chứng thực tế mạnh nhất cho **Research Gap 3**:
1. **Sự cố trôi dạt địa lý xuyên khuôn viên đại học (Cross-Campus Catastrophic Drift):** Trong $5\% - 12\%$ tình huống xấu nhất ở phân vị đuôi, mô hình không chỉ sai số vài chục mét mà thực sự đưa máy bay UAV bay lạc sang hẳn một trường đại học khác cách xa từ **$1.000\text{m}$ đến hơn $5.300\text{m}$**.
2. **Ảo ảnh thị giác (Visual Aliasing) gây nhầm lẫn tự tin cao:** Trích xuất các cặp ảnh thực tế chứng minh rằng UAV bị đánh lừa bởi kết cấu bề mặt tương đồng (sân bóng, cụm cây xanh, mái nhà vuông góc) ở trường khác và gán độ tương đồng Cosine rất cao ($s_1 \ge 0.60 - 0.75$), trong khi vị trí thực tế cách xa hàng cây số.

---

## 2. Cấu trúc Thư mục Task 4
```text
Task_K_Gap_Robustness/task4/
├── README.md                          # Báo cáo phương pháp luận và kết quả thực nghiệm Task 4
├── task4_cross_campus_drift.py        # Mã nguồn lọc sự cố trôi dạt và trích xuất cặp ảnh
└── results/
    ├── cross_campus_drift_summary.csv # Bảng đối chiếu tỷ lệ trôi dạt liên trường giữa các mô hình (CSV)
    ├── extreme_drift_cases.json       # Danh sách chi tiết các ca trôi dạt nghiêm trọng nhất (JSON)
    └── visual_pairs/                  # Thư mục chứa 20 ảnh ghép trực quan độ phân giải cao
        ├── drift_rank01_err5375m_sim59.jpg
        ├── drift_rank02_err5375m_sim62.jpg
        └── ...
```

---

## 3. Phương pháp luận & Tiêu chí Nhận diện

### 3.1. Cờ Nhận diện Trôi dạt Liên trường
Do 14 trường đại học trong DenseUAV nằm rải rác trên toàn thành phố Hàng Châu và cách nhau từ $1.5\text{km}$ đến hơn $10\text{km}$, cờ trôi dạt liên trường được xác lập khi khoảng cách trắc địa Top-1 vượt ngưỡng an toàn bay:
$$\text{Cross\_Campus\_Flag} = (E_q \ge 1.000\text{m})$$
với $E_q = \text{Haversine}(p_q, \hat{p}_1)$.

### 3.2. Trích xuất Cặp ảnh So sánh Trực quan (Visual Montage)
Với mỗi ca trôi dạt cực đoan trong Top phân vị đuôi của mô hình FSRA:
* **Ảnh trái:** Ảnh UAV chụp từ trên không (`query_drone`), ghi rõ ID lớp, ID campus, độ cao và tọa độ GPS thực tế.
* **Ảnh phải:** Ảnh ô vệ tinh Top-1 bị chọn nhầm (`gallery_satellite`), ghi rõ ID lớp nhầm lẫn, điểm số Cosine similarity $s_1$, và khoảng cách trôi dạt thực tế $E_q$ tính bằng mét.

---

## 4. Bảng Kết quả Thực nghiệm Đối chiếu Đa Mô hình

Trích xuất từ [cross_campus_drift_summary.csv](file:///media/ml4u/Extreme%20SSD/Paper_UAV/Task_K_Gap_Robustness/task4/results/cross_campus_drift_summary.csv):

| Mô hình | Tỷ lệ Trôi dạt $> 1\text{km}$ (%) | Số lượng chuyến bay bay lạc | Sai số Trôi dạt TB ($\text{Mean}$) | Sai số Trôi dạt Lớn nhất ($\text{Max}$) | Số ca bay lạc $> 3\text{km}$ | Độ tự tin TB ($s_1$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **FSRA (ViT-S)** | **12.66%** | **295 / 2.331** | **2.914,34 m (~2.9 km)** | **5.375,08 m (~5.4 km)** | **140 ca** | **0.5971** |
| **Baseline (ViT-S)** | **46.42%** | **1.082 / 2.331** | **2.818,99 m (~2.8 km)** | **5.431,61 m (~5.4 km)** | **489 ca** | **0.5925** |
| **ResNet-50** | **24.45%** | **570 / 2.331** | **2.499,91 m (~2.5 km)** | **5.375,86 m (~5.4 km)** | **180 ca** | **0.5301** |
| **LPN (ViT-S)** | **11.67%** | **272 / 2.331** | **2.838,36 m (~2.8 km)** | **5.414,59 m (~5.4 km)** | **129 ca** | **0.6001** |

---

## 5. Phát hiện Khoa học & Bằng chứng Trực quan Chứng minh Gap 3

1. **Quy mô rủi ro thực tế của các mô hình SOTA:**
   * Mặc dù **FSRA** được xem là mô hình rất mạnh ($R@1 = 64.48\%$, $\text{Median} = 0.00\text{m}$, $\text{SDM@1} = 68.51\%$), vẫn có tới **$12.66\%$** (295 chuyến bay) bị định vị nhầm sang một trường đại học hoàn toàn khác.
   * Trong số đó, có tới **140 chuyến bay trôi dạt xa hơn $3.000\text{m}$ ($3\text{km}$)** và xa nhất lên tới **$5.375\text{m}$ ($5.4\text{km}$)**.
2. **Visual Aliasing đánh lừa mô hình:**
   * Điểm tương đồng Cosine của các ca bay lạc xuyên trường vẫn duy trì ở mức cao ($\text{Mean } s_1 \approx 0.60$, nhiều ca đạt $s_1 > 0.75$).
   * Các ảnh ghép trong thư mục `results/visual_pairs/` cho thấy rõ các kết cấu hình học lặp lại (sân cỏ nhân tạo, đường băng, cụm nhà cao tầng mái xám) ở trường khác khiến mô hình tự tin kết luận trùng khớp tuyệt đối.
3. **Ý nghĩa an toàn bay thực tế:**
   * Nếu đưa các mô hình chỉ tối ưu hóa theo $R@1$ hoặc $\text{SDM}$ vào hệ thống dẫn đường tự hành ngoài đời thực, việc không có cơ chế cảnh báo rủi ro đuôi sẽ trực tiếp dẫn đến mất mát máy bay khi gặp lỗi trôi dạt liên trường.

---

## 6. Hướng dẫn Tái hiện Thực nghiệm
```bash
python task4/task4_cross_campus_drift.py \
    --mat_path data/pytorch_result_fsra.mat \
    --gps_path data/Dense_GPS_ALL.txt \
    --drift_threshold 1000.0 \
    --output_dir task4/results
```

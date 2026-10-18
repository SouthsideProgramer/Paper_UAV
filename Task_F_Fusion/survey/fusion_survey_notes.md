# F1 — Khảo sát: định vị UAV không GPS bằng fusion camera (retrieval ảnh vệ tinh) + IMU

> Ngày: 2026-10-01. Mục đích: xác định (1) ai đã làm gì, (2) dataset nào có IMU thật, (3) điểm mới của nhóm.
> Các mục ghi "chưa xác minh" là thông tin lấy từ abstract/README, cần đọc full paper trước khi trích dẫn.

## 1. Công trình liên quan gần nhất

| Công trình | Năm | Cách fusion | Đo lường tuyệt đối | Kết quả báo cáo | Khác với hướng của nhóm |
|---|---|---|---|---|---|
| **NaviLoc** — *Trajectory-Level Visual Localization for GNSS-Denied UAV Navigation*, Drones 10(2):97 | 01/2026 | Tối ưu **theo cả quỹ đạo** (batch, 3 giai đoạn): căn SE(2) toàn cục → xoay ảnh theo heading từ VIO → tinh chỉnh cục bộ. Training-free. | VPR (AnyLoc-VLAD / MobileNet-V3) coi là đo nhiễu | MLE 19.5 m, ATE ~20 m, nông thôn 50–150 m; nhanh hơn 16× so với AnyLoc-VLAD, 32× so với VIO trôi | Là **đối thủ trực tiếp nhất**. Batch, không phải online filter; không mô hình hoá độ bất định của retrieval; đánh giá bằng trung bình (MLE/ATE), không đo lỗi đuôi |
| **FoundLoc** (arXiv 2310.16299) | 2023 | VIO + VPR foundation model (AnyLoc); chi tiết filter chưa xác minh | VPR trên ảnh vệ tinh | Trung bình < 20 m, không cần pose ban đầu | Dùng feature tổng quát, không dùng mô hình cross-view đã train; dataset Nardo-Air có IMU |
| **SWA-PF** (arXiv 2509.13795), cùng nhóm tác giả DenseUAV | 09/2025 | **Particle filter** 4-DoF (x, y, h, yaw), motion model từ odometry (vận tốc tuyến tính/góc) | So khớp **bản đồ ngữ nghĩa** (Semantic-weighted Distance Map), không dùng retrieval | < 10 m, nhanh hơn 10× so với trích feature | Phủ nhận hướng retrieval; yếu ở vùng ít đặc trưng và vùng nhập nhằng. Dataset MAFS (14 campus, 100–500 m) |
| Kinnari et al., *GNSS-denied geolocalization… with orthophotos* (arXiv 2103.14381) | 2021 | VIO + so khớp ảnh với orthophoto, có particle filter | Template matching | — | Hướng cổ điển, không học sâu cross-view |
| Goforth & Lucey, *GPS-Denied UAV Localization using Pre-existing Satellite Imagery*, ICRA 2019 | 2019 | VO + căn chỉnh CNN với ảnh vệ tinh | Căn chỉnh ảnh | — | Nền tảng, hay được trích |
| SatLoc (Remote Sensing 17(17):3048) | 2025 | "Hierarchical adaptive fusion" (chưa xác minh chi tiết, trang 403) | Matching UAV↔vệ tinh, 100–300 m | — | Cần đọc thêm |

**Kết luận:** ý tưởng "VIO + khớp ảnh vệ tinh" **đã có**. Nếu paper chỉ nói "retrieval + EKF" thì sẽ bị từ chối vì thiếu tính mới.

## 2. Dataset có IMU + ảnh UAV + ảnh vệ tinh

| Dataset | IMU? | Chuỗi bay? | Độ cao | Ảnh vệ tinh | Tải được | Ghi chú |
|---|---|---|---|---|---|---|
| **DenseUAV** (đang dùng) | ❌ | ❌ (điểm rời rạc, bước ~20 m) | 80/90/100 m | ✅ | ✅ (GPS không public) | Chỉ dùng được cho **bán mô phỏng** |
| **MAFS** (SWA-PF) | Có trong dữ liệu thu, **chưa rõ phần open-source có IMU không** (README chỉ ghi `gps.txt`) | ✅ video 30 fps | 100–500 m | ✅ (kèm bản đồ ngữ nghĩa) | Baidu Pan, mới public "một phần" | 14 campus giống miền DenseUAV → **ứng viên số 1**, cần tải và kiểm tra |
| **Nardo-Air** (FoundLoc) | ✅ | ✅ | chưa xác minh | ✅ | Google Drive | Dùng để so trực tiếp với FoundLoc |
| **MARS-LVIG** (DJI M300 RTK) | ✅ BMI088 (trong Livox Avia) | ✅ ROS bag, camera 10 Hz | 80–130 m | ❌ phải tự lấy tile vệ tinh | ✅ | GT RTK rất tốt; địa hình rừng/núi/đảo, ít giống campus |
| **AerialVL** | ❌ theo README (chỉ camera + GNSS) | ✅ 11 chuỗi, ~70 km | nhiều độ cao | ✅ | ✅ MIT | Dùng được nếu sinh IMU từ GT, hoặc chỉ dùng VO |
| **UAV-VisLoc** | ❌ (có lat/lon/độ cao) | một phần | nhiều | ✅ 11 bản đồ | ✅ | Chủ yếu cho định vị từng ảnh |

**Đề xuất dữ liệu:** (a) bán mô phỏng trên DenseUAV để phát triển phương pháp; (b) MAFS (nếu có IMU) hoặc Nardo-Air làm dữ liệu thật chính; (c) MARS-LVIG làm dữ liệu thật phụ với IMU chuẩn.

## 2b. Kết quả kiểm tra dataset (F4, 2026-10-01)

Kiểm tra trực tiếp README / file thật, không dựa vào abstract:

| Dataset | Phát hiện | Kết luận |
|---|---|---|
| **MAFS** (SWA-PF) | README chỉ có `map/` (`img.png`, `label.png`, `detail.txt`) và `route/` (ảnh liên tiếp + `gps.txt` dạng `path lat lon height`). **Không có IMU / odometry** trong bản public. Chỉ có trên Baidu Pan (mã 8888), 15 địa điểm, 100–500 m | Miền giống DenseUAV nhất nhưng không có IMU, tải khó → phụ |
| **Nardo-Air** (FoundLoc) | Thư mục Google Drive chỉ có `test_40_midref_rot{0,90}.zip` (~64 MB, 71 query / 102 tile, bản VPR của AnyLoc). **Không có IMU, không có chuỗi liên tục**; bay 50 m trên đường băng cỏ | **Loại** (quá nhỏ, không có IMU) |
| **AerialVL** (RA-L 2024, MIT) | HF `hmf21/AerialVL`, tải trực tiếp được. `VAL` = 11 chuỗi bay 3.7–11 km (~70 km tổng), ảnh tên `@UTC@lon@lat@.png` (hướng đông), 2 bản đồ vệ tinh Google Earth căn bắc kèm toạ độ góc; GNSS NovAtel 1.5 m RMS. Phần HF **không có IMU**. Kích thước: VAL 58 GB, VPR 28 GB, train vệ tinh 11 GB | **Chọn làm dữ liệu thật chính**: ảnh thật liên tiếp + quỹ đạo thật + bản đồ vệ tinh → aliasing thật theo thời gian; IMU/VIO tạm sinh từ quỹ đạo GNSS |
| **GeoVINS** (T-RO 2025, cùng nhóm AerialVL) | Rosbag thô (có IMU) của AerialVL/GeoVINS phát hành trên Baidu (2025-09, 2026-05), DEM 2026-06 | Nguồn **IMU thật** cho AerialVL; cần tài khoản Baidu. GeoVINS cũng là **đối thủ mới** (VINS + bản đồ địa lý), phải đọc và so sánh |
| **MARS-LVIG** (HKU, CC BY-NC-SA) | 23 chuỗi rosbag, 80–130 m, 3–12 m/s, 6–23 phút; có IMU (Livox Avia), RTK GT; sân bay mô hình, đảo, thị trấn, thung lũng; tải từ `mars.hku.hk/dataset.html` | Dự phòng có IMU thật chuẩn; phải tự lấy tile vệ tinh |
| **UAVScenes** (HF `sijieaaa/UAVScenes`) | Ảnh + LiDAR + nhãn ngữ nghĩa của MARS-LVIG (37 GB), file trên HF không thấy IMU | Không dùng cho fusion |

**Định dạng AerialVL đã kiểm tra (đọc header phần zip 1, 2026-10-01):** ảnh PNG 2048×1536, ~3.3 MB, **2 Hz** (timestamp ms trong tên file), GNSS trong tên file; tốc độ khoảng 6 m/s ở đầu chuỗi `2023-03-16-18-04-01`. Bản đồ `large_map` 5888×3584 px, `small_map` 3328×2048 px, GSD **≈ 0.96 m/px**, phủ ~5.6 × 3.4 km (nông thôn ven Thanh Đảo: ruộng, làng). Ảnh mẫu bay lúc ~18:06 giờ địa phương (tối) và phủ cỡ vài trăm mét → độ cao lớn hơn DenseUAV nhiều; ảnh xoay 90° so với bản đồ (ảnh hướng đông). Mẫu trích ra ở `datasets/AerialVL/peek/`. ⚠ Lệch miền lớn: gần như chắc chắn phải fine-tune retrieval; cần kiểm tra phần VPR có trùng vùng / chuyến bay với VAL không để tránh rò rỉ.

**Rủi ro AerialVL:** lệch miền với DenseUAV (độ cao và địa hình khác, không phải campus) → model retrieval train trên DenseUAV có thể yếu khi chạy zero-shot; cần đo R@1 / Top-K trước, có thể phải fine-tune trên phần `VPR` / `vpr_training_data` của AerialVL.

## 3. Điểm mới đề xuất cho nhóm

Xuất phát từ chính các research gap đã chứng minh, không phải ý tưởng chung chung:

1. **Mô hình đo có hiệu chỉnh cho retrieval cross-view.** Similarity s₁ không dự báo được lỗi (GeoAUROC ~0.52–0.57). Dùng **độ phân tán Top-K** (Spatial Mismatch task 2) để đặt hiệp phương sai R của phép đo, thay vì hằng số hoặc theo score.
2. **Gating theo chuyển động.** Kiểm định χ² trên innovation (khoảng cách Mahalanobis) để loại các ca cross-campus (12 % query > 1 km) và các lỗi tự tin cao (s₁ = 0.77 mà sai 5.4 km). Đây là phiên bản có nguyên lý của K5 spatial gating (K5 thất bại vì không có prior chuyển động).
3. **Đo đa giả thuyết.** Coi Top-K là hỗn hợp Gaussian trong particle filter, thay vì chỉ lấy top-1 hay centroid (centroid đã được chứng minh là làm hỏng kết quả, Spatial Mismatch task 3).
4. **Đánh giá theo lỗi đuôi.** Báo GFR@ρ, p95, lỗi lớn nhất, thời gian phục hồi sau khi bị bắt cóc (kidnapped), chứ không chỉ MLE/ATE như NaviLoc. Tái sử dụng K1 `eval_metrics.py`.
5. **Phân tích độ nhạy:** lợi ích fusion theo cấp IMU (consumer / tactical), theo tần số retrieval và theo R@1 của backbone, trả lời câu hỏi thực tế "retrieval cần tốt đến mức nào khi đã có IMU?".

Câu luận điểm đề xuất: *"Retrieval cross-view có lỗi đuôi nặng và độ tự tin sai; chúng tôi cho thấy một bộ lọc quán tính với mô hình đo dựa trên độ phân tán Top-K và gating χ² loại gần hết lỗi thảm hoạ, giảm p95 từ cấp km xuống cấp chục mét."*

## 4. Rủi ro

- NaviLoc (01/2026) rất gần; cần đọc full paper và so sánh trực tiếp nếu có code.
- Nếu MAFS open-source không có IMU và Nardo-Air khó dùng, phải dựa vào MARS-LVIG + tự tải ảnh vệ tinh (tốn công, cần kiểm tra bản quyền ảnh).
- Heading: ảnh drone DenseUAV không căn hướng bắc chuẩn; khi chạy trên video thật cần xoay ảnh theo yaw từ IMU (giống NaviLoc stage 2).
- Vẫn phụ thuộc Giai đoạn 0 (tái lập R@1 ≥ 78 %).

## Nguồn

- NaviLoc: https://www.mdpi.com/2504-446X/10/2/97 · https://ui.adsabs.harvard.edu/abs/2026Drone..10...97S/abstract
- FoundLoc: https://arxiv.org/abs/2310.16299 · https://anyloc.github.io/FoundLoc/
- SWA-PF / MAFS: https://arxiv.org/abs/2509.13795 · https://github.com/YuanJiayuuu/SWA-PF
- Kinnari et al.: https://arxiv.org/abs/2103.14381
- Goforth & Lucey, ICRA 2019: https://dl.acm.org/doi/10.1109/ICRA.2019.8793558
- SatLoc: https://www.mdpi.com/2072-4292/17/17/3048
- MARS-LVIG / UAVScenes: https://arxiv.org/abs/2507.22412
- AerialVL: https://github.com/hmf21/AerialVL
- UAV-VisLoc: https://arxiv.org/abs/2405.11936
- AerialVL: https://github.com/hmf21/AerialVL · https://huggingface.co/datasets/hmf21/AerialVL
- GeoVINS (T-RO 2025): https://ieeexplore.ieee.org/document/11176431
- MARS-LVIG: https://mars.hku.hk/dataset.html
- Danh sách dataset: https://github.com/michaelschleiss/awesome-aerial-localization-datasets

# F5 — Fusion trên chuyến bay thật AerialVL

Dữ liệu: [AerialVL](https://github.com/hmf21/AerialVL) phần `VAL` (HF `hmf21/AerialVL`, tải bằng `datasets/AerialVL/download_val.sh`, giải nén vào `datasets/AerialVL/extracted/`).

**Thật:** ảnh UAV (2 Hz), quỹ đạo GNSS (1.5 m RMS), bản đồ vệ tinh, Top-K retrieval.
**Mô phỏng:** IMU / VIO, sinh từ quỹ đạo GNSS thật bằng đúng mô hình nhiễu của F2/F3 (`../prototype/sensors.py`). Rosbag IMU thật có trên Baidu (GeoVINS), chưa tải.

## Giao thức

- **val** = các chuyến ngày 2023-03-11 và 2023-03-16 (được chẩn đoán, chỉnh, hiệu chỉnh lệch camera).
- **test** = các chuyến ngày 2023-03-18, chạy **một lần** với thiết kế đã đóng băng (MH-EKF v3, `FROZEN_CFG` trong `run_aerialvl.py`).
- Một "run" = cửa sổ 240 s của một chuyến (bắt đầu mỗi 20 s) × một seed nhiễu IMU/VIO. Các run trong cùng chuyến tương quan với nhau → luôn báo kèm kết quả theo chuyến.

## Hình học (F5-00, `footprint_scan.py`)

Ảnh có hướng cố định, **đỉnh ảnh = hướng đông** → xoay 90° theo chiều kim đồng hồ để đưa về hướng bắc. Footprint theo chiều đông–tây là ~200 m (đo bằng NCC trên ảnh gradient so với bản đồ). SIFT + RANSAC thất bại vì ruộng lặp và khác mùa. Query = cắt vuông 200 m ở giữa ảnh; gallery = tile 200 m, bước 25 m trên `large_map` (28 340 tile, GSD 0.96 m/px).

## File

| File | Việc |
|---|---|
| `aerialvl_io.py` | Đọc bản đồ (toạ độ góc trong tên file), danh sách ảnh (`@UTC ms@lon@lat@.png`), đổi toạ độ |
| `footprint_scan.py`, `register_frames.py` | F5-00: đo footprint / hướng xoay (`register_frames.py` = thử SIFT, thất bại, giữ để truy vết) |
| `aerialvl_extract.py` | Feature retrieval (venv DenseUAV, checkpoint đã train) cho tile và ảnh → `feats/<model>_s<seed>.npz`; `--gallery_from` dùng lại feature gallery |
| `eval_retrieval.py` | Lỗi top-1 / Top-10 theo chuyến |
| `run_aerialvl.py` | Fusion: quỹ đạo GNSS → spline 100 Hz (yaw thân bám hướng bay, ≤ 0.5 rad/s), IMU/VIO mô phỏng, đo = Top-K thật 1 Hz; `--calib val` trừ lệch hệ thống camera (đo trên val) |
| `run_f5_test.sh`, `aggregate_f5.py` | F5-04: 9 model × 4 kịch bản trên test; bảng tổng hợp |
| `extract_long.sh` | F5-05: 6 chuyến dài, giải nén từng chuyến → feature → xoá ảnh (thiếu ổ đĩa) |

## Phát hiện chính trên val (chi tiết: F5-01..03 trong `EXPERIMENT_LOG.md`)

1. Retrieval DenseUAV zero-shot vẫn có ích (LPN: top-1 ≤ 50 m 36 %, Top-10 có ứng viên đúng 63 %), nhưng lỗi đuôi p95 ~3.8 km.
2. Lệch hệ thống ~23 m về phía nam giữa tâm tile top-1 và GNSS → hiệu chỉnh trên val.
3. Aliasing kéo dài tới 79 s; có đoạn ~130 s không ứng viên đúng nào. Luật tìm lại vị trí `3σ + v_max·Δt` (v2) cho phép nhảy sang alias → **v3**: chỉ tìm lại trong 3σ của hiệp phương sai lan truyền. Trên DenseUAV val, v3 cho kết quả trùng v2.

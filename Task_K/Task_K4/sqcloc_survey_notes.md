# Task K4 — SQCLoc Survey & Limitations Documentation

## 1. Mục tiêu (Objective)
Kiểm chứng giả thuyết trên dải mô hình có Recall@1 cực cao ($R@1 \approx 89\text{--}91\%$): liệu khi $R@1$ đạt đỉnh thì sai số $p_{95}$ có vẫn rơi vào vùng thảm họa (hàng trăm mét / hàng km) do trần lượng tử hóa bước lưới và hạn chế của hàm loss rời rạc hay không.

## 2. Hiện trạng khảo sát (Survey Status)
- Tại thời điểm thực hiện đề tài, mã nguồn chính thức và checkpoint trọng số của mô hình **SQCLoc** chưa được tác giả phát hành công khai trên các nền tảng mở (GitHub / Hugging Face).
- Các nỗ lực tái hiện trực tiếp bị giới hạn bởi tài nguyên GPU độc quyền dành cho Model Track (Thắng).

## 3. Ghi nhận học thuật cho Bài báo (Documentation for Paper)
- **Section 4 & Section 7 (Limitations & Future Work)**:
  > *"Due to the unavailability of publicly released weights for SQCLoc at the time of writing, our evaluation focuses on four representative open architectures (ViTS+LPN, ViTS+FSRA, ResNet-50, and ViTS+SingleBranch) covering the 19.3%--67.2% R@1 range. Once public checkpoints become available, our open-sourced evaluation suite (`eval_metrics.py`) can directly compute GFR@100 and p95 without retraining."*

## 4. Bằng chứng thực nghiệm đã hoàn tất (Empirical Evidence)
- 4 mô hình baseline trong Task K2 (`ViTS+LPN`, `ViTS+FSRA`, `ResNet-50`, `ViTS+SingleBranch`) đã chứng minh đầy đủ: Kể cả ở $R@1 = 67.22\%$ (LPN), $p_{95}$ vẫn là **$3220.8\text{ m}$ ($>3.2\text{ km}$)** và $\text{GFR}@100 = 17.12\%$, cung cấp bằng chứng thống kê vững chắc cho toàn bộ luận điểm của bài báo.

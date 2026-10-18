# F2 — Prototype bán mô phỏng: fusion retrieval cross-view + IMU/VIO

Mục tiêu: kiểm tra **trước khi có dữ liệu thật** xem việc kết hợp retrieval drone → vệ tinh (đo vị trí tuyệt đối, có lỗi đuôi nặng) với IMU/VIO (đo chuyển động tương đối, trôi dần) có loại được lỗi thảm hoạ hay không, và biến thể bộ lọc nào đáng theo đuổi.

Chỉ cần `numpy` + `matplotlib`. Chế độ `--world real` cần thêm `scipy`, file `.mat` và `Dense_GPS_ALL.txt` (chỉ có trên server).

## Cấu trúc

| File | Nội dung |
|---|---|
| `world.py` | Lưới tile vệ tinh (bước 19.71 m như DenseUAV): tổng hợp 14 campus, hoặc thật từ GPS (campus = thành phần liên thông, liên kết < 150 m). Sinh quỹ đạo bay trơn giữa các tile trong một campus (4–8 m/s, quay ≤ 0.35 rad/s). |
| `sensors.py` | IMU 2-D 100 Hz (bias bật máy + random walk + nhiễu trắng; cấp `consumer`/`tactical`), VIO 10 Hz (sai scale 2 %, lệch yaw 3° trôi 0.5°/√phút, bias vận tốc random walk → trôi ~1.2 % quãng đường). Retrieval: `SyntheticRetrieval` (hiệu chỉnh theo K2) hoặc `MatRetrieval` (Top-K thật từ `.mat`). |
| `filters.py` | Các phương pháp so sánh (bảng dưới). |
| `metrics.py` | GFR@ρ, p50/p90/p95/p99, max, % chuyến bay từng lệch > 500 m; CI bootstrap **theo quỹ đạo**; hiệu số cặp. |
| `run_f2.py` | Chạy một cấu hình → `results/<tag>/{summary.json, table.md, cdf.png, errors.npz}`. |
| `analyze_f2.py` | Hiệu số cặp bất kỳ (A − B) kèm CI từ `errors.npz`. |

## Phương pháp so sánh

| Tên | Mô tả |
|---|---|
| `retrieval_top1` | Chỉ retrieval: vị trí = tâm tile top-1 (giữ giá trị cũ khi không có đo) |
| `dead_reckoning` | Chỉ VIO hoặc chỉ IMU, biết điểm xuất phát |
| `ekf_naive` | EKF, đo = top-1, R cố định (σ = 20 m), nhận mọi phép đo |
| `ekf_gated` | + gating χ² (99 %, 2 bậc tự do); sau 20 lần bị từ chối liên tiếp thì nới hiệp phương sai thêm 50 m |
| `ekf_disp_gated` | + R tăng theo độ phân tán Top-K có trọng số softmax(score/τ) (đề xuất A) |
| `ekf_dispgate` | Bỏ phép đo khi độ phân tán Top-K > `disp_thr`, rồi gating χ² (F2-11) |
| `ekf_topk_nn` | Chọn trong Top-K ứng viên gần dự đoán nhất (Mahalanobis), rồi gating |
| `mh_ekf` | Multi-hypothesis EKF: ≤ 10 giả thuyết Gaussian, mỗi tick tách thành nhánh "outlier" + một nhánh cho mỗi ứng viên Top-K qua gate, gộp các nhánh < 15 m, sinh lại giả thuyết từ Top-K nếu 20 s không được ủng hộ (đề xuất C, F2-12) |
| `pf_topk` | Particle filter 2000 hạt [x, y, δψ, s, b], likelihood = hỗn hợp Gaussian trên Top-K + sàn outlier ε = 0.3 (đề xuất B). Với IMU, hạt mang state INS 8 chiều |

## Mô hình retrieval tổng hợp và **các giả định**

Top-1 thuộc 1 trong 4 loại với xác suất lấy từ số đo của nhóm (`sensors.RETRIEVAL_PRESETS`):

| Preset | Đúng | Cục bộ ≤ 100 m | Xa, cùng campus | Khác campus | Nguồn |
|---|---|---|---|---|---|
| `baseline_vits_19` | 0.19 | 0.18 | 0.33 | 0.30 | K2 (R@1 19.26, GFR@100 63.02) |
| `fsra` | 0.645 | 0.165 | 0.07 | 0.12 | K2 + Robustness task 4 (12.66 % trôi > 1 km) |
| `lpn` | 0.672 | 0.157 | 0.06 | 0.111 | K2 + Robustness task 4 |
| `vits_82` | 0.82 | 0.08 | 0.04 | 0.06 | **Giả định** cho model tái lập 82.20 % |

Các giả định **chưa được kiểm chứng trên dữ liệu thật** (F3 sẽ kiểm):
- **Tương quan theo thời gian:** với xác suất `persist` (mặc định 0.5), loại lỗi của giây trước lặp lại và vị trí sai "đi theo" UAV.
- **Cấu trúc Top-K:** khi top-1 sai, tile đúng vẫn có trong Top-K với xác suất 0.5; các slot còn lại nằm gần một "neo" (≤ 60 m) với xác suất 0.5, còn lại là tile ngẫu nhiên (70 % cùng campus).
- **Độ phân tán có mang thông tin không:** `anchor_truth` = 0.5 nghĩa là khi sai, Top-K lẫn quanh cả chỗ đúng và chỗ sai (phân tán lớn hơn). `anchor_truth` = 0 thì độ phân tán không cho biết gì về đúng/sai.
- Score top-1 gần như không phân biệt đúng/sai (lệch 0.02), khớp với GeoAUROC ~0.55 ở K2.
- 2-D, không có vấn đề xoay ảnh theo heading, retrieval luôn chạy được khi UAV ở gần một tile có query.

## Chạy

```bash
cd Task_F_Fusion/prototype
python run_f2.py --preset fsra --motion vio --seed 0 --tag F2-01_val          # val
python analyze_f2.py results/F2-01_val ekf_gated retrieval_top1 pf_topk ekf_gated
# Trên server, retrieval thật (F3), một lệnh cho nhiều checkpoint:
bash run_f3_server.sh <Dense_GPS_ALL.txt> <ckpt_lpn>/pytorch_result_1.mat <ckpt_fsra>/pytorch_result_1.mat
# hoặc từng lần:
python run_f2.py --world real --result_mat <pytorch_result_1.mat> --gps_path <Dense_GPS_ALL.txt> --seed 0 --tag F3_lpn_val
```

Quy ước: `--seed 0` là val (được chỉnh siêu tham số), `--seed 1` là test (chỉ chạy một lần cho cấu hình đã chốt).

## Kết quả

Xem mục *Kết quả* bên dưới và các dòng F2-xx trong [`EXPERIMENT_LOG.md`](../../EXPERIMENT_LOG.md). `results_v1/` là lần chạy đầu với mô hình VIO **có lỗi** (drift bị chặn, không tăng theo quãng đường), chỉ giữ lại để truy vết, không dùng.

### Tóm tắt kết quả val (seed 0, sim v2, 100 quỹ đạo × 300 s trừ khi ghi khác)

p95 lỗi vị trí (m); `*` = hiệu số với `ekf_gated` có CI 95 % không chứa 0.

| Kịch bản | retrieval_top1 | chỉ VIO/IMU | ekf_naive | ekf_gated | ekf_disp_gated | ekf_topk_nn | pf_topk |
|---|---|---|---|---|---|---|---|
| F2-01 FSRA, VIO | 3416 | 40 | 909 | **8.3** | 22.7* | 8.9 | **7.5*** |
| F2-03/10a FSRA, IMU consumer | 3416 | 1187 | 1387 | **18.2** | 61.5 | 38.4 | 182 ✗ |
| F2-10b IMU + xuất phát sai 300 m | 3416 | 1241 | — | **34.8** | — | 1220 | 1181 ✗ |
| F2-04 xuất phát sai σ = 300 m | 3416 | 675 | 979 | 41.7 (kẹt 4 % chuyến) | 31.8 | 344 | **18.5** |
| F2-05 retrieval 10 s/lần | 3263 | 40 | 1389 | 21.2 | 35.1 | 25.2 | **17.5*** |
| F2-07a retrieval yếu (R@1 19 %) | 4759 | 40 | 1703 | 49.3 | 38.0 | 11.6* | **11.0*** |
| F2-07b retrieval mạnh (R@1 82 %) | 1952 | 40 | 667 | **6.3** | 21.6 | 8.5 | 6.4 |
| F2-08 aliasing kéo dài (persist 0.9) | 3650 | 40 | 1931 | 17.1 | 27.8 | 9.5* | **9.4*** |
| F2-09 bay 30 phút (40 quỹ đạo) | 3536 | 190 | — | 6.7 | — | 7.2 | **6.4*** |

**Đọc kết quả:**
1. **Gating là thứ quan trọng nhất.** Fusion không gating (`ekf_naive`) còn tệ hơn median của retrieval, vì lỗi cross-campus kéo bộ lọc đi xa. Có gating χ² thì p95 giảm từ cấp km xuống cấp chục mét hoặc vài mét trong mọi kịch bản.
2. **Chỉ IMU consumer** (không VIO) trôi hơn 1 km sau 5 phút; fusion giữ được khoảng 18 m. **VIO** tốt hơn nhiều nhưng vẫn trôi tăng dần (190 m sau 30 phút); fusion giữ lỗi bị chặn.
3. **Đề xuất A (R theo độ phân tán Top-K) thất bại** trong dạng hiện tại: tệ hơn R cố định ở hầu hết kịch bản, vì nó nới R cho cả phép đo đúng.
4. **Đề xuất B (PF trên Top-K) là phương án tốt nhất hoặc ngang tốt nhất ở mọi kịch bản VIO.** Lợi thế thể hiện rõ đúng ở các tình huống khó: retrieval yếu, aliasing kéo dài, không biết chính xác điểm xuất phát. Khi retrieval mạnh và điều kiện dễ thì PF ≈ EKF gated.
5. `ekf_topk_nn` mạnh khi điểm xuất phát tốt, nhưng sập khi xuất phát sai (tự khẳng định giả thuyết sai của chính nó).

6. **PF với IMU thuần thất bại** (F2-10): state 8 chiều mất đa dạng sau resample. Cần Rao-Blackwellized PF.
7. **Dispersion dùng để bỏ phép đo** (F2-11) có lợi khi retrieval yếu (49 → 24 m) nhưng có hại khi retrieval tốt (8.3 → 11+ m). Không phải cải tiến phổ quát.
8. **Kiểm tra trên `.mat` thật (F3-00, model 19 %):** khi top-1 sai, tile đúng nằm trong Top-10 ở 45.5 % trường hợp, gần giả định 50 % của mô phỏng. Tile đúng dồn ở hạng 2–3, nên có lẽ PF Top-K có lợi hơn so với mô phỏng.

### F2-12: Multi-hypothesis EKF (p95, m)

| Kịch bản | ekf_gated | pf_topk | **mh_ekf** |
|---|---|---|---|
| FSRA + VIO | 8.3 | **7.5** | 8.4 |
| Xuất phát sai 300 m (VIO) | 41.7 | 17.3 | **8.7*** |
| Retrieval yếu 19 % (VIO) | 49.3 | **11.0** | 13.6* |
| Retrieval mạnh 82 % (VIO) | **6.3** | 6.4 | 6.5 |
| Aliasing kéo dài (VIO) | 17.1 | **9.1** | 10.4* |
| Chỉ IMU | 18.2 | 182 ✗ | **16.0*** |
| Chỉ IMU + xuất phát sai 300 m | 34.8 | 1181 ✗ | **16.6*** |

`*` = khác ekf_gated có ý nghĩa (CI 95 %). Sau 30 s đầu, tỉ lệ chuyến bay từng lệch > 100 m: **mh_ekf 0–1 %**, ekf_gated 10–12 % (kẹt, tới 2 km).

9. **MH-EKF là ứng viên chính cho paper:** không bao giờ tệ hơn EKF gated (chênh ≤ 0.2 m), tốt hơn rõ ở mọi kịch bản khó, và chạy được cả với IMU thuần (PF thì không). PF nhỉnh hơn khoảng 1–2.6 m khi có VIO và xuất phát chuẩn.

### F3: Top-K **thật** (GPS thật, `.mat` baseline 19 %)

GPS tải từ HuggingFace `Dmmm997/DenseUAV` (`Dense_GPS_ALL.txt` nằm trong zip). Retrieval thật còn khắc nghiệt hơn mô phỏng: **54.6 % top-1 rơi sang campus khác** (mô phỏng giả định 30 %), và có những đoạn **> 20 s liên tục** cả Top-10 nằm ở một campus "song sinh" cách 1–4 km.

p95 (m), sau khi sửa MH-EKF (F3-03):

| Kịch bản | retrieval_top1 | chỉ VIO/IMU | ekf_gated | pf_topk | **mh_ekf** |
|---|---|---|---|---|---|
| VIO | 4437 | 29 | 66.9 | 14.7 | **14.2** |
| Chỉ IMU | 4437 | 623 | 171.7 | 107.4 | **35.4** |
| VIO + xuất phát sai 300 m | 4437 | 669 | 1284 | 645 | **32.0** |
| IMU + xuất phát sai 300 m | 4437 | 861 | 1383 | 1033 | **149.9** |

Sau 30 s đầu, % chuyến bay từng lệch > 500 m: mh_ekf **0 %** khi xuất phát chuẩn, **6 %** khi xuất phát sai (ekf_gated 26–28 %, pf_topk 7–34 %).

Hai thay đổi của MH-EKF rút ra từ dữ liệu thật (mô phỏng không lộ ra):
1. Chỉ coi là **mất dấu** khi không có ứng viên Top-K nào lọt gate của giả thuyết tốt nhất (bản đầu đếm sai → sinh lại giả thuyết dù đang bám tốt).
2. **Re-acquisition giới hạn theo vùng tới được**: chỉ sinh giả thuyết ở ứng viên trong bán kính 3σ + v_max·Δt (v_max = 10 m/s). Đây là ràng buộc vật lý "UAV không thể dịch chuyển tức thời", chặn được aliasing kéo dài theo cả vùng.

⚠ Cả hai được thiết kế **sau khi xem dữ liệu test thật** → số trên là khám phá. Để chốt số cho paper: sinh `.mat` cho các campus train (val theo campus), chọn thiết kế ở đó, rồi chạy test một lần.

### F3-05: kết quả **test** đầu tiên (ViT-S tái lập 79.67 %, campus test 11, 12, thiết kế chốt trên val)

p95 (m); trong ngoặc: % chuyến bay từng lệch > 100 m sau 30 s đầu.

| Kịch bản | retrieval_top1 | chỉ VIO/IMU | ekf_gated | pf_topk | **mh_ekf** |
|---|---|---|---|---|---|
| VIO | 1306 | 30 | 7.7 (0) | 6.4 (0) | **6.4 (0)** |
| Chỉ IMU | 1306 | 713 | 13.1 (0) | 21.3 (4) | **11.3 (0)** |
| VIO + xuất phát sai 300 m | 1306 | 670 | 682 (6) | 13.4 (0) | **6.4 (0)** |
| IMU + xuất phát sai 300 m | 1306 | 924 | 681 (7) | 618 (59) | **11.4 (0)** |

MH-EKF − EKF gated (p95) có CI 95 % không chứa 0 ở cả 4 kịch bản. Đây là số đầu tiên **đủ điều kiện đưa vào paper** (với ghi chú: 1 seed model, 1 seed quỹ đạo, IMU/VIO mô phỏng).

### F3-06: lặp lại với LPN (86.36 %), campus test 11, 12

| Kịch bản | retrieval_top1 | ekf_gated | pf_topk | **mh_ekf** |
|---|---|---|---|---|
| VIO | 77.9 | 6.6 (0) | 6.4 (0) | **6.2 (0)** |
| Chỉ IMU | 77.9 | 11.6 (0) | 20.2 (3) | **10.8 (0)** |
| VIO + xuất phát sai | 77.9 | 8.5 (3) | 13.4 (0) | **6.3 (0)** |
| IMU + xuất phát sai | 77.9 | 16.2 (3) | 578 (59) | **10.9 (0)** |

Retrieval mạnh hơn thu hẹp khoảng cách về p95, nhưng EKF gated vẫn mất dấu ở 3 % chuyến khi xuất phát sai; MH-EKF giữ 0 %.

### Tổng hợp test (campus 11, 12): 3 model retrieval tái lập × 4 kịch bản

p95 (m) của **MH-EKF** / EKF gated / chỉ retrieval; trong ngoặc là % chuyến bay mất dấu (> 100 m sau 30 s) của MH-EKF / EKF gated.

| Model (R@1) | VIO | Chỉ IMU | Xuất phát sai 300 m | IMU + xuất phát sai |
|---|---|---|---|---|
| ViT-S (79.67 %) | **6.4** / 7.7 / 1306 (0 / 0) | **11.3** / 13.1 / 1306 (0 / 0) | **6.4** / 682 / 1306 (0 / 6) | **11.4** / 681 / 1306 (0 / 7) |
| FSRA (81.85 %) | **6.8** / 7.8 / 78.7 (0 / 0) | **11.8** / 13.5 / 78.7 (0 / 0) | **6.9** / 8.5 / 78.7 (0 / 1) | **12.0** / 14.7 / 78.7 (0 / 1) |
| LPN (86.36 %) | **6.2** / 6.6 / 77.9 (0 / 0) | **10.8** / 11.6 / 77.9 (0 / 0) | **6.3** / 8.5 / 77.9 (0 / 3) | **10.9** / 16.2 / 77.9 (0 / 3) |

MH-EKF − EKF gated (p95) có CI 95 % không chứa 0 ở cả 12 ô.

**Giới hạn:** mô hình retrieval là tổng hợp. Các giả định về tương quan thời gian và cấu trúc Top-K chưa được kiểm chứng; mô phỏng 2-D; chưa xử lý heading của ảnh. Chưa chạy test (seed 1) vì thiết kế phương pháp còn thay đổi. Cần F3 (Top-K thật từ `.mat` + GPS trên server) trước khi đưa bất kỳ con số nào vào paper.

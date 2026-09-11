# Phân task — Khải & Thắng

**Thắng:** model track — pretrain, loss, Method section. Độc quyền GPU.
**Khải:** evaluation track — metrics, texture analysis, Section 3–4–6. Không dùng GPU.

**Ràng buộc:** 1× RTX 3060, ~35–40 phút/run. Chỉ Thắng nằm trên GPU-dependent path.

**Interface duy nhất:** file `pytorch_result_1.mat`, format giữ nguyên từ repo gốc. Thắng sinh ra, Khải consume. Thắng không sửa eval code, Khải không sửa `train.py`.

---

## S0 — Config chung (cả hai, ngày 1, nửa ngày)

**Lý do.** Khác seed list hay augment variant thì mọi so sánh chéo giữa hai track vô nghĩa, và không ai phát hiện ra cho tới lúc viết bài.

**Việc.** Tạo `config/shared.yaml`: seed `[0,1,2]`, augment variant 11, test split gốc (777 query / 3033 gallery), input 224×224, ρ mặc định 100 m, checkpoint naming.

**Đạt khi.** Cả `train.py` và `eval_metrics.py` load từ file này, không còn hằng số rải rác.

---

# KHẢI — Evaluation track

## K1 — `eval_metrics.py` ⚠ CRITICAL PATH · hết tuần 1

**Lý do.** Tiền đề của toàn bộ dự án. R@1 và SDM đã bão hòa thông tin trên DenseUAV, nên nếu chưa có metric mới thì mọi kết quả Thắng train ra đều không diễn giải được. Thắng bị block cho tới khi task này xong.

**Đầu vào.** `pytorch_result_1.mat`, `Dense_GPS_ALL.txt`.

**Việc.** Script nhận checkpoint path, trả về:
- `GFR@ρ` = P(err > ρ) + Wilson CI, ρ ∈ {50, 100, 200, 500}, mặc định 100
- `p50 / p90 / p95` + bootstrap CI (1000 resample)
- `MA@{50,100,200,500}`
- `GeoAUROC` — AUROC của margin (s₁ − s₂) khi detect {err > ρ}
- `R@1 / R@5 / SDM@1` để đối chiếu tài liệu
- Xuất `results.json` + `errors.npy` (sai số per-query, dùng lại ở K3)

**Đạt khi.**
1. Reproduce đúng `evaluateDistance.py` và `evaluateGPU.py` trên `baseline_vits_single`: R@1 = 82.20, p95 = 188.55, lệch < 0.01. Lệch thì bug ở code mới.
2. Chạy được cả 4 checkpoint sẵn có, không sửa gì.
3. GFR@100 tính tay trên 20 query ngẫu nhiên khớp với output.

**Nếu kẹt.** GeoAUROC dễ sai nhất (dấu của margin, xử lý tie). Giao bản không có GeoAUROC đúng hạn rồi bổ sung — Thắng cần GFR và p95 trước.

## K2 — Baseline table, 4 checkpoint sẵn có · tuần 2

**Lý do.** Quick win và bảo hiểm cho cả nhóm: kể cả model track thất bại hoàn toàn, vẫn còn một contribution đứng được. Không cần GPU vì `.mat` đã có sẵn.

**Việc.** Chạy K1 lên `baseline_vits_single`, `vits_lpn`, `vits_fsra`, `resnet50_single`. Vẽ CDF ở dải K > s (Hình 1 hiện tại chỉ có K ∈ [1,100]).

**Đạt khi.** Tìm được ít nhất một cặp checkpoint mà thứ hạng GFR@100 **khác** thứ hạng R@1. Nếu không có cặp nào, luận điểm "metric mới mang thông tin độc lập" yếu đi đáng kể — báo ngay cho cả nhóm, dù theo chiều nào đây cũng là kết quả quan trọng.

## K3 — Texture proxy + logistic regression · tuần 3

**Lý do.** Trả lời câu hỏi của thầy về địa hình mà không dính circular reasoning. Section 6.5(c) hiện mới mô tả định tính; task này biến nó thành hệ số có CI.

**Việc.**
- 3 proxy tính từ *riêng ảnh vệ tinh*, không đụng kết quả retrieval: Canny edge density, ExG = 2G − R − B, số ORB keypoint.
- Kiểm tra tương quan giữa 3 proxy, tương quan > 0.9 thì bỏ bớt.
- Fit `logit P(err > 100) ~ β₀ + β₁·texture + β₂·altitude`, altitude ∈ {80, 90, 100}.

**Đạt khi.** Báo cáo β₁ + CI 95% + p-value cho cả 3 proxy, có control altitude. Không có ý nghĩa thống kê cũng là kết quả hợp lệ, miễn CI đủ hẹp để phát biểu được điều đó.

**Lưu ý.** Không NDVI (không có kênh NIR). Không gán nhãn tay.

## K4 — SQCLoc checkpoint · tuần 2–4, chạy nền

**Lý do.** Bằng chứng mạnh nhất cho luận điểm: model R@1 ≈ 89–91% mà p95 vẫn hàng trăm mét. Checkpoint mạnh nhất nhóm đang có chỉ 82.88%, dải R@1 cao còn trống.

**Việc.** Xin hoặc tải checkpoint / `.mat` từ nhóm SQCLoc. Không reproduce trừ khi Thắng còn dư GPU slot.

**Đạt khi.** Có số, hoặc có ghi chép rõ là không tiếp cận được (để viết vào Limitations).

## K5 — FPI/OS-FPI loader · tuần 4 (task đệm)

**Lý do.** Con đường duy nhất verify được cải tiến sub-tile. `evaluate_RDS.py` đã có sẵn trong repo, viết đúng cho format `labels.json` của FPI.

**Đạt khi.** Đo được sai số theo mét thật (không tile-quantized) cho ít nhất 1 checkpoint.

**Nếu K1–K3 xong sớm** thì kéo task này lên tuần 3, hoặc chuyển sang implement spatial confidence gating (Section 8.1) — cũng là post-processing, không cần GPU.

---

# THẮNG — Model track

## T0 — Fallback eval script · ngày 1, 2 giờ

**Lý do.** Không ngồi chờ Khải. 20 dòng tính R@1 + p95 thô, đủ sanity-check training loop trong tuần 1.

**Đạt khi.** Chạy được, số gần đúng `evaluateDistance.py`. Bỏ đi khi K1 xong.

## T1 — Survey prior work ⚠ LÀM TRƯỚC KHI CODE · hết tuần 1

**Lý do.** Distance-weighted contrastive loss là ý tưởng tự nhiên, xác suất đã có prior work ở nhánh ground-to-aerial là thật. Biết ở tuần 1 tốn 3 ngày; biết ở tuần 4 mất 3 tuần và phải viết lại framing của cả paper.

**Từ khóa.** *geographically-aware contrastive loss*, *distance-weighted triplet*, *soft label geo-localization*, *metric learning with continuous labels*. Đọc kỹ nhánh VIGOR / ground-to-aerial.

**Đạt khi.** Trả lời dứt khoát: "ý tưởng này mới ở điểm nào" — hoặc "không mới, cần đổi hướng".

## T2 — Distance-dependent margin · tuần 2

**Lý do.** Contribution phương pháp duy nhất của kế hoạch, và là hệ quả trực tiếp của negative result ở Section 5.2: loss hiện tại phạt như nhau một negative cách 20 m và một negative cách 2 km, vì nhãn chỉ là class id rời rạc.

**Việc.** Trong `train.py`:

    m_an = m₀ · min(1, ‖g_a − g_n‖ / ρ)

g lấy từ `Dense_GPS_ALL.txt` theo class id. Không cần nhãn mới.

**Đạt khi.**
1. **Degenerate-limit check (bắt buộc):** ρ → 0 phải thu về đúng baseline loss, loss curve lệch < 1% so với run gốc. Không có kiểm tra này thì lúc T3 ra kết quả xấu sẽ không phân biệt được "ý tưởng sai" với "implement sai".
2. Log phân bố m_an theo epoch, xác nhận margin thật sự biến thiên chứ không collapse về hằng số.

## T3 — Ablation ρ và m₀ · tuần 3, ~6h GPU

**Lý do.** Cần biết kết quả có nhạy với hai tham số này không. Nhạy quá là điểm yếu phải báo cáo — đúng cách nhóm đã xử lý khảo sát (K, τ).

**Việc.** Grid ρ ∈ {50, 100, 200, 500} m × m₀ ∈ {0.3, 0.5}, 8 run, seed=0.

**Đạt khi.** Có bảng đầy đủ, không phải một điểm tham số may rủi. Nếu không cấu hình nào thắng baseline thì đó là negative result thứ hai — báo cáo trung thực kèm phân tích nguyên nhân, giống cách đã làm với centroid decoding.

## T4 — 3 seed cho cấu hình tốt nhất · tuần 3–4, ~4h GPU

**Lý do.** GFR@100 có Wilson CI ≈ ±1.2 điểm trên ~2331 query. Một seed không phân biệt được cải tiến thật với nhiễu — loại lỗi reviewer bắt ngay.

**Đạt khi.** Chênh lệch proposed vs baseline lớn hơn tổng CI hai bên. Nếu không, phát biểu là "không có bằng chứng cải thiện", không phải "cải thiện nhẹ".

## T5 — Ablation pretrain · tuần 4, ~4h GPU

**Lý do.** Hướng thầy đề xuất. Giả thuyết: pretrain tốt hơn có thể không đoán đúng thêm ô nào (R@1 đứng yên) nhưng *biết rõ hơn khi nào mình đang đoán bừa* — GeoAUROC tăng. Đó là cải thiện thật cho an toàn bay, và là điều kiện cần của spatial confidence gating.

**Việc.** So ImageNet-21k (hiện tại) với ít nhất một lựa chọn khác — DINOv2 hoặc backbone SSL trên ảnh vệ tinh. Giữ nguyên head, augment, batch size, schedule, và **tuyệt đối giữ nguyên decoding top-1 → tile center**.

**Đạt khi.** Chỉ đổi đúng một biến. Báo cáo cả trường hợp R@1 không đổi mà GeoAUROC đổi — đó là điều đáng quan tâm nhất.

---

# Lịch

| Tuần | Khải | Thắng | GPU |
|---|---|---|---|
| 1 | S0, **K1** | T0, **T1** | trống |
| 2 | K2, K4 (nền) | T2 | ~1h |
| 3 | K3 | T3, T4 | ~10h |
| 4 | K5 | T4 (nốt), T5 | ~4h |
| 5 | Viết Section 3–4–6 | Viết Method | dự phòng |

**Hai mốc không được trượt:** K1 và T1, cả hai hết tuần 1. Mọi task khác trượt 1 tuần vẫn không vỡ kế hoạch.

**Nếu T3 ra negative result:** không kéo dài. Chuyển sang phân tích nguyên nhân, dồn sức cho T5 và track của Khải. Nhóm đã có contribution đứng được từ K2–K3.

**Sync 15 phút mỗi thứ Hai.** Chỉ ba câu hỏi: tuần rồi xong gì, tuần này làm gì, đang bị chặn bởi ai.

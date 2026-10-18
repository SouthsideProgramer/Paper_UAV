# PLAN — Quy trình 6 tuần: từ tái lập baseline đến bản nháp paper

> Trạng thái cập nhật: 2026-09-29. Mỗi thí nghiệm phải có một dòng trong [`EXPERIMENT_LOG.md`](EXPERIMENT_LOG.md) **trước khi chạy**.
> Tổng hợp những gì đã làm trước kế hoạch này: [`ALL_doc.md`](ALL_doc.md).

## Ba nguyên tắc áp dụng suốt quá trình

1. **Chỉ thay đổi một yếu tố mỗi lần.** Baseline hỏng hiện nay khó truy vết chính vì nhiều thứ bị sửa cùng lúc: `test.py`, `tool/utils.py` và `SingleBranch.py` đều nằm trong một commit `bbfa61f`, cộng thêm hyper-parameter.
2. **Không tinh chỉnh trên tập test.** Hiện K, τ, ρ đang được chọn trực tiếp trên 2331 query test, tức là rò rỉ dữ liệu. Cách sửa: tách 1–2 trong 10 trường train làm **tập validation theo campus**. Mọi siêu tham số (ρ, m₀, K, τ, ngưỡng từ chối) chỉ được chọn trên tập này. Tập test chỉ chạy **một lần** ở cuối mỗi thí nghiệm.
3. **Viết giả thuyết và tiêu chí thành công trước khi chạy.** Mỗi thí nghiệm là một dòng trong `EXPERIMENT_LOG.md`, ví dụ: *"Giả thuyết: X tốt hơn Y về GFR@100. Thành công nếu CI bootstrap của hiệu số không chứa 0."*

## Lịch tổng quát

| Tuần | Giai đoạn | Thắng (GPU) | Khải (không GPU) | Cổng qua |
|---|---|---|---|---|
| 1 | 0. Tái lập baseline | Chạy lại code gốc | Kiểm tra pipeline eval | ViT-S R@1 ≥ 78% |
| 2 | 1. Chốt giao thức đánh giá | Train 4 mô hình × 3 seed | Gộp code eval, một nguồn số | Số khớp giữa mọi script |
| 2–3 | 2. Chẩn đoán lỗi (Cải tiến 3) | Hỗ trợ | Phân loại lỗi | Bảng taxonomy hoàn chỉnh |
| 3–4 | 3. Bất định & từ chối | — | Risk–coverage | Dispersion thắng margin có ý nghĩa |
| 3–5 | 4. Phương pháp (Cải tiến 1, 2) | Margin theo khoảng cách | Re-rank bằng descriptor | Cải thiện trên val, xác nhận trên test |
| 6 | 5. Viết paper | Bảng ablation | Hình, bảng chính | Bản nháp đầy đủ |

**Điểm dừng cần báo thầy sớm:** cuối tuần 1, dù baseline có tái lập được hay không.

---

## Giai đoạn 0 — Tái lập baseline (tuần 1)

**Mục tiêu:** tìm ra vì sao ViT-S chỉ đạt 19.26% trong khi nhóm từng đạt 82.20%. Bài gốc báo 83.01% theo `report.tex`; kế hoạch cũ ghi 80.18%, cần đối chiếu lại với bảng trong bài gốc.

### Những gì đã biết (kiểm tra 2026-09-29)

| Bằng chứng | Nguồn | Hệ quả |
|---|---|---|
| Nhóm **đã tái lập được** 82.20% (LPN 82.88, FSRA 80.74, ResNet-50 33.16) | `reports/report.tex:307, 326` — commit `cc3e3be`, máy `/home/internship/thang2/DenseUAV` | Code gốc + config trong `run_experiments.sh` là đủ để đạt cổng qua |
| `test.py`, `tool/utils.py`, `SingleBranch.py` bị sửa cùng lúc trong `bbfa61f` (15/09); mọi số 19–67% xuất hiện sau đó | `git log` | Nghi phạm số 1 |
| ResNet-50 **tăng** 33.16 → 41.36%, còn các ViT giảm | K2 `baseline_summary.json` | Một lỗi ở khâu test khó làm model tăng → nhiều khả năng các checkpoint mới là **lần train khác** |
| `.mat` 19.26% sinh trên **Windows** (path `datasets\DenseUAV\test\...`) | `diagnose_mat.py` trên `Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat` | Checkpoint này không phải checkpoint 82.20% trên máy Linux |
| `.mat` đó: feature đã L2-normalize, 777/777 query class có trong gallery, không có feature collapse (cos q–q trung bình 0.15), R@1 theo độ cao 17.6 / 18.8 / 21.4% | `diagnose_mat.py` | Khâu so khớp và nhãn không có lỗi; vấn đề nằm ở **feature**, tức checkpoint hoặc cách load |
| `requirements.txt` không pin phiên bản `timm` / `torch` | `requirements.txt` | Máy Windows có thể dùng timm khác → pretrained hoặc kiến trúc khác |

### Các bước chẩn đoán (theo thứ tự)

Công cụ nằm trong `diagnostics/`:

| Script | Cần torch? | Việc làm |
|---|---|---|
| `diagnose_mat.py` | Không | Kiểm tra L2-norm, nhãn, OS sinh file, R@1/R@5, R@1 theo độ cao, dấu hiệu collapse; so sánh nhiều `.mat` |
| `diagnose_checkpoint.py` | Có | Phiên bản môi trường, diff `opts.yaml`, pretrained có load không (norm và cosine ckpt↔pretrained), missing/unexpected keys, parse `train.log`, **R@1 trên một phần tập train** |
| `bisect_test_code.sh` | Có (GPU) | Chạy **cùng một checkpoint** qua 5 phiên bản code: gốc, HEAD, và HEAD với đúng một file revert về `b8de187` |

1. **Tìm lại checkpoint 82.20%** trên máy internship (`/home/internship/thang2/DenseUAV/checkpoints/baseline_vits_single`) và checkpoint 19.26% trên máy Windows.
2. **Bisect code test** trên checkpoint 82.20%:
   ```bash
   bash diagnostics/bisect_test_code.sh /home/internship/thang2/DenseUAV/checkpoints/baseline_vits_single \
        /home/internship/thang2/DenseUAV/test
   ```
   - A_orig ≈ B_head ≈ 82% → code test không có lỗi, sang bước 3.
   - B_head thấp → phiên bản nào trong C/D/E hồi phục lại thì file đó là thủ phạm.
   - Lưu ý: script ghi đè `inference_time.txt` trong thư mục checkpoint và ghi `results.txt` vào thư mục cha của `checkpoints/`.
3. **Chẩn đoán checkpoint 19.26%**, diff với opts của run 82.20%:
   ```bash
   python diagnostics/diagnose_checkpoint.py --ckpt_dir checkpoints/baseline_vits_single \
       --compare_opts <run_82>/opts.yaml --train_dir <DenseUAV>/train --n_classes 200
   ```
   Kiểm tra lần lượt: pretrained có được load không, loss có giảm không, đủ 120 epoch chưa, test có đúng chiều drone → satellite không (`--mode 1`), feature có L2-normalize không, thứ tự nhãn query/gallery.
   - R@1 trên train thấp → lỗi ở khâu huấn luyện hoặc load.
   - R@1 trên train cao mà test thấp → lỗi ở khâu test.
4. Nếu không còn checkpoint 82.20%: checkout `b8de187`, không sửa gì, train đúng config trong `train_test_local.sh`, rồi áp lại từng thay đổi một.
5. **Pin môi trường** của run đạt cổng (torch/torchvision/timm) vào `requirements.txt`.

**Cổng qua:** ViT-S R@1 ≥ 78%. Chưa đạt thì **dừng mọi phân tích khác**.

---

## Giai đoạn 1 — Chốt giao thức đánh giá (tuần 2)

**Mục tiêu:** một nguồn số duy nhất, tái lập được.

- **Gộp code eval** thành một package, ví dụ `uavgeo_eval/`: K1 `eval_metrics.py` cùng 8 script gap. Bỏ các bản sao trong `scripts/`, đưa mọi đường dẫn vào một file config. Hiện có nhiều đường dẫn hard-code: `/media/ml4u/...`, `/home/internship/...`.
- **Kiểm soát phiên bản kết quả:** mỗi `pytorch_result_*.mat` đi kèm checkpoint, seed, commit hash và sha256 của chính file (`diagnose_mat.py` đã in sha256). Mọi bảng trong paper phải sinh tự động từ các file này.
- **4 mô hình × 3 seed**, báo cáo trung bình ± độ lệch chuẩn. Lưu ý `train.py` đang cố định `set_seed(666)`, cần thêm tham số `--seed`.
- **Bootstrap theo campus** vì query trong cùng một trường không độc lập. ⚠ Tập test chỉ có **4 trường**, nên cluster bootstrap với 4 cụm cho CI rất rộng và không ổn định. Báo cáo cả hai kiểu (theo query và theo campus), hoặc thêm leave-one-campus-out.
- **Ghi rõ sai số là rời rạc:** GPS của drone chính là tâm tile, nên sai số chỉ nhận giá trị 0 hoặc ≥ ~20 m. Chỉ số chính là GFR@ρ và p90/p95. Nếu báo cáo p50 thì phải kèm chú thích này.
- **Thống nhất số liệu đang lệch:** GFR@100 của LPN là 17.12% ở K2 nhưng 19.13% ở Robustness task 2; R@1 baseline 19.26% ở K2 so với 82.20% ở report.
- **Tập validation theo campus:** gom cụm tọa độ trong `Dense_GPS_ALL.txt` để gán campus cho 2256 class train, rồi tách 1–2 trường. File này bị gitignore, nên đường dẫn phải lấy từ config.

Sau đó **chạy lại toàn bộ task gap** trên mô hình đã tái lập và ghi rõ luận điểm nào còn đứng vững, luận điểm nào mất. Đây là bước trung thực quan trọng nhất của cả quy trình.

**Cổng qua:** mọi script cho cùng một con số trên cùng một `.mat`.

---

## Giai đoạn 2 — Chẩn đoán lỗi, tức Cải tiến 3 (tuần 2–3)

Xếp mỗi query vào đúng một nhóm, với bước lưới s ≈ 19.71 m:

| Nhóm | Điều kiện |
|---|---|
| Đúng | 0 m |
| Lân cận | 1 bước lưới (≤ ~28 m, tính cả ô chéo) |
| Cục bộ | ≤ 100 m |
| Xa, cùng trường | intra-campus confusion |
| Khác trường, rơi vào trường test | inter-campus confusion |
| Khác trường, rơi vào trường train | dấu hiệu nhớ cảnh huấn luyện. Nhóm này hợp lệ vì gallery gồm 3033 lớp của cả 14 trường |

Cắt thêm bảng theo độ cao (80/90/100 m) và theo từng campus.

**Cặp mơ hồ (ambiguous pairs):** các cặp gallery–gallery có cosine cao nhưng cách xa về địa lý (d_geo ≫ 0 trong khi d_F nhỏ). Đếm mật độ theo từng trường, rồi kiểm tra: query rơi vào vùng nhiều cặp mơ hồ có sai nhiều hơn không? Nếu có, ta có giải thích nhân quả thay vì chỉ là thống kê mô tả.

**Cổng qua:** bảng taxonomy hoàn chỉnh.

---

## Giai đoạn 3 — Bất định và từ chối (tuần 3–4)

**Giả thuyết:** độ phân tán địa lý của Top-K dự báo lỗi lớn tốt hơn margin s₁−s₂.

Các score cần so sánh: margin s₁−s₂; s₁; đường kính Top-K; độ phân tán Top-K có trọng số theo similarity; tỷ lệ phần tử Top-K nằm trong bán kính ρ quanh top-1.

Công cụ đánh giá:
- **GeoAUROC.** Hiện margin chỉ đạt 52–57, gần như ngẫu nhiên, theo K2.
- **Đường risk–coverage:** GFR@100 thay đổi thế nào khi được từ chối 5% / 10% / 20% số query.

**Cổng qua:** hiệu số AUROC (dispersion − margin) có CI bootstrap không chứa 0. Nếu không đạt, vẫn báo cáo, và luận điểm chuyển thành *"bất định trong không gian embedding không dự báo được rủi ro địa lý"*.

---

## Giai đoạn 4 — Phương pháp, tức Cải tiến 1 và 2 (tuần 3–5, chạy song song)

**Thắng — margin phụ thuộc khoảng cách (Cải tiến 2).** Áp `m = m₀·min(1, d/ρ)` vào soft-weighted triplet. Ablation ρ ∈ {20, 50, 100, 200} × m₀. Chọn cấu hình trên **val theo campus**, xác nhận trên test với 3 seed. Theo dõi đồng thời R@1 và GFR@100/p95: kỳ vọng R@1 giữ nguyên hoặc giảm nhẹ, còn phần đuôi phân phối giảm. Bắt buộc kiểm tra giới hạn suy biến: ρ → 0 phải thu về đúng baseline loss.

**Khải — re-rank bằng descriptor tích phân (Cải tiến 1).** Bắt đầu từ bản rẻ nhất:
1. Histogram hoặc tỷ lệ diện tích của các proxy đã có (Canny, ExG, ORB, xem K3) trên **lưới vòng tròn đồng tâm**, để bất biến với phép quay.
2. Dùng descriptor để re-rank Top-K.
3. Chỉ khi bản rẻ cho tín hiệu tích cực mới đầu tư vào segmentation ngữ nghĩa.

Khoảng cách descriptor phải chuẩn hóa theo diện tích mặt đất (độ cao bay và tỷ lệ ảnh vệ tinh khác nhau).

**Cổng qua:** cải thiện trên val, xác nhận trên test.

---

## Giai đoạn 5 — Viết paper (tuần 6)

1. Vấn đề: R@1 và SDM không phản ánh rủi ro theo mét.
2. Giao thức đánh giá mới: GFR, p95, risk–coverage, kèm lưu ý về trần lượng tử hóa của lưới.
3. Chẩn đoán lỗi: bảng taxonomy và phân tích cặp mơ hồ.
4. Phương pháp: tín hiệu bất định, margin theo khoảng cách, re-rank.
5. Giới hạn: GPS theo lớp, chỉ một bộ dữ liệu, SQCLoc chưa có checkpoint công khai, chỉ 4 campus test.

**Chỉ đưa vào paper những số liệu sinh ra từ giao thức đã chốt ở Giai đoạn 1.**

---

## Hướng F — Định vị không GPS: fusion retrieval cross-view + IMU (từ 2026-10-01)

**Lý do:** các research gap cho thấy retrieval có lỗi đuôi nặng (p95 cỡ 3 km, khoảng 12 % query trôi sang campus khác) và độ tự tin sai (GeoAUROC ~0.55). Một prior chuyển động từ IMU/VIO loại được các bước nhảy vô lý về vật lý. Chi tiết khảo sát: [`Task_F_Fusion/survey/fusion_survey_notes.md`](Task_F_Fusion/survey/fusion_survey_notes.md).

**Điểm mới cần giữ** (vì "VIO + khớp ảnh vệ tinh" đã có: NaviLoc 2026, FoundLoc 2023, SWA-PF 2025):
hiệp phương sai đo lấy từ **độ phân tán Top-K**, **gating χ²** theo dự đoán chuyển động, đo **đa giả thuyết** Top-K (particle filter), đánh giá theo **lỗi đuôi** (GFR, p95, lỗi lớn nhất).

| Bước | Việc | Dữ liệu | Cổng qua |
|---|---|---|---|
| F1 | Khảo sát related work + dataset có IMU | — | Xong, xem survey notes |
| F2 | Prototype bán mô phỏng: quỹ đạo giả trên lưới DenseUAV, IMU/VIO giả, đo retrieval (mô hình tổng hợp hoặc `.mat` thật) → ESKF / PF | Tổng hợp + DenseUAV `.mat` + `Dense_GPS_ALL.txt` | Fusion + gating giảm p95 so với chỉ retrieval, CI không chứa 0 |
| F3 | Chạy F2 với `.mat` thật của LPN/FSRA trên server (cần GPS) | DenseUAV | Kết quả F2 lặp lại trên retrieval thật |
| F4 | Tải và kiểm tra dữ liệu thật: MAFS (có IMU không?), Nardo-Air, MARS-LVIG | Thật | Chọn được ≥ 1 dataset có IMU + chuỗi bay + ảnh vệ tinh |
| F5 | Pipeline trên dữ liệu thật, so với NaviLoc / FoundLoc / SWA-PF | Thật | Thắng hoặc ngang về mean, thắng rõ về p95 / lỗi lớn nhất |

**Phụ thuộc:** F3 trở đi cần checkpoint retrieval đã tái lập (Giai đoạn 0). F2 dùng mô hình lỗi tổng hợp nên làm được ngay.

**Điều chỉnh sau F4 (2026-10-01):** dữ liệu thật chính = **AerialVL**. Bước tiếp: (1) giải nén, đọc định dạng chuỗi và bản đồ; (2) cắt bản đồ thành tile gallery; (3) đo R@1 / Top-K zero-shot của 3 model DenseUAV trên ảnh AerialVL (rủi ro lệch miền → có thể fine-tune trên phần VPR); (4) chạy MH-EKF với IMU/VIO sinh từ GNSS; (5) khi có rosbag thì thay bằng IMU thật. Thêm **GeoVINS** (T-RO 2025) vào danh sách đối thủ.

**Điều chỉnh sau F3 (2026-10-01):** dữ liệu thật có aliasing dài, nhất quán theo vùng (campus "song sinh"); MH-EKF cần ràng buộc vùng tới được khi tìm lại vị trí. Vì thiết kế đã bị chỉnh theo test, **bắt buộc** làm val theo campus trước khi báo số. Dataset đầy đủ đang tải về `datasets/` (16.7 GB); máy có RTX 3050 8 GB để sinh `.mat`.

**Điều chỉnh sau F2-12 (2026-10-01):** phương pháp chính = **MH-EKF trên Top-K** (thay cho PF, vì PF hỏng khi chỉ có IMU). Đánh giá phải tách giai đoạn khởi tạo (30 s đầu) khỏi giai đoạn bám.

**Điều chỉnh sau F2 (2026-10-01):** "hiệp phương sai theo độ phân tán Top-K" bị bác bỏ trong dạng hiện tại → đóng góp chính chuyển sang **particle filter đo đa giả thuyết trên Top-K** + **đánh giá theo lỗi đuôi**. Việc tiếp theo cho F3: (1) đo trên `.mat` thật xem tile đúng có nằm trong Top-10 khi top-1 sai không (giả định 50 % của mô phỏng), (2) đo tương quan lỗi giữa các tile liền kề (giả định persist), (3) thêm PF cho IMU-only, (4) thử dùng dispersion cho gating thay vì phóng R.

---

## Theo dõi tiến độ

| Giai đoạn | Trạng thái | Ghi chú |
|---|---|---|
| 0 | ✅ Qua cổng (2026-10-01) | Đã có công cụ `diagnostics/`; đã kiểm tra `.mat` 19.26% (pipeline so khớp OK). 2026-10-01: checkpoint chính thức không tải được (OneDrive bị vô hiệu, Quark cần app, HF không có) → **train lại bằng code gốc `b8de187`** trên máy local (RTX 3050, worktree `../DenseUAV_b8de187`, E003); **baseline R@1 79.67 % → qua cổng**; LPN 86.36 %; FSRA 81.85 % (1 seed mỗi model), kết quả ở `../DenseUAV_b8de187/logs/stage0_summary.txt` |
| 1 | ⬜ Chưa bắt đầu | |
| 2 | ⬜ | |
| 3 | ⬜ | |
| 4 | ⬜ | |
| 5 | ⬜ | |
| F1 | ✅ Xong (2026-10-01) | Survey: NaviLoc là đối thủ gần nhất; dataset ứng viên MAFS, Nardo-Air, MARS-LVIG |
| F2 | ✅ Xong val (2026-10-01) | Gating χ² là yếu tố chính; PF Top-K tốt nhất ở kịch bản khó **khi có VIO**; PF + IMU thuần thất bại (F2-10); R theo dispersion và gating theo dispersion bị bác bỏ (F2-02, F2-11). Chưa chạy test (seed 1) |
| F3 | 🟡 Đang làm | GPS lấy từ HF. F3-01..03 trên `.mat` 19 %: MH-EKF (đã sửa) tốt nhất ở cả 4 kịch bản real. **Giao thức val/test (F3-04):** val = campus 9, 10, test = campus 11, 12 (`run_f2.py --campuses val/test`); thiết kế MH-EKF v2 chốt trên val. **F3-05 (test, ViT-S 79.67 %): MH-EKF tốt nhất ở cả 4 kịch bản, 0 % chuyến mất dấu sau 30 s.** F3-06 (LPN 86.36 %), F3-07 (FSRA 81.85 %) lặp lại kết luận: **MH-EKF tốt nhất ở cả 12 ô (3 model × 4 kịch bản) trên test**. **E006 + F3-08 xong (2026-10-02):** R@1 ổn định theo seed (std ≤ 1.2 điểm); MH-EKF thắng ekf_gated ở 108/108 ô (3 model × 3 seed model × 3 seed quỹ đạo × 4 kịch bản), mất dấu ≤ 0.2 % → ✅. **F3-09 (2026-10-05):** chạy lại 108 ô với MH-EKF v3 (`v_max = 0`): kết quả trùng v2 (lệch p95 ≤ 0.33 m), thắng gated 108/108 → **mọi bảng paper dùng MH-EKF v3** |
| F2b | ✅ Xong val (2026-10-01) | Thay RBPF bằng **multi-hypothesis EKF** (F2-12): tốt hoặc ngang tốt nhất ở mọi kịch bản, kể cả IMU thuần → **phương pháp chính đề xuất cho paper**. Còn lại: chạy test seed 1 khi cấu hình đã chốt |
| F4 | ✅ Xong (2026-10-02) | MAFS và Nardo-Air bản public không có IMU; chọn **AerialVL** (11 chuyến thật, GNSS, bản đồ vệ tinh). Đã tải `VAL` 54 GB; giải nén 5 chuyến ngắn; 6 chuyến dài xử lý từng chuyến (F5-05). IMU thật nằm trong rosbag GeoVINS trên Baidu (chưa có tài khoản) → IMU/VIO mô phỏng từ quỹ đạo GNSS thật |
| F5 | 🟡 Đang làm (2026-10-02) | `Task_F_Fusion/aerialvl/`. F5-00 hình học (ảnh hướng đông, footprint 200 m); F5-01 retrieval zero-shot LPN top-1 ≤ 50 m 36 %, p95 3.8 km; F5-02 val: MH-EKF v2 thua PF ở chuyến khó (nhảy alias) → F5-03 **MH-EKF v3** (tìm lại trong 3σ), trùng v2 trên DenseUAV val. **F5-04 test (3 chuyến, xong):** MH-EKF v3 thắng gated 36/36, thắng PF 33/36 (thua < 1 m ở VIO); p95 VIO 37–41 m, IMU 56–72 m (PF 591–680), xuất phát sai 43–244 m (PF ~600) so với retrieval đơn thuần ~3.8 km. **F5-05 (5 chuyến dài, xong):** MH-EKF vẫn tốt nhất (p95 thấp nhất 12/12 ô), nhưng chỉ VIO cho kết quả dùng được (p95 ~50 m); chỉ IMU / xuất phát sai mất dấu 17–55 % cửa sổ → nút thắt là retrieval zero-shot. Hướng tiếp: fine-tune retrieval trên phần VPR của AerialVL (tránh trùng chuyến bay test), IMU thật (Baidu), so sánh đối thủ. **F6 (2026-10-06): đã so với NaviLoc** (cài lại, `prototype/naviloc.py`): MH-EKF thắng cả 3 biến thể NaviLoc ở 180/180 ô (AerialVL ngắn, dài, DenseUAV); NaviLoc vỡ khi > 50 % top-1 sai và khi chỉ có IMU. Chưa so với FoundLoc / SWA-PF / GeoVINS. **F7 (2026-10-08): fine-tune retrieval** trên 2 chuyến 03-16 (val 03-11): retrieval test gần gấp đôi (LPN top-1 ≤ 50 m chuyến dài 0.29 → 0.60); mất dấu của MH-EKF trên chuyến dài giảm (xuất phát sai 17–19 → 4–7 %, chỉ IMU 43–55 → 28–35 %); ở kịch bản dễ NaviLoc/PF ngang MH-EKF. Fine-tune cùng vùng bản đồ với test → nêu là giới hạn. **F5-06 (2026-10-05):** so với VIO/IMU đơn thuần (dead reckoning), MH-EKF giảm p95 khoảng 2× khi có VIO (dài 95 → 50 m), có ý nghĩa 22/24 ô (CI theo chuyến bay); EKF gated còn tệ hơn VIO đơn thuần ở chuyến dài; xuất phát sai trên chuyến dài chỉ thắng sau 60 s |

# ALL_doc — Tổng hợp những gì nhóm đã làm thêm trên DenseUAV

Repo này fork từ [Dmmm1997/DenseUAV](https://github.com/Dmmm1997/DenseUAV) (commit gốc cuối cùng: `b8de187`, 2025-12-12).
Tài liệu này liệt kê **mọi thứ nhóm đã thêm/sửa sau commit đó** (từ `cc3e3be` đến `2a15c2c`, 03/09 → 21/09/2026).

Kế hoạch tiếp theo: [`PLAN.md`](PLAN.md) · nhật ký thí nghiệm: [`EXPERIMENT_LOG.md`](EXPERIMENT_LOG.md) · công cụ chẩn đoán Giai đoạn 0: `diagnostics/`.

Luận điểm xuyên suốt: **Recall@1 và SDM không phản ánh độ an toàn định vị theo mét của UAV.** Nhóm xây một bộ đánh giá theo mét (GFR, p50/p90/p95, GeoAUROC, CDF), rồi dùng nó để chứng minh các research gap.

---

## 0. Tổng quan thay đổi

| Nhóm | File / thư mục | Loại |
|---|---|---|
| Kế hoạch & vận hành | `split_task.md`, `Running_On_Server.md`, `run_experiments.sh` | Thêm mới |
| Báo cáo | `reports/` (report EN/VI, manual, báo cáo 2 research gap .docx/.pdf) | Thêm mới |
| Hình | `docs/images/fig1_cdf*.{png,pdf}`, `docs/images/texture_odds_ratios.png` | Thêm mới |
| Code gốc bị sửa | `test.py`, `tool/utils.py`, `models/Head/SingleBranch.py`, `.gitignore` | Sửa |
| Sắp xếp lại | Script eval ở root → `tests/` ; `requirments.txt` → `requirements.txt` | Di chuyển |
| Evaluation track (K1–K5) | `Task_K_Gap_Recall@1/` | Thêm mới |
| Research Gap Robustness | `Task_K_Gap_Robustness/` (task1–4) | Thêm mới |
| Research Gap Spatial Mismatch | `Task_K_Gap_Spatial_Mismatch/` (task1–4) | Thêm mới |
| Hướng mới: fusion camera + IMU | `Task_F_Fusion/` (F1 survey, F2 prototype) | Thêm mới (2026-10-01) |

Lịch sử commit liên quan:

| Commit | Ngày | Tác giả | Nội dung |
|---|---|---|---|
| `cc3e3be` | 2026-09-03 | SouthsideProgramer | Metre-level evaluation, grid-free (weighted centroid) decoding, report/manual LaTeX, `run_experiments.sh` |
| `8319f05` | 2026-09-11 | Cocobaut | Dọn cấu trúc: chuyển script eval vào `tests/`, thêm `phan_task_khai_thang.md` |
| `bbfa61f` | 2026-09-15 | Cocobaut | Thêm `Task_K/` (K1–K5) + kết quả |
| `66d1641` | 2026-09-17 | Cocobaut | Cập nhật K2 (CDF, baseline eval) |
| `2febcee` | 2026-09-20 | baotram153 | `Running_On_Server.md`, đổi tên kế hoạch → `split_task.md` |
| `61c9998` | 2026-09-21 | baotram153 | Đổi `Task_K` → `Task_K_Gap_Recall@1`, thêm 2 research gap (Robustness, Spatial Mismatch) |
| `f931d70`, `b3e61de` | 2026-09-21 | baotram153 | Sửa README, thêm báo cáo research gap (.docx/.pdf) |

---

## 1. Kế hoạch & vận hành

### `split_task.md` — Phân task Khải & Thắng
- **Thắng — model track** (độc quyền GPU): T0 fallback eval, T1 survey prior work, T2 distance-dependent margin `m_an = m₀·min(1, ‖g_a − g_n‖/ρ)`, T3 ablation ρ × m₀, T4 chạy 3 seed, T5 ablation pretrain (ImageNet-21k vs DINOv2/SSL).
- **Khải — evaluation track** (không cần GPU): K1 `eval_metrics.py`, K2 bảng baseline, K3 texture + logistic regression, K4 SQCLoc, K5 FPI loader / spatial confidence gating.
- Interface duy nhất giữa hai track: file `pytorch_result_1.mat` (format gốc của repo).
- Lịch 5 tuần; hai mốc không được trượt: K1 và T1.

### `Running_On_Server.md`
Hướng dẫn chạy trên server ML4U: `cd "/media/ml4u/Extreme SSD/Paper-UAV"`, `conda activate safe-gs`, kiểm tra `nvidia-smi` trước khi chạy, **mọi checkpoint/dataset/cache phải lưu trên `Extreme SSD`**, không lưu vào ổ hệ thống.

### `run_experiments.sh`
Train + test + eval tuần tự 4 cấu hình (`baseline_vits_single`, `vits_lpn`, `vits_fsra`, `resnet50_single`) với cùng hyper-parameter (224×224, batch 16, lr 0.01, `WeightedSoftTripletLoss`, `KLLoss`). Đường dẫn đang hard-code cho máy `/home/internship/thang2/DenseUAV`.

---

## 2. Sửa code gốc

### `test.py` — viết lại
- Bọc vào `main()`, thêm `get_parse()` với default mới (`--name baseline_vits_single`, `--h/--w 224`, `--batchsize 64`).
- `resolve_paths()`: tự tìm thư mục checkpoint và `test_dir` (`datasets/DenseUAV/test`, …), load `opts.yaml` từ checkpoint nhưng **giữ lại** các override CLI (batchsize, test_dir, gpu_ids, mode…).
- Chạy được trên **CPU** (`--gpu_ids -1`).
- Tích hợp luôn đánh giá retrieval (`compute_mAP`, `evaluate_retrieval`): in và ghi `results.txt` gồm R@1, R@5, R@10, R@top1%, mAP.
- Vẫn xuất `pytorch_result_{mode}.mat` như cũ → tương thích mọi script eval.

### `tool/utils.py`
- `copyfiles2checkpoints`: không còn copy toàn bộ source vào checkpoint, chỉ lưu `opts.yaml`; `copytree` bỏ qua ảnh/dataset/.mat/.npy.
- `load_network`: tự dò đường dẫn checkpoint, `map_location` CPU/GPU.

### `models/Head/SingleBranch.py`
Hỗ trợ feature CNN 4 chiều `[B, C, H, W]` (adaptive avg/max pool) bên cạnh token Transformer `[B, N, D]` → **ResNet-50 dùng được SingleBranch head**.

### `.gitignore`
Bỏ qua `test/`, `train/`, `Dense_GPS_*.txt` (theo `docs/Request.md`, annotation DenseUAV **không được public**), `task_khai.txt`.

### `tests/` — tổ chức lại các script eval của repo gốc
```
tests/
├── retrieval/evaluate_gpu.py            # CMC, R@K, mAP
├── distance/evaluateDistance*.py        # SDM, theo độ cao
├── distance/evaluateMA*.py              # MA@K
├── continuous/evaluate_RDS.py           # RDS cho FPI/SiamUAV
└── experimental/eval_weighted_centroid.py, heatmap.py
```

---

## 3. Báo cáo — `reports/`

| File | Nội dung |
|---|---|
| `report.tex/.pdf` (EN), `report_vi.tex/.pdf` (VI) | Paper draft: **Quantisation Ceiling** (bước lưới gallery s ≈ 19.71 m → sàn median ≈ 7.86 m), metre-level protocol (median/p90/p95 + CDF), grid-free weighted-centroid decoder — sweep (K, τ) cho thấy **không cấu hình nào thắng top-1** vì láng giềng trong feature space không phải láng giềng địa lý. |
| `manual.tex/.pdf` | Hướng dẫn tiếng Việt: kiểm tra môi trường, train, eval, vẽ Hình 1, chạy weighted centroid, biên dịch báo cáo, bảng lỗi thường gặp. |
| `Báo cáo kết quả chứng minh tính đúng đắn 2 loại research gap.{docx,pdf}` | Báo cáo tổng hợp kết quả của `Task_K_Gap_Robustness` và `Task_K_Gap_Spatial_Mismatch`. |

---

## 4. `Task_K_Gap_Recall@1/` — Evaluation track (K1–K5)

### K1 — `eval_metrics.py`
Nhận `pytorch_result_1.mat`, tính: **GFR@ρ** = P(err > ρ) + Wilson CI (ρ ∈ {50,100,200,500}), **p50/p90/p95** + bootstrap CI (1000 resample), **MA@ρ**, **GeoAUROC** (AUROC của margin s₁−s₂ khi phát hiện err > ρ), và R@1/R@5/SDM@1 để đối chiếu. Xuất `results.json` + `errors.npy`.

```bash
python Task_K_Gap_Recall@1/Task_K1/eval_metrics.py --result_mat checkpoints/baseline_vits_single/pytorch_result_1.mat
```

### K2 — Bảng 4 baseline + CDF (`run_baseline_eval.py`, `plot_fig1_cdf.py`)

| Model | R@1 (%) | SDM@1 (%) | GFR@100 (%) | p50 (m) | p95 (m) | GeoAUROC |
|---|---|---|---|---|---|---|
| baseline_vits_single | 19.26 | 23.53 | 63.02 | 751.1 | 4757.7 | 52.12 |
| resnet50_single | 41.36 | 48.33 | 33.50 | 20.1 | 3756.6 | 52.82 |
| vits_fsra | 64.48 | 68.51 | 19.05 | 0.0 | 3557.2 | 56.53 |
| vits_lpn | 67.22 | 71.04 | 17.12 | 0.0 | 3220.8 | 56.55 |

→ Ngay cả model R@1 cao nhất vẫn có p95 > 3.2 km; GeoAUROC chỉ ~52–57 (margin gần như không dự báo được lỗi lớn). Hình CDF: `Task_K2/fig1_cdf{,_vi}.png`.

### K3 — Texture proxy + logistic regression (`texture_analysis.py`)
3 proxy tính **chỉ từ ảnh vệ tinh**: Canny edge density, ExG = 2G−R−B, số ORB keypoint (tương quan Spearman lớn nhất 0.69 → giữ cả 3). Fit `logit P(err > 100) ~ texture + altitude`.
- Baseline: cả 3 proxy có ý nghĩa (p < 0.001; texture nhiều cạnh/keypoint → ít lỗi hơn, ExG cao → nhiều lỗi hơn).
- FSRA / ResNet-50: `orb_count` có ý nghĩa (β < 0); LPN: chỉ `canny_density` (p = 0.03).
- Hình odds ratio: `docs/images/texture_odds_ratios.png`.

### K4 — SQCLoc (`sqcloc_survey_notes.md`)
Chưa có checkpoint công khai → ghi vào Limitations kèm đoạn văn mẫu cho paper.

### K5 — FPI loader + Spatial Confidence Gating
`fpi_loader.py` (loader cho FPI/OS-FPI), `spatial_confidence_gating.py`: so sánh top-1, centroid không ràng buộc và centroid có gating theo bán kính ρ.
- Centroid không ràng buộc **làm tệ đi** GFR@100 (LPN: 17.12 → 27.11 / 37.84 / 51.27 % với K = 3/5/10).
- Gating giữ GFR@100 gần như bằng top-1 (LPN tốt nhất 16.95 % ở K5/K10, ρ=100) — không làm hại nhưng cải thiện không đáng kể.

---

## 5. `Task_K_Gap_Robustness/` — Research Gap: Altitude Degradation & Tail Risk

4 model (Baseline ViT-S, FSRA, LPN, ResNet-50), 2331 query. Mỗi task có thư mục riêng `taskN/` (script + README + `results/`), đồng thời bản gộp ở `scripts/` và `results/`.

| Task | Script | Kết quả chính |
|---|---|---|
| 1. Phân tầng theo độ cao 80/90/100 m | `task1_altitude_stratification.py` | R@1 dao động 3–4 điểm giữa các độ cao, nhưng FailMean luôn 1.6–2.1 km và p95 luôn 3.2–3.7 km ở mọi độ cao. |
| 2. Tail risk & Median blindness | `task2_tail_risk_metrics.py` | FSRA/LPN có **median = 0 m** nhưng p95 = 3557 / 3221 m; 11.7–12.7 % query trôi > 1 km. |
| 3. SDM saturation | `task3_sdm_saturation_proof.py` | Với s = 5000, bán rã SDM ≈ 14.35 m; từ 200 m trở đi SDM ≈ 0. 97.49 % lỗi > 50 m của FSRA có SDM = 0.0000. Hình: `sdm_loss_sensitivity_curve.png`. |
| 4. Cross-campus drift | `task4_cross_campus_drift.py` | FSRA 295 ca (12.66 %), LPN 273 ca (11.71 %) trôi > 1 km, tối đa 5375 m, cosine s₁ lên tới 0.81–0.82. 20 cặp ảnh minh họa trong `task4/results/visual_pairs/`. |

---

## 6. `Task_K_Gap_Spatial_Mismatch/` — Research Gap: Visual similarity ≠ Spatial proximity

Chủ yếu trên Baseline ViT-S (`data/pytorch_result.mat`), đối chứng FSRA và ResNet-50.

| Task | Script | Kết quả chính |
|---|---|---|
| 1. Rank thị giác vs khoảng cách | `task1_spearman_correlation.py` | Spearman Top-5 trung bình chỉ +0.097 (Baseline), +0.184 (ResNet-50), +0.254 (FSRA); 90 % query Baseline có cặp bị đảo thứ tự địa lý. |
| 2. Độ phân tán Top-K | `task2_topk_dispersion.py` | Đường kính Top-5 trung bình 1806 m; 62 % cụm Top-5 (85 % cụm Top-10) trải rộng > 1 km. |
| 3. Naive weighted centroid | `task3_naive_centroid_crash.py` | Baseline: median 751 → 1125 m (K=5, τ=1), 55 % query tệ đi. FSRA: median 0 → 30 m, 74 % query tệ đi. |
| 4. Lỗi tự tin cao | `task4_high_conf_failures.py` | 79 query (3.39 %) có s₁ ≥ 0.70 nhưng sai ≥ 200 m; 55 query (2.36 %) sai ≥ 1 km, ví dụ s₁ = 0.77 mà sai 5.43 km. |

---

## 7. `Task_F_Fusion/` — Hướng mới: định vị không GPS bằng fusion camera + IMU (từ 2026-10-01)

Ý tưởng: dùng retrieval drone → vệ tinh đã có làm **phép đo vị trí tuyệt đối**, kết hợp với IMU/VIO làm **prior chuyển động** trong một bộ lọc, để loại các lỗi đuôi mà hai research gap đã chứng minh. Kế hoạch: mục *Hướng F* trong [`PLAN.md`](PLAN.md).

### F1 — Khảo sát (`survey/fusion_survey_notes.md`)
- Đối thủ gần nhất: **NaviLoc** (Drones, 01/2026): VPR + VIO tối ưu theo cả quỹ đạo, MLE 19.5 m. Ngoài ra có FoundLoc (2023) và **SWA-PF** (2025, cùng nhóm tác giả DenseUAV, particle filter + bản đồ ngữ nghĩa).
- DenseUAV **không có IMU và không có chuỗi bay** → chỉ dùng cho bán mô phỏng.
- Dataset thật ứng viên: **MAFS** (SWA-PF, video 30 fps trên 14 campus, cần kiểm tra phần public có IMU không), **Nardo-Air** (FoundLoc, có IMU), **MARS-LVIG** (có IMU + RTK nhưng không kèm ảnh vệ tinh). AerialVL không có IMU.
- Điểm mới đề xuất: hiệp phương sai đo từ độ phân tán Top-K, gating χ², đo đa giả thuyết, đánh giá theo lỗi đuôi.

### F2 — Prototype bán mô phỏng (`prototype/`, chi tiết trong `prototype/README.md`)
Mô phỏng 14 campus theo lưới DenseUAV, quỹ đạo bay 4–8 m/s, IMU 100 Hz / VIO 10 Hz (trôi ~1.2 % quãng đường), retrieval Top-10 tổng hợp hiệu chỉnh theo K2 (FSRA, LPN, baseline 19 %, giả định 82 %). So sánh 7 phương pháp: chỉ retrieval, chỉ VIO/IMU, EKF naive / gated / dispersion-R / Top-K NN, particle filter trên Top-K. Kết quả val, p95 với FSRA + VIO: **retrieval 3416 m → EKF gated 8.3 m → PF 7.5 m**; chỉ IMU consumer: 1187 m → 18 m. Đề xuất "R theo độ phân tán Top-K" **thất bại** (tệ hơn R cố định). PF trên Top-K tốt nhất ở các kịch bản khó (retrieval yếu 49 → 11 m, aliasing kéo dài 17 → 9 m, xuất phát sai 300 m 42 → 18.5 m). Nhật ký: F2-01…F2-09 trong `EXPERIMENT_LOG.md`. ⚠ Retrieval tổng hợp; phải xác nhận bằng `.mat` thật (F3).

Bổ sung (F2-10, F2-11, F3-00): PF với IMU thuần (không VIO) **thất bại** (p95 182 m so với EKF gated 18 m) → cần Rao-Blackwellized PF. Bỏ phép đo theo độ phân tán Top-K chỉ có lợi khi retrieval yếu. Trên `.mat` thật (model 19 %), tile đúng nằm trong Top-10 ở 45.5 % trường hợp top-1 sai, khớp giả định của mô phỏng. Đã kiểm tra chế độ `--world real` bằng file GPS giả; script server: `prototype/run_f3_server.sh`.

**F2-12 — Multi-hypothesis EKF (`mh_ekf`), ứng viên chính:** ≤ 10 EKF song song, sinh từ các ứng viên Top-K. Không bao giờ tệ hơn EKF gated, và tốt hơn rõ ở các kịch bản khó. p95: xuất phát sai 300 m 41.7 → 8.7 m; retrieval yếu 49.3 → 13.6 m; chỉ IMU + xuất phát sai 34.8 → 16.6 m. Sau 30 s đầu không còn chuyến bay nào lệch > 100 m (EKF gated: 10–12 %).

### F3 — Top-K thật với GPS thật
`Dense_GPS_ALL.txt` có sẵn trong zip HuggingFace `Dmmm997/DenseUAV` (đã tải về `datasets/DenseUAV/`, bị gitignore). Trên `.mat` baseline 19 %: 54.6 % top-1 rơi sang campus khác, có đoạn > 20 s liền cả Top-10 ở một campus "song sinh". Dữ liệu thật lộ ra 2 lỗi của MH-EKF mà mô phỏng không bắt được; đã sửa (điều kiện mất dấu + re-acquisition giới hạn theo vùng tới được). Sau khi sửa, p95: VIO 14.2 m (gated 66.9, retrieval 4437), chỉ IMU 35.4 m (gated 172), xuất phát sai 300 m 32 m (gated 1284). ⚠ Sửa sau khi xem test → mang tính khám phá; cần val theo campus.

**Giao thức val/test (F3-04):** 4 campus test của DenseUAV chia đôi theo thứ tự nhãn: val = campus 9, 10 (nhãn 2256–2632), test = campus 11, 12 (nhãn 2633–3032); model retrieval chưa thấy campus nào trong số này. Ablation trên val xác nhận cả 2 lần sửa MH-EKF (sau 30 s, % chuyến > 500 m: v0 11–17 % → v2 0–4 %) → chốt v2.

### Dữ liệu & môi trường local (2026-10-01)
- Dataset đầy đủ tải từ HF `Dmmm997/DenseUAV` (16.7 GB, public) → `datasets/DenseUAV/` (gitignore). Số ảnh khớp README.
- Checkpoint chính thức không còn tải được (link OneDrive bị vô hiệu, Quark cần app) → train lại.
- Env train: venv `~/.venvs/denseuav` (dựa trên env conda `libero`: torch 2.2.0+cu121, timm 0.9.10, + `pytorch-metric-learning` 2.9.0). GPU RTX 3050 8 GB; 1 epoch ViT-S ≈ 19 s.
- Code gốc ở worktree `../DenseUAV_b8de187` (commit gốc, không sửa).
- **Giai đoạn 0 qua cổng (E003):** ViT-S baseline train lại bằng code gốc đạt **R@1 79.67 %** (R@5 93.26, AP 68.50) → `.mat` 19.26 % cũ là checkpoint hỏng.

### F3-05 — Kết quả test đầu tiên (ViT-S 79.67 %, campus test 11, 12)
p95: VIO — retrieval 1306 m, EKF gated 7.7 m, **MH-EKF 6.4 m**; chỉ IMU — gated 13.1, **MH-EKF 11.3**; xuất phát sai 300 m — gated 682, PF 13.4, **MH-EKF 6.4**; IMU + xuất phát sai — gated 681, PF 618, **MH-EKF 11.4**. MH-EKF là phương pháp duy nhất không có chuyến bay nào lệch > 100 m sau 30 s đầu ở cả 4 kịch bản.

**LPN tái lập (E004): R@1 86.36 %.** F3-06 (test, LPN): p95 MH-EKF 6.2–10.9 m ở cả 4 kịch bản, 0 % chuyến mất dấu; EKF gated 6.6–16.2 m nhưng mất dấu 3 % chuyến khi xuất phát sai.

**FSRA tái lập (E005): R@1 81.85 %.** F3-07 (test, FSRA) lặp lại kết luận.

#### Tổng hợp test (campus 11, 12): 3 model retrieval tái lập × 4 kịch bản

p95 (m) của **MH-EKF** / EKF gated / chỉ retrieval; trong ngoặc là % chuyến bay mất dấu (> 100 m sau 30 s) của MH-EKF / EKF gated.

| Model (R@1) | VIO | Chỉ IMU | Xuất phát sai 300 m | IMU + xuất phát sai |
|---|---|---|---|---|
| ViT-S (79.67 %) | **6.4** / 7.7 / 1306 (0 / 0) | **11.3** / 13.1 / 1306 (0 / 0) | **6.4** / 682 / 1306 (0 / 6) | **11.4** / 681 / 1306 (0 / 7) |
| FSRA (81.85 %) | **6.8** / 7.8 / 78.7 (0 / 0) | **11.8** / 13.5 / 78.7 (0 / 0) | **6.9** / 8.5 / 78.7 (0 / 1) | **12.0** / 14.7 / 78.7 (0 / 1) |
| LPN (86.36 %) | **6.2** / 6.6 / 77.9 (0 / 0) | **10.8** / 11.6 / 77.9 (0 / 0) | **6.3** / 8.5 / 77.9 (0 / 3) | **10.9** / 16.2 / 77.9 (0 / 3) |

MH-EKF − EKF gated (p95) có CI 95 % không chứa 0 ở cả 12 ô.


---

### F4 — Kiểm tra dữ liệu thật (2026-10-01)

- Kết quả kiểm tra từng dataset: `Task_F_Fusion/survey/fusion_survey_notes.md` mục 2b. MAFS và Nardo-Air bản public không có IMU; MARS-LVIG có IMU nhưng không có ảnh vệ tinh.
- Chọn **AerialVL** (HF `hmf21/AerialVL`, MIT): 11 chuỗi bay, ảnh tên `@UTC@lon@lat@.png`, 2 bản đồ vệ tinh căn bắc. Script tải: `datasets/AerialVL/download_val.sh` (dùng `wget -c`, chạy lại sẽ tải tiếp phần còn thiếu; log ở `download.log`).
- Đối thủ mới cần đọc: **GeoVINS** (T-RO 2025), cùng nhóm tác giả AerialVL.

### F5 — Fusion trên chuyến bay thật AerialVL (`Task_F_Fusion/aerialvl/`, 2026-10-02)

- Ảnh, quỹ đạo GNSS, bản đồ và retrieval là thật; IMU/VIO mô phỏng từ quỹ đạo thật. Chi tiết và giao thức val/test theo ngày bay: `Task_F_Fusion/aerialvl/README.md`.
- Phát hiện: retrieval DenseUAV zero-shot vẫn có ích nhưng đuôi rất nặng; lệch camera ~23 m (hiệu chỉnh trên val); aliasing kéo dài tới 79 s → sửa luật tìm lại vị trí thành **MH-EKF v3** (chỉ trong 3σ), chốt trước khi chạy test.
- E006 / F3-08 (độ vững theo seed trên DenseUAV) đã xong: bảng `Task_F_Fusion/prototype/results/F3-08_summary.md`.

## 8. Lưu ý khi dùng lại

- **Dữ liệu không có trong repo:** `Dense_GPS_ALL.txt` bị gitignore (không được public); `Task_K_Gap_Robustness/data/` chỉ có `test_query_list.txt`, thiếu 4 file `pytorch_result_*.mat` mà README nhắc tới → phải tự sinh bằng `test.py`. `Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat` (~43 MB) thì có commit.
- **Đường dẫn hard-code:** README và script dùng `/media/ml4u/Extreme SSD/...` và `/home/ml4u/conda_envs/uav_env/bin/python`; `run_experiments.sh` dùng `/home/internship/...`. Script có cơ chế tìm file dự phòng (thư mục hiện tại, thư mục cha, `data/`, `checkpoints/`) vì exFAT không hỗ trợ symlink.
- **README cũ chưa cập nhật tên:** `Task_K_Gap_Recall@1/README.md` vẫn ghi đường dẫn `Task_K/...` (thư mục đã đổi tên). README Robustness ghi ảnh `drift_case_001.png`, còn file thật là `drift_rankXX_errYYYYm_simZZ.jpg`.
- **Script bị trùng:** mỗi script ở `scripts/` là bản sao của `taskN/`; sửa một chỗ thì nhớ sửa chỗ kia.
- **Số liệu lệch nhẹ giữa các nơi:** ví dụ GFR@100 của LPN là 17.12 % (K2) và 19.13 % (Robustness task 2); R@1 baseline trong K2 là 19.26 %, còn trong `report.tex` dải R@1 là 33–83 % (bộ checkpoint khác). Khi viết paper cần thống nhất lại nguồn số.

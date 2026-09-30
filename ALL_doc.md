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

## 7. Lưu ý khi dùng lại

- **Dữ liệu không có trong repo:** `Dense_GPS_ALL.txt` bị gitignore (không được public); `Task_K_Gap_Robustness/data/` chỉ có `test_query_list.txt`, thiếu 4 file `pytorch_result_*.mat` mà README nhắc tới → phải tự sinh bằng `test.py`. `Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat` (~43 MB) thì có commit.
- **Đường dẫn hard-code:** README và script dùng `/media/ml4u/Extreme SSD/...` và `/home/ml4u/conda_envs/uav_env/bin/python`; `run_experiments.sh` dùng `/home/internship/...`. Script có cơ chế tìm file dự phòng (thư mục hiện tại, thư mục cha, `data/`, `checkpoints/`) vì exFAT không hỗ trợ symlink.
- **README cũ chưa cập nhật tên:** `Task_K_Gap_Recall@1/README.md` vẫn ghi đường dẫn `Task_K/...` (thư mục đã đổi tên). README Robustness ghi ảnh `drift_case_001.png`, còn file thật là `drift_rankXX_errYYYYm_simZZ.jpg`.
- **Script bị trùng:** mỗi script ở `scripts/` là bản sao của `taskN/`; sửa một chỗ thì nhớ sửa chỗ kia.
- **Số liệu lệch nhẹ giữa các nơi:** ví dụ GFR@100 của LPN là 17.12 % (K2) và 19.13 % (Robustness task 2); R@1 baseline trong K2 là 19.26 %, còn trong `report.tex` dải R@1 là 33–83 % (bộ checkpoint khác). Khi viết paper cần thống nhất lại nguồn số.

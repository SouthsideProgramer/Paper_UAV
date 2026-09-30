# EXPERIMENT_LOG

Quy tắc (xem [`PLAN.md`](PLAN.md)):
- Ghi dòng **trước khi chạy**; chỉ điền cột Kết quả / Kết luận sau khi chạy.
- Mỗi thí nghiệm chỉ đổi **một** yếu tố so với thí nghiệm tham chiếu.
- Siêu tham số chọn trên **val theo campus**; test chỉ chạy một lần, ghi "test" ở cột Tập.

| ID | Ngày | Người | Giai đoạn | Giả thuyết | Tiêu chí thành công | Đổi yếu tố gì (so với ID) | Tập | Commit / ckpt / sha256 .mat | Kết quả | Kết luận |
|---|---|---|---|---|---|---|---|---|---|---|
| E000 | 2026-09-29 | — | 0 | `.mat` baseline 19.26% có lỗi ở khâu so khớp (chưa normalize / lệch nhãn) | `diagnose_mat.py` báo WARN | — | test | `Task_K_Gap_Spatial_Mismatch/data/pytorch_result.mat`, sha256 `62ffe21c3ec26423` | L2-norm OK, 777/777 class khớp, không collapse, R@1 = 19.26%, file sinh trên Windows | **Bác bỏ.** Lỗi nằm ở feature (checkpoint / load), không ở khâu so khớp |
| E001 | | | 0 | Code test ở `bbfa61f` làm giảm R@1 của checkpoint 82.20% | A_orig − B_head > 2 điểm R@1 | test code: A vs B vs C/D/E | test | | | |
| E002 | | | 0 | Checkpoint 19.26% được train khác run 82.20% (pretrained / epoch / opts) | `diagnose_checkpoint.py` báo diff opts, WARN pretrained, hoặc R@1 train thấp | — | train subset | | | |
# Run-On-Server

Hướng dẫn thiết lập và chạy mã nguồn trên Server.

---

## 🚀 Các bước thực hiện

### Bước 1: Di chuyển vào thư mục làm việc
```bash
cd "/media/ml4u/Extreme SSD/Paper-UAV"
# Hoặc nếu vào thư mục mã nguồn Paper_UAV:
cd "/media/ml4u/Extreme SSD/Paper-UAV/Paper_UAV"
```

### Bước 2: Kích hoạt môi trường Conda
```bash
conda activate safe-gs
```

### Bước 3: Cài đặt thư viện bổ sung (nếu cần)
```bash
conda install <tên_thư_viện>
# Ví dụ:
# conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
# Hoặc cài bằng pip nếu conda không hỗ trợ gói:
# pip install <tên_thư_viện>
```

---

## ⚠️ Lưu ý quan trọng

1. **Kiểm tra VRAM trước khi chạy:**
   - Trước khi bắt đầu huấn luyện (training) hoặc suy luận (inference), luôn kiểm tra trạng thái GPU và bộ nhớ VRAM còn trống bằng lệnh:
   ```bash
   nvidia-smi
   ```
   - Đảm bảo GPU còn đủ VRAM và không bị xung đột tiến trình với người dùng/tác vụ khác để tránh lỗi `CUDA out of memory`.

2. **Vị trí lưu trữ Checkpoint & Cache:**
   - **Tất cả các file checkpoint, weights model, dataset và bất kỳ file cache nào đều PHẢI lưu trên ổ đĩa `Extreme SSD`** (đường dẫn: `/media/ml4u/Extreme SSD/...`).
   - Tuyệt đối không lưu vào ổ đĩa hệ thống (`/` hoặc `/home/ml4u/...`) để tránh tình trạng tràn bộ nhớ hệ điều hành.

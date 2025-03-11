# CDCNPM-PTIT

## 📌 Giới thiệu
Dự án kiểm thử tự động với **Selenium** cho ứng dụng quản lý công việc **TodoManager**.

## 🚀 Cài đặt
### 1️⃣ Yêu cầu hệ thống
- **Python** >= 3.8
- **Google Chrome** >= 120
- **Chromedriver** tương thích với phiên bản Chrome
- **Git**
- **Selenium**
- **Pytest**

### 2️⃣ Clone dự án
```sh
git clone https://github.com/Harihuynh2007/CDCNPM-PTIT.git
cd CDCNPM-PTIT
```

### 3️⃣ Tạo và kích hoạt môi trường ảo
```sh
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 4️⃣ Cài đặt thư viện
```sh
pip install -r requirements.txt
```

### 5️⃣ Kiểm tra trình duyệt Chrome & Chromedriver
Kiểm tra phiên bản Chrome:
```sh
chrome --version
```
Tải Chromedriver tương ứng: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

## 🛠️ Chạy test với Selenium
### 1️⃣ Chạy toàn bộ test
```sh
pytest
```

### 2️⃣ Chạy test cụ thể
Ví dụ chạy test xóa task:
```sh
pytest tests/test3_delete.py
```

### 3️⃣ Tạo báo cáo test
Chạy test và tạo báo cáo HTML:
```sh
pytest --html=report.html
```
Sau đó mở `report.html` trong trình duyệt để xem kết quả.

## 💡 Lưu ý
- Nếu gặp lỗi **"Không tìm thấy task để xóa"**, hãy đảm bảo có ít nhất một task trong hệ thống trước khi chạy test xóa.
- Kiểm tra kỹ `chromedriver.exe` đã nằm trong thư mục `PATH` hoặc đặt trong thư mục dự án.

## 📞 Hỗ trợ
Nếu gặp vấn đề khi cài đặt hoặc chạy test, hãy liên hệ qua **Issues** trên GitHub hoặc email: [your-email@example.com](mailto:hminhhai2000@gmail.com)

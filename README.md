# 📋 TodoManager – Dự án kiểm thử tự động

Đây là dự án học phần *Chuyên đề Công nghệ phần mềm* (CDCNPM), triển khai ứng dụng quản lý công việc (todo-list) với giao diện web. Dự án bao gồm hệ thống đăng nhập, thêm/xóa task, và kiểm thử tự động bằng Selenium WebDriver.

---

## 🚀 1. Cách chạy project

### ✅ Mở bằng Live Server (VSCode)

1. Mở thư mục dự án bằng Visual Studio Code.
2. Cài extension **Live Server** nếu chưa có.
3. Click chuột phải vào file `login.html` → `Open with Live Server`.
4. Truy cập tại: `http://127.0.0.1:5500/TodoManager/login.html`

> ⚠️ Nếu muốn đổi port:  
Mở `settings.json` (Ctrl + Shift + P → "Preferences: Open Settings (JSON)"):
```json
"liveServer.settings.port": 3000
```

---

## 🧪 2. Cách chạy kiểm thử (Selenium + unittest)

### 🔧 Cài đặt môi trường

```bash
pip install selenium
```

> Tải **Edge WebDriver** tương thích với Microsoft Edge:  
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Đảm bảo `msedgedriver.exe` nằm trong `PATH` hoặc cùng thư mục với file `.py`.

---

### ▶️ Chạy toàn bộ test

1. Di chuyển toàn bộ file test vào thư mục `tests/`
2. Chạy file tổng:

```bash
python run_test.py
```

---

## 📁 3. Các file test

| File name              | Chức năng                           |
|------------------------|-------------------------------------|
| `test1_login.py`       | Kiểm thử đăng nhập thành công       |
| `test2_add_task.py`    | Thêm công việc mới                  |
| `test3_delete.py`      | Xóa task `"Học Selenium"` nếu có    |
| `test4_logout.py`      | Kiểm thử đăng xuất thành công       |
| `test5_login_fail.py`  | Đăng nhập sai mật khẩu (negative test) |

---

## 🛠 4. Các lỗi đã phát hiện & sửa

### ✅ `test3_delete.py`
- ❌ **Lỗi**: `AssertionError – Không có task để xóa`
  - 💡 **Sửa**: Tự động tạo task `"Học Selenium"` trước khi thử xóa.
- ❌ **Lỗi**: `ElementClickInterceptedException` do `#preloader` che nút đăng nhập
  - 💡 **Sửa**: Dùng `WebDriverWait` để đợi `#preloader` biến mất trước khi click.

### ✅ `test5_login_fail.py`
- ❌ **Lỗi**: Không kiểm tra có thông báo lỗi khi nhập sai mật khẩu
  - 💡 **Sửa**: Thêm dòng `assertIn("sai", errorMsg.text)` để xác nhận hiển thị lỗi.

---

## 👨‍💻 Tác giả

- Tên SV: [Điền tên tại đây]
- MSSV: [Mã số sinh viên]
- Lớp: [VD: CNTT3-K64]
- Trường: [VD: Đại học Công nghệ - ĐHQGHN]

---

## 📌 Ghi chú

- Các file `.py` được viết bằng Python 3.10+
- Dự án phù hợp kiểm thử giao diện, không yêu cầu backend thật (demo offline)

# BÁO CÁO ĐỒ ÁN CUỐI KHÓA
## Ứng dụng Quản lý Tủ sách cá nhân

**Sinh viên:** Lưu Thanh Hải  

## 1. Giới thiệu
Ứng dụng desktop giúp quản lý sách cá nhân: thêm sách, xem danh sách, đánh dấu đã đọc,
xóa sách và thống kê số lượng sách theo thể loại bằng biểu đồ cột.

## 2. Quy trình xây dựng
| Bước | Nội dung thực hiện |
|---|---|
| Phân tích yêu cầu | 5 chức năng: thêm, hiển thị, đánh dấu đã đọc, xóa, thống kê |
| Thiết kế giao diện | Tkinter: `LabelFrame`, `Entry`, `Combobox`, `Listbox` + `Scrollbar`, nút màu |
| Thiết kế lưu trữ | SQLite, bảng `sach(id, ten_sach, tac_gia, the_loai, da_doc)` |
| Xử lý logic | Các hàm CRUD trong `csdl_sach.py`, truy vấn tham số hóa (`?`) |
| Trực quan hóa | Matplotlib: biểu đồ cột có nhãn số liệu, lưới ngang |
| Đóng gói | PyInstaller `--onefile --windowed` |

## 3. Cấu trúc dự án
```
DoAn_TuSach/
├── csdl_sach.py          # Module CSDL (không biết gì về giao diện)
├── ung_dung_tu_sach.py   # Giao diện Tkinter + logic xử lý sự kiện
├── kiem_thu.py           # Kiểm thử module CSDL, tạo dữ liệu mẫu, xuất PNG
├── tu_sach.db            # Dữ liệu mẫu (sinh ra sau khi chạy)
├── thong_ke_the_loai.png # Biểu đồ thống kê
└── dist/                 # File .exe sau khi đóng gói
```

## 4. Điểm kỹ thuật nổi bật
- **Tách module**: tầng dữ liệu và tầng giao diện độc lập, dễ kiểm thử và bảo trì.
- **Truy vấn tham số hóa** chống SQL injection.
- **Xử lý lỗi nhập liệu**: báo lỗi khi để trống tên sách/tác giả; báo lỗi khi xóa hoặc đánh dấu mà chưa chọn sách; thông báo khi chưa có dữ liệu để thống kê.
- **Xác nhận trước khi xóa** để tránh mất dữ liệu nhầm.
- Đường dẫn file `.db` tính theo vị trí file chạy, nên dùng được cả khi chạy `.py` lẫn `.exe`.

## 5. Kiểm thử
- Module CSDL: thêm 4 sách → đánh dấu đã đọc → xóa 1 sách → thống kê (`python kiem_thu.py`).
- GUI: thêm sách, đánh dấu đã đọc, xóa, thử thêm với dữ liệu trống (báo lỗi, số sách không đổi).

## 6. Hướng dẫn chạy
```
python ung_dung_tu_sach.py
```
Đóng gói:
```
pip install pyinstaller matplotlib
pyinstaller --onefile --windowed ung_dung_tu_sach.py
```
File thực thi nằm tại `dist/ung_dung_tu_sach.exe`.

## 7. Hướng phát triển
Sửa thông tin sách, tìm kiếm/lọc theo thể loại hoặc trạng thái, xuất danh sách ra CSV,
thêm đánh giá (số sao) và ngày đọc.

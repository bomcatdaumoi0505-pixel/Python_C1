# --- BÀI TẬP 3: PEP8 ---
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000 

print("Họ và tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)


# --- BÀI TẬP 5: TOÁN TỬ ---
# 5.1 Toán tử số học
a = 17
b = 5

print("a + b =", a + b)    
print("a - b =", a - b)    
print("a * b =", a * b)    
print("a / b =", a / b)    
print("a // b =", a // b)  
print("a % b =", a % b)    
print("a ** b =", a ** b)  

# 5.2 Toán tử so sánh & logic
diem = 6.5
tuoi = 20

la_kha = (diem >= 6.5) and (diem < 8.0)
print("Đạt loại Khá:", la_kha)  

ngoai_do_tuoi_lao_dong = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60:", ngoai_do_tuoi_lao_dong)  

print("Phủ định điều kiện loại Khá:", not la_kha)  
print("Phủ định điều kiện tuổi:", not ngoai_do_tuoi_lao_dong)  

# 5.3 Toán tử gán & toán tử đặc biệt
x = 10

x += 5
print("x += 5 ->", x)

x -= 3
print("x -= 3 ->", x)

x *= 2
print("x *= 2 ->", x)

x /= 4
print("x /= 4 ->", x)

x //= 2
print("x //= 2 ->", x)

x **= 3
print("x **= 3 ->", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh sách:", 3 in danh_sach)

list1 = [1, 2, 3]
list2 = list1
print("list1 và list2 cùng tham chiếu:", list1 is list2)

# 5.4 Độ ưu tiên toán tử (Đã sửa lỗi cú pháp tại đây)
print(2 + 3 * 4 ** 2)                  # Output: 50
print((2 + 3) * 4 ** 2)                # Output: 80
print(10 > 5 and 3 < 1 or not False)   # Output: True


# --- BÀI TẬP 6: BIẾN & DYNAMIC TYPING ---
# 6.1 Giải thích lý thuyết Dynamic Typing
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))

# 6.2 Bài toán tổng hợp
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))
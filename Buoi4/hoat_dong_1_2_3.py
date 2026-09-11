# 1.1
print("--- HOẠT ĐỘNG 1 ---")
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print("Họ tên:", sinh_vien["ho_ten"])
print("Điểm TB:", sinh_vien.get("diem_tb"))
print("Lớp:", sinh_vien.get("lop", "Chua co"))

# 1.2
sinh_vien["lop"] = "CNTT01"       # Thêm khóa mới
sinh_vien["diem_tb"] = 9.0        # Sửa giá trị
print("Sau khi thêm/sửa:", sinh_vien)

diem_cu = sinh_vien.pop("diem_tb") # Xóa khóa
print(sinh_vien, "- Điểm đã xóa:", diem_cu)

sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # Cập nhật nhiều khóa
print("Sau khi update:", sinh_vien)



print("\n--- HOẠT ĐỘNG 2 ---")
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}

print("Danh sách môn học (keys):")
for mon in diem_mon_hoc.keys():
    print(mon)

print("\nDanh sách điểm (values):")
for diem in diem_mon_hoc.values():
    print(diem)

print("\nChi tiết môn học và điểm (items):")
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
print("Điểm trung bình:", round(tong_diem / len(diem_mon_hoc), 2))



print("\n--- HOẠT ĐỘNG 3 ---")
# 3.1 
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print("Điểm sau khi cộng:", diem_cong_diem)

ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print("Tên môn viết hoa:", ten_mon_viet_hoa)

# 3.2
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print("\nMôn học chung 2 kỳ (Giao &):", mon_hoc_ky1 & mon_hoc_ky2)
print("Tất cả môn học cả 2 kỳ (Hợp |):", mon_hoc_ky1 | mon_hoc_ky2)
print("Môn chỉ có ở kỳ 1 (Hiệu -):", mon_hoc_ky1 - mon_hoc_ky2)
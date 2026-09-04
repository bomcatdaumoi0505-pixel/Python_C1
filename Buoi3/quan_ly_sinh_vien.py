# HOẠT ĐỘNG 6:
danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]


danh_sach_sv.append((8.0, "Em"))
danh_sach_sv.remove((7.0, "Binh"))
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

print("Chi (9.2 điểm) có trong danh sách không?", (9.2, "Chi") in danh_sach_sv)

danh_sach_sv.sort()
print("\nDanh sách sau khi sắp xếp theo điểm TĂNG DẦN:")
for diem, ten in danh_sach_sv:
    print(f"{ten:<10} - Điểm: {diem}")


danh_sach_sv.sort(reverse=True)
print("\nDanh sách sau khi sắp xếp theo điểm GIẢM DẦN:")
for diem, ten in danh_sach_sv:
    print(f"{ten:<10} - Điểm: {diem}")
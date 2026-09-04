# HOẠT ĐỘNG 1
print("--- HOẠT ĐỘNG 1 ---")

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print("Phần tử đầu tiên:", diem_so[0])
print("Phần tử cuối cùng:", diem_so[-1])
print("Cắt từ vị trí 1 đến trước 4:", diem_so[1:4])
print("Lấy cách 1 phần tử (step = 2):", diem_so[::2])
print("Đảo ngược danh sách:", diem_so[::-1])


ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung")
ten_sv.insert(1, "Em")
print("Sau khi append và insert:", ten_sv)

ten_sv.remove("Chi")
pop_ra = ten_sv.pop()
print(ten_sv, "- đã xóa:", pop_ra)

ten_sv.sort()
print("Sau khi sort tăng dần:", ten_sv)

ten_sv.reverse()
print("Sau khi reverse (đảo ngược):", ten_sv)

ten_sv.extend(["Giang", "Hoa"])
print("Sau khi extend:", ten_sv)



# HOẠT ĐỘNG 2

print("\n--- HOẠT ĐỘNG 2 ---")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0
for diem in diem_so:
    print(diem)
    tong = tong + diem
print("Tổng điểm:", tong)
print("Điểm trung bình:", round(tong / len(diem_so), 2))

ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("In theo từng hàng:")
for hang in ma_tran:
    print(hang)

print("In từng phần tử dạng lưới:")
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

# YÊU CẦU BÀI TẬP: Tính tổng tất cả phần tử trong ma_tran
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran = tong_ma_tran + phan_tu

print("Tổng tất cả phần tử trong ma trận là:", tong_ma_tran)



 #HOẠT ĐỘNG 3: 
print("\n--- HOẠT ĐỘNG 3 ---")
day_so = list(range(1, 21))
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]
print("Số chẵn:", so_chan)
print("Số lẻ:", so_le)


diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print("Điểm sau khi cộng ưu đãi:", diem_cong)
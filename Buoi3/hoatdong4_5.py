import math
print("--- HOẠT ĐỘNG 4 ---")
toa_do = (3, 5)
print("Tọa độ:", toa_do, "| Kiểu dữ liệu:", type(toa_do))


x, y = toa_do
print("x =", x, "- y =", y)


a, b = 10, 20
a, b = b, a
print("Sau khi đổi chỗ: a =", a, "- b =", b)

c, d = 17, 5
thuong_du = divmod(c, d)
thuong, du = thuong_du
print(f"{c} chia {d} được thương {thuong}, dư {du}")



# HOẠT ĐỘNG 5:

import math

diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoảng cách giữa {diem_a} và {diem_b} là: {round(khoang_cach, 2)}")


cac_diem = [(0, 0), (3, 4), (6, 8)]

print("\nKhoảng cách từ các điểm đến gốc tọa độ (0, 0):")
for diem in cac_diem:
    x, y = diem
    kc_den_goc = math.sqrt(x**2 + y**2) 
    print(f"Điểm {diem}: khoảng cách = {round(kc_den_goc, 2)}")
# Hoat dong 3: Number - int, float, complex & ham built-in
# Bai tap 3.1
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))
print(int(so_thuc))

# Bai tap 3.2
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))
print(round(b))
print(round(b, 2))
print(pow(c, 2))
print(divmod(c, d))

# Bai tap 3.3
import math
a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

# Hoat dong 4: String - indexing, slicing & phuong thuc xu ly
# Bai tap 4.1
cau = "Lap trinh Python rat thu vi"
print(cau[0])
print(cau[-1])
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])
print(cau == cau[::-1])

# Bai tap 4.2
ten = "Nam"
ten_moi = "T" + ten[1:]
print(ten_moi)

# Bai tap 4.3
cau_3 = "  Toi dang HOC Python rat vui  "
print(cau_3.strip())
print(cau_3.strip().upper())
print(cau_3.strip().lower())
print(cau_3.strip().replace("HOC", "hoc"))
print(cau_3.strip().split())
print(len(cau_3.strip().split()))
print(cau_3.count("o"))
print(cau_3.find("Python"))
print(cau_3.strip().startswith("Toi"))
print(cau_3.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

# Bai tap 4.4
ho_ten_tho = "  nguyen   van   an  "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach)
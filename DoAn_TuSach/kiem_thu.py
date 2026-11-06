"""Kiem thu module CSDL (khong can giao dien), tao du lieu mau va xuat bieu do PNG.

Chay:  python kiem_thu.py
Ket qua: tu_sach.db (du lieu mau) va thong_ke_the_loai.png
"""
import os

import matplotlib
matplotlib.use("Agg")  # khong can cua so, chi xuat file anh
import matplotlib.pyplot as plt

import csdl_sach as db

# Bat dau tu CSDL sach de test lap lai duoc
if os.path.exists(db.TEN_FILE_CSDL):
    os.remove(db.TEN_FILE_CSDL)
db.tao_bang_neu_chua_co()

# 1. Them sach
for sach in [
    ("Doc Vi Nhan Sinh", "Robert Cialdini", "Ky nang song"),
    ("Dac Nhan Tam", "Dale Carnegie", "Ky nang song"),
    ("Nha Gia Kim", "Paulo Coelho", "Tieu thuyet"),
    ("Sapiens", "Yuval Noah Harari", "Lich su"),
]:
    db.them_sach(*sach)
ds = db.lay_toan_bo_sach()
assert len(ds) == 4
print("Danh sach sach:")
for dong in ds:
    print(dong)

# 2. Danh dau da doc
db.danh_dau_da_doc(1)
assert db.lay_toan_bo_sach()[0][4] == 1
assert db.lay_toan_bo_sach()[1][4] == 0
print("Sau khi danh dau da doc id=1:", db.lay_toan_bo_sach()[0])

# 3. Xoa
db.xoa_sach(3)
assert len(db.lay_toan_bo_sach()) == 3
print("Sau khi xoa id=3:", len(db.lay_toan_bo_sach()), "cuon")

# 4. Thong ke
thong_ke = db.thong_ke_theo_the_loai()
assert dict(thong_ke) == {"Ky nang song": 2, "Lich su": 1}
print("Thong ke theo the loai:", thong_ke)

# 5. Xuat bieu do
the_loai = [d[0] for d in thong_ke]
so_luong = [d[1] for d in thong_ke]
plt.figure(figsize=(7, 4.5))
cac_cot = plt.bar(the_loai, so_luong, color="cornflowerblue", width=0.5)
for cot, gt in zip(cac_cot, so_luong):
    plt.text(cot.get_x() + cot.get_width() / 2, gt, str(gt),
             ha="center", va="bottom", fontweight="bold")
plt.title("SỐ LƯỢNG SÁCH THEO THỂ LOẠI", fontweight="bold")
plt.xlabel("Thể loại")
plt.ylabel("Số lượng sách")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.gca().set_axisbelow(True)
plt.tight_layout()
duong_dan_anh = os.path.join(db.THU_MUC_GOC, "thong_ke_the_loai.png")
plt.savefig(duong_dan_anh, dpi=120)
print("Da xuat bieu do:", duong_dan_anh)

print("TEST PASS - module CSDL hoat dong dung")

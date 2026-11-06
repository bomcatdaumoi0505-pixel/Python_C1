"""Kiem thu GUI tu dong (mo phong thao tac nguoi dung) va nhap du lieu mau de demo.

Chay:  python kiem_thu_gui.py
"""
import os
from tkinter import messagebox

import csdl_sach as db
import ung_dung_tu_sach as ui

# Thay hop thoai bang ham in ra man hinh de khong phai bam chuot
messagebox.showinfo = lambda tieu_de, nd: print(f"[INFO] {tieu_de}: {nd}")
messagebox.showerror = lambda tieu_de, nd: print(f"[LOI] {tieu_de}: {nd}")
messagebox.askyesno = lambda tieu_de, nd: True

if os.path.exists(db.TEN_FILE_CSDL):
    os.remove(db.TEN_FILE_CSDL)

app = ui.UngDungTuSach()


def nhap(ten, tac_gia, the_loai):
    app.o_nhap_ten_sach.insert(0, ten)
    app.o_nhap_tac_gia.insert(0, tac_gia)
    app.chon_the_loai.set(the_loai)
    app.xu_ly_them_sach()


def chon(chi_so):
    app.listbox_sach.selection_clear(0, "end")
    app.listbox_sach.selection_set(chi_so)


# 1. Them 2 cuon
nhap("Nha Gia Kim", "Paulo Coelho", "Tieu thuyet")
nhap("Sapiens", "Yuval Noah Harari", "Lich su")
print("Danh sach sau khi them 2 cuon:", *db.lay_toan_bo_sach(), sep="\n")
assert app.listbox_sach.size() == 2

# 2. Danh dau da doc cuon dau
chon(0)
app.xu_ly_danh_dau_da_doc()
assert db.lay_toan_bo_sach()[0][4] == 1
print("Sau khi danh dau da doc cuon dau tien:", *db.lay_toan_bo_sach(), sep="\n")

# 3. Xoa cuon thu hai
chon(1)
app.xu_ly_xoa_sach()
assert len(db.lay_toan_bo_sach()) == 1
print("Sau khi xoa cuon thu hai:", *db.lay_toan_bo_sach(), sep="\n")

# 4. Validate: them rong, thao tac khi chua chon
nhap("", "", "Khac")
assert len(db.lay_toan_bo_sach()) == 1
app.listbox_sach.selection_clear(0, "end")
app.xu_ly_xoa_sach()
app.xu_ly_danh_dau_da_doc()
assert len(db.lay_toan_bo_sach()) == 1
print("So luong sach sau khi thu them rong (phai van la 1):", len(db.lay_toan_bo_sach()))
print("TEST PASS - toan bo chuc nang CRUD tren GUI hoat dong dung\n")

# 5. Nhap du lieu mau de demo
for sach in [
    ("Đắc Nhân Tâm", "Dale Carnegie", "Ky nang song"),
    ("Đọc Vị Người Khác", "David J. Lieberman", "Ky nang song"),
    ("Phàm Nhân Tu Tiên", "Vong Ngữ", "Tieu thuyet"),
    ("Mắt Biếc", "Nguyễn Nhật Ánh", "Tieu thuyet"),
    ("Đại Việt Sử Ký Toàn Thư", "Ngô Sĩ Liên", "Lich su"),
    ("Lược Sử Thời Gian", "Stephen Hawking", "Khoa hoc"),
    ("Vũ Trụ", "Carl Sagan", "Khoa hoc"),
    ("Gen: Lịch Sử Và Tương Lai", "Siddhartha Mukherjee", "Khoa hoc"),
    ("Cha Giàu Cha Nghèo", "Robert Kiyosaki", "Kinh te"),
    ("Nhà Đầu Tư Thông Minh", "Benjamin Graham", "Kinh te"),
]:
    nhap(*sach)
for chi_so in (1, 3, 6, 9):
    chon(chi_so)
    app.xu_ly_danh_dau_da_doc()

print("Du lieu mau:", db.lay_toan_bo_sach().__len__(), "cuon")
print("Thong ke:", db.thong_ke_theo_the_loai())
app.destroy()

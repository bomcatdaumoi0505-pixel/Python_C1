"""Giao dien Tkinter cho ung dung Quan ly Tu sach ca nhan."""
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_sach as db

DANH_SACH_THE_LOAI = ["Ky nang song", "Tieu thuyet", "Lich su", "Khoa hoc", "Kinh te", "Khac"]


class UngDungTuSach(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Tu sach ca nhan")
        self.geometry("560x520")
        self.resizable(False, False)
        self.danh_sach_hien_tai = []
        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sach()

    def khoi_tao_giao_dien(self):
        # --- Khung nhap lieu ---
        khung_nhap = tk.LabelFrame(self, text="Thêm sách mới", padx=10, pady=5)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Tên sách:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten_sach = tk.Entry(khung_nhap, width=40)
        self.o_nhap_ten_sach.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Tác giả:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_tac_gia = tk.Entry(khung_nhap, width=40)
        self.o_nhap_tac_gia.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Thể loại:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_the_loai = ttk.Combobox(khung_nhap, values=DANH_SACH_THE_LOAI,
                                          width=37, state="readonly")
        self.chon_the_loai.current(0)
        self.chon_the_loai.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm sách", command=self.xu_ly_them_sach,
                  bg="#2e7d32", fg="white", font=("Segoe UI", 9, "bold"),
                  width=12).grid(row=3, column=0, columnspan=2, pady=10)

        # --- Khung danh sach ---
        khung_danh_sach = tk.LabelFrame(self, text="Danh sách sách trong tủ", padx=5, pady=5)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_sach = tk.Listbox(khung_danh_sach, width=75, height=12,
                                       activestyle="none")
        self.listbox_sach.pack(side="left", fill="both", expand=True)
        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical",
                                  command=self.listbox_sach.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sach.config(yscrollcommand=thanh_cuon.set)

        # --- Khung nut thao tac ---
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(khung_nut_thao_tac, text="Đánh dấu đã đọc",
                  command=self.xu_ly_danh_dau_da_doc, bg="#1565c0", fg="white",
                  font=("Segoe UI", 9, "bold")).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut_thao_tac, text="Xóa sách", command=self.xu_ly_xoa_sach,
                  bg="#c62828", fg="white",
                  font=("Segoe UI", 9, "bold")).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut_thao_tac, text="Thống kê theo thể loại",
                  command=self.xu_ly_thong_ke, bg="#ef6c00", fg="white",
                  font=("Segoe UI", 9, "bold")).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach_sach(self):
        self.listbox_sach.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_sach()
        for sach in self.danh_sach_hien_tai:
            _id_sach, ten_sach, tac_gia, the_loai, da_doc = sach
            trang_thai = "[Đã đọc]" if da_doc == 1 else "[Chưa đọc]"
            self.listbox_sach.insert(tk.END, f"{trang_thai} {ten_sach} - {tac_gia} - ({the_loai})")

    def lay_id_sach_dang_chon(self, thong_bao_loi):
        """Tra ve id cua sach dang chon, hoac None (kem hop thoai loi) neu chua chon."""
        lua_chon = self.listbox_sach.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", thong_bao_loi)
            return None
        return self.danh_sach_hien_tai[lua_chon[0]][0]

    def xu_ly_them_sach(self):
        ten_sach = self.o_nhap_ten_sach.get().strip()
        tac_gia = self.o_nhap_tac_gia.get().strip()
        the_loai = self.chon_the_loai.get()

        if ten_sach == "" or tac_gia == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tên sách và tác giả.")
            return

        db.them_sach(ten_sach, tac_gia, the_loai)
        self.o_nhap_ten_sach.delete(0, tk.END)
        self.o_nhap_tac_gia.delete(0, tk.END)
        self.tai_lai_danh_sach_sach()
        messagebox.showinfo("Thành công", f"Đã thêm sách: {ten_sach}")

    def xu_ly_xoa_sach(self):
        id_sach = self.lay_id_sach_dang_chon("Vui lòng chọn một cuốn sách trong danh sách để xóa.")
        if id_sach is None:
            return
        if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa cuốn sách này?"):
            return
        db.xoa_sach(id_sach)
        self.tai_lai_danh_sach_sach()

    def xu_ly_danh_dau_da_doc(self):
        id_sach = self.lay_id_sach_dang_chon("Vui lòng chọn một cuốn sách để đánh dấu đã đọc.")
        if id_sach is None:
            return
        db.danh_dau_da_doc(id_sach)
        self.tai_lai_danh_sach_sach()

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_the_loai()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu sách để thống kê.")
            return

        cac_the_loai = [dong[0] for dong in du_lieu_thong_ke]
        so_luong = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(7, 4.5))
        cac_cot = plt.bar(cac_the_loai, so_luong, color="cornflowerblue", width=0.5)
        for cot, gia_tri in zip(cac_cot, so_luong):
            plt.text(cot.get_x() + cot.get_width() / 2, gia_tri, str(gia_tri),
                     ha="center", va="bottom", fontweight="bold")
        plt.title("SỐ LƯỢNG SÁCH THEO THỂ LOẠI", fontweight="bold")
        plt.xlabel("Thể loại")
        plt.ylabel("Số lượng sách")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.gca().set_axisbelow(True)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ung_dung = UngDungTuSach()
    ung_dung.mainloop()

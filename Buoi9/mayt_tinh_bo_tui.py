import tkinter as tk
from tkinter import messagebox

def nhap_phim(gia_tri):
    hien_tai = entry_hien_thi.get()
    entry_hien_thi.delete(0, tk.END)
    entry_hien_thi.insert(0, hien_tai + str(gia_tri))

def xoa_man_hinh():
    entry_hien_thi.delete(0, tk.END)

def tinh_ket_qua():
    bieu_thuc = entry_hien_thi.get()
    try:
        ket_qua = str(eval(bieu_thuc))
        entry_hien_thi.delete(0, tk.END)
        entry_hien_thi.insert(0, ket_qua)
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0.")
        entry_hien_thi.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le.")
        entry_hien_thi.delete(0, tk.END)

cua_so = tk.Tk()
cua_so.title("May tinh bo tu")
cua_so.geometry("300x400")
cua_so.resizable(False, False)
entry_hien_thi = tk.Entry(cua_so, font=("Arial", 18), justify="right", bd=5)
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=5)
cac_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
for (text, hang, cot) in cac_nut:
    if text == '=':
        nut = tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, bg="#000000", fg="white", command=tinh_ket_qua)
    elif text == 'C':
        nut = tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, bg="#f43636", fg="white", command=xoa_man_hinh)
    else:
        nut = tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, command=lambda t=text: nhap_phim(t))
    nut.grid(row=hang, column=cot, padx=5, pady=5)
cua_so.mainloop()
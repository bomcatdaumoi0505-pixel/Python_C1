
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Bo cuc bang pack()")
cua_so.geometry("300x250")

tk.Label(cua_so, text="Ho ten:").pack(pady=5)
tk.Label(cua_so, text="Tuoi:").pack(pady=5)
tk.Label(cua_so, text="Email:").pack(pady=5)

nut_dong_y = tk.Button(cua_so, text="Dong y")
nut_dong_y.pack(side="left", padx=20, pady=15)

nut_huy = tk.Button(cua_so, text="Huy")
nut_huy.pack(side="right", padx=20, pady=15)

cua_so.mainloop()
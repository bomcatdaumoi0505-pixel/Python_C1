import csdl_sach as db

# Khởi tạo bảng
db.tao_bang_neu_chua_co()

# Thêm 4 sách
db.them_sach('Doc Vi Nhan Sinh', 'Robert Cialdini', 'Ky nang song')
db.them_sach('Dac Nhan Tam', 'Dale Carnegie', 'Ky nang song')
db.them_sach('Nha Gia Kim', 'Paulo Coelho', 'Tieu thuyet')
db.them_sach('Sapiens', 'Yuval Noah Harari', 'Lich su')

print("Danh sach sach:")
for s in db.lay_toan_bo_sach(): print(s)

# Đánh dấu đã đọc id=1
db.danh_dau_da_doc(1)
print("\nSau khi danh dau da doc id=1:")
print(db.lay_toan_bo_sach()[0])

# Xóa 1 sách (Nha Gia Kim - id=3)
db.xoa_sach(3)

print("\nThong ke theo the loai:")
print(db.thong_ke_theo_the_loai())

tu_dien_anh_viet = {
    "hello": "xin chao",
    "book": "quyen sach",
    "table": "cai ban"
}


print("Tra từ 'hello':", tu_dien_anh_viet.get("hello", "Khong tim thay tu nay"))
print("Tra từ 'computer':", tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"))


tu_dien_anh_viet["computer"] = "may tinh"

tu_dien_anh_viet.pop("table")

print("\nTừ điển hiện tại:")
for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh} - {tu_viet}")
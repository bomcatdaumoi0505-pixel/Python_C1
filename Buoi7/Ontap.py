
danh_sach_sach = [
    {"ma_sach": "S001", "ten_sach": "Lap trinh Python co ban", "tac_gia": "Nguyen Van A", "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S002", "ten_sach": "Cau truc du lieu", "tac_gia": "Tran Thi B", "trang_thai": "Co san", "nguoi_muon": ""},
    {"ma_sach": "S003", "ten_sach": "Co so du lieu SQL", "tac_gia": "Le Van C", "trang_thai": "Co san", "nguoi_muon": ""}
]
lich_su_phat = []


def nhap_so(loi_nhac):
    while True:
        try:
            val = int(input(loi_nhac))
            if val >= 0:
                return val
            print("-> Nhap so >= 0!")
        except ValueError:
            print("-> Vui long nhap so nguyen!")


def tim_sach(ma_sach):
    for s in danh_sach_sach:
        if s["ma_sach"] == ma_sach:
            return s
    return None


def hien_thi():
    print("\n--- DANH SACH SACH ---")
    for s in danh_sach_sach:
        print(f"[{s['ma_sach']}] {s['ten_sach']} - TG: {s['tac_gia']} | TT: {s['trang_thai']} | NM: {s['nguoi_muon']}")


def them_sach():
    ma = input("Ma sach: ").strip().upper()
    if tim_sach(ma):
        print("-> Ma sach da ton tai!")
        return
    ten = input("Ten sach: ").strip()
    tac_gia = input("Tac gia: ").strip()
    danh_sach_sach.append({"ma_sach": ma, "ten_sach": ten, "tac_gia": tac_gia, "trang_thai": "Co san", "nguoi_muon": ""})
    print("-> Them thanh cong!")


def muon_sach():
    s = tim_sach(input("Ma sach muon: ").strip().upper())
    if not s:
        print("-> Khong tim thay sach!")
    elif s["trang_thai"] == "Da muon":
        print("-> Sach dang duoc muon!")
    else:
        s["nguoi_muon"] = input("Ten nguoi muon: ").strip()
        s["trang_thai"] = "Da muon"
        print("-> Muon sach thanh cong!")


def tra_sach():
    s = tim_sach(input("Ma sach tra: ").strip().upper())
    if not s:
        print("-> Khong tim thay sach!")
    elif s["trang_thai"] == "Co san":
        print("-> Sach dang o trong kho!")
    else:
        tre = nhap_so("So ngay tre (0 neu dung han): ")
        phat = tre * 5000
        if phat > 0:
            lich_su_phat.append({"ma": s["ma_sach"], "nguoi": s["nguoi_muon"], "tien": phat})
            print(f"-> Tre {tre} ngay, phat: {phat:,} VND")
        else:
            print("-> Tra dung han!")
        s["trang_thai"] = "Co san"
        s["nguoi_muon"] = ""


def thong_ke():
    if not lich_su_phat:
        print("-> Chưa co tien phat!")
        return
    tong = sum(p["tien"] for p in lich_su_phat)
    print("\n--- LICH SU PHAT ---")
    for p in lich_su_phat:
        print(f"Ma: {p['ma']} | Nguoi: {p['nguoi']} | Phat: {p['tien']:,} VND")
    print(f">>> TONG TIEN PHAT: {tong:,} VND")


def main():
    while True:
        print("\n=== QUAN LY THU VIEN ===")
        print("1. Xem danh sach | 2. Them sach | 3. Muon sach")
        print("4. Tra sach      | 5. Thong ke  | 0. Thoat")
        chon = input("Chon (0-5): ").strip()
        
        if chon == "1": hien_thi()
        elif chon == "2": them_sach()
        elif chon == "3": muon_sach()
        elif chon == "4": tra_sach()
        elif chon == "5": thong_ke()
        elif chon == "0":
            print("Tam biet!")
            break
        else:
            print("-> Chon sai, nhap lai!")

if __name__ == "__main__":
    main()
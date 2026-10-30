import requests

print("=== Bai tap 5.1: Goi API GitHub ===")
response_gh = requests.get("https://api.github.com/repos/python/cpython")

if response_gh.status_code == 200:
    du_lieu = response_gh.json()
    print("Ten repository:", du_lieu["full_name"])
    print("So luot gan sao (stars):", du_lieu["stargazers_count"])
    print("Ngon ngu chinh:", du_lieu["language"])
else:
    print("Goi API that bai, ma loi:", response_gh.status_code)

print("\n=== Bai tap 5.2: Goi API ty gia ngoai te ===")
response_er = requests.get("https://open.er-api.com/v6/latest/USD")

if response_er.status_code == 200:
    du_lieu_er = response_er.json()
    ty_gia_vnd = du_lieu_er["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Khong lay duoc ty gia, ma loi:", response_er.status_code)
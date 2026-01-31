def kiem_tra_dinh_dang(s):
    if len(s) != 10:
        return False
    
    if s[2] != "/" or s[5] != "/":
        return False
    
    parts = s.split("/")
    if len(parts) != 3:
        return False
    
    chu_so = "0123456789"
    for p in parts:
        if len(p) == 0: 
            return False
        for ky_tu in p:
            if ky_tu not in chu_so:
                return False
                
    return True
            
    return True
def kiem_tra_nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    else:
        return False

chuoi_nhap = input("Nhập ngày tháng năm: ")

if kiem_tra_dinh_dang(chuoi_nhap):
    nam = int(chuoi_nhap[6:]) 
    
    if kiem_tra_nam_nhuan(nam):
        print(f"{nam} là năm nhuận.")
    else:
        print(f"{nam} không là năm nhuận.")
else:

    print("yêu cầu nhập đúng định dạng dd/MM/yyyy")
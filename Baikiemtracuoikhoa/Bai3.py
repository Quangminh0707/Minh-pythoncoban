danh_sach_xe = []
hang_xe_cho_phep = ["Honda", "Yamaha", "Sym", "Piaggio", "Suzuki", "Ducati", "Hãng khác"]

def hien_thi():
    print("\n--- DANH SÁCH XE TRONG BÃI ---")
    if len(danh_sach_xe) == 0:
        print("Bãi xe hiện đang trống.")
    else:
        for xe in danh_sach_xe:
            print(f"Biển số: {xe['bien_so']} | Tên: {xe['ten']} | CMND: {xe['cmnd']} | Hãng: {xe['hang']} | Phí: {xe['phi']}")

def them_xe():
    print("\n--- THÊM XE MỚI ---")
    
    while True:
        bs = input("Nhập biển số xe (tối đa 20 ký tự): ")
        if 0 < len(bs) <= 20:
            trung = False
            for xe in danh_sach_xe:
                if xe['bien_so'] == bs:
                    trung = True
                    break
            if trung:
                print("Lỗi: Biển số này đã tồn tại!")
            else:
                break
        else:
            print("Lỗi: Biển số không được trống và tối đa 20 ký tự.")

    while True:
        ten = input("Nhập họ tên sinh viên (tối đa 40 ký tự): ")
        if 0 < len(ten) <= 40:
            break
        print("Lỗi: Họ tên không hợp lệ.")

    while True:
        try:
            cmnd = int(input("Nhập CMND (chỉ nhập số): "))
            phi = float(input("Nhập phí gửi xe (Nghìn đồng): "))
            break 
        except ValueError:
            print("Lỗi: CMND và Phí bắt buộc phải là số. Vui lòng nhập lại!")

    while True:
        print("Danh sách hãng:", hang_xe_cho_phep)
        hang = input("Chọn hãng xe: ")
        if hang in hang_xe_cho_phep:
            break
        print("Lỗi: Hãng xe không đúng danh sách.")

    xe_moi = {
        "bien_so": bs,
        "ten": ten,
        "cmnd": cmnd,
        "hang": hang,
        "phi": phi
    }
    danh_sach_xe.append(xe_moi)
    print("Thêm xe thành công!")

def xoa_xe():
    bs_can_xoa = input("Nhập biển số xe muốn xóa: ")
    xe_tim_thay = None
    
    for xe in danh_sach_xe:
        if xe['bien_so'] == bs_can_xoa:
            xe_tim_thay = xe
            break
            
    if xe_tim_thay:
        xac_nhan = input(f"Xác nhận xóa xe {bs_can_xoa}? (Có/Không): ")
        if xac_nhan.lower() == "Có":
            danh_sach_xe.remove(xe_tim_thay)
            print("Đã xóa xong.")
    else:
        print("Không tìm thấy biển số này.")

while True:
    print("\n===== BÃI ĐỔ XE TRUNG TÂM CODEGYM ====")
    print("\n========= MENU QUẢN LÝ =========")
    print("1. Danh sách | 2. Thêm | 3. Xóa | 4. Thoát")
    chon = input("Lựa chọn của bạn: ")
    if chon == "1": 
        hien_thi()
    elif chon == "2": 
        them_xe()
    elif chon == "3": 
        xoa_xe()
    elif chon == "4": 
        break
    else: print("Chọn lại từ 1-4.")
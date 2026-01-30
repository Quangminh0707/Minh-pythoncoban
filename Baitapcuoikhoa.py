import os

Luutru = "sanpham.txt"

danh_sach_sp = []
if os.path.exists(Luutru):
    with open(Luutru, "r", encoding="utf-8") as f:
        for dong in f:
            
            du_lieu = dong.strip().split(",")
            if len(du_lieu) == 3:
                danh_sach_sp.append(du_lieu)

while True:
    print("\n--- QUẢN LÝ SẢN PHẨM ---")
    print("1. Xem danh sách")
    print("2. Thêm mới")
    print("3. Sửa sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Thoát")
    
    chon = input("Chọn chức năng (1-5): ")

    if chon == "1":
        print("\nDANH SÁCH SẢN PHẨM:")
        for sp in danh_sach_sp:
            print(f"Mã: {sp[0]} - Tên: {sp[1]} - Giá: {sp[2]}")
    
    elif chon == "2":
        try:
            ma = input("Nhập mã: ")
            ten = input("Nhập tên: ")
            gia = float(input("Nhập giá: ")) # Kiểm tra lỗi nhập số
            danh_sach_sp.append([ma, ten, str(gia)])
            print("Đã thêm!")
        except ValueError:
            print("Lỗi: Giá phải là con số!")

    elif chon == "3":
        ma_sua = input("Nhập mã cần sửa: ")
        cho_thay = False
        for sp in danh_sach_sp:
            if sp[0] == ma_sua:
                sp[1] = input("Tên mới: ")
                try:
                    sp[2] = str(float(input("Giá mới: ")))
                    print("Đã sửa!")
                    cho_thay = True
                    break
                except ValueError:
                    print("Lỗi: Giá không hợp lệ!")
                    cho_thay = True
        if not cho_thay: print("Không tìm thấy mã này!")

    elif chon == "4":
        ma_xoa = input("Nhập mã cần xóa: ")
        for sp in danh_sach_sp:
            if sp[0] == ma_xoa:
                danh_sach_sp.remove(sp)
                print("Đã xóa!")
                break
    
    elif chon == "5":
        with open(Luutru, "w", encoding="utf-8") as f:
            for sp in danh_sach_sp:
                f.write(f"{sp[0]},{sp[1]},{sp[2]}\n")
        print("Đã lưu dữ liệu. Tạm biệt!")
        break
    
    else:
        print("Chọn sai, vui lòng chọn lại!")
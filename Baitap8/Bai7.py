danh_sach_ban_be = []

def menu():
    global danh_sach_ban_be 

    print("\n-------Chương trình quản lý bạn bè trên facebook-------")
    print("1. Hiển thị danh sách")
    print("2. Thêm mới bạn bè")
    print("3. Xóa bạn bè")
    print("4. Sửa tên bạn bè")
    print("5. Thoát")
    
    a = input("\nMời bạn nhập lựa chọn (1-5): ")

    if a == '1':
        print("\n--- DANH SÁCH BẠN BÈ ---")
        # Vòng lặp 2 chiều in trên cùng một hàng
        for ban in danh_sach_ban_be:
            for thong_tin in ban:
                print(thong_tin, end=" | ") # end=" | " giúp các thông tin nằm cùng hàng và cách nhau bởi dấu gạch
            print() # Lệnh print trống này để xuống dòng sau khi in xong 1 người
        menu()

    elif a == '2':
        ten = input("Nhập tên: ")
        ngay_sinh = input("Nhập ngày sinh: ")
        dia_chi = input("Nhập địa chỉ: ")
        sdt = input("Nhập số điện thoại: ")
        danh_sach_ban_be.append([ten, ngay_sinh, dia_chi, sdt])
        menu()

    elif a == '3':
        ten_xoa = input("Nhập tên cần xóa: ")
        danh_sach_ban_be = [b for b in danh_sach_ban_be if b[0] != ten_xoa]
        menu()

    elif a == '4':
        ten_cu = input("Nhập tên cũ: ")
        for ban in danh_sach_ban_be:
            if ban[0] == ten_cu:
                ban[0] = input("Nhập tên mới: ")
        menu()

    elif a == '5':
        print("Đã thoát.")
        return

    else:
        print("Nhập sai!")
        menu()

menu()
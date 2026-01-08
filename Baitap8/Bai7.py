danh_sach_ban_be = []

def menu():
    print("-------Chương trình quản lý bạn bè trên facebook-------" )
    print("Nhập phím 1 để hiển thị danh sách bạn bè")
    print("Nhập phím 2 để thêm mới bạn bè")
    print("Nhập phím 3 để xóa bạn bè")
    print("Nhập phím 4 để sửa tên bạn bè")
    print("Nhập phím 5 để thoát chương trình")
    
    a = input("\nMời bạn nhập lựa chọn (1-5): ")


    if a == '1':
        print("\n--- DANH SÁCH BẠN BÈ ---")
        if len(danh_sach_ban_be) == 0:
            print("Danh sách trống.")
        else:
            for i in range(len(danh_sach_ban_be)):
                print(str(i + 1) + ". " + danh_sach_ban_be[i])
        menu() 

    elif a == '2':
        ten_moi = input("Nhập tên bạn mới: ")
        danh_sach_ban_be.append(ten_moi)
        menu()

    elif a == '3':
        ten_xoa = input("Nhập tên cần xóa: ")
        if ten_xoa in danh_sach_ban_be:
            danh_sach_ban_be.remove(ten_xoa)
        else:
            print("Không tìm thấy.")
        menu()

    elif a == '4':
        ten_cu = input("Nhập tên cũ: ")
        if ten_cu in danh_sach_ban_be:
            vi_tri = danh_sach_ban_be.index(ten_cu)
            danh_sach_ban_be[vi_tri] = input("Nhập tên mới: ")
        else:
            print("Không tồn tại.")
        menu()

    elif a == '5':
        print("Đã thoát chương trình.")
        return 

    else:
        print("Lựa chọn sai, mời nhập lại.")
        menu()


menu()
danh_sach_sv = []

try:
    ten = input("Nhập tên sinh viên: ")
    tuoi = int(input("Nhập tuổi sinh viên: ")) 
    danh_sach_sv.append({"tên": ten, "tuổi": tuoi})
    print("Thêm thành công!")
except ValueError:
    print("Lỗi: Tuổi phải là một số nguyên.")
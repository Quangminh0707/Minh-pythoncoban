import password_utils

pw = input("Nhập mật khẩu: ")

if password_utils.is_strong_password(pw):
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")
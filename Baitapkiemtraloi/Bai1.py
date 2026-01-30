try:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    print(f"Kết quả: {a / b}")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho số 0.")
except ValueError:
    print("Lỗi: Vui lòng nhập số thực hợp lệ.")
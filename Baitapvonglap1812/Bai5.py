while True :
    n = int(input("Nhập vào số nguyên (Nhập 0 để dừng) : "))
    if n == 0:
        print("Chương trình đã được dừng")
        break
    if n % 2 == 0:
        print(n,"là số chắn")
    else :
        print(n,"là số lẻ")
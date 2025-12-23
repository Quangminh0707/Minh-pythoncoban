chieu_dai = 20
chieu_rong = 7

for i in range(chieu_rong):
    for j in range(chieu_dai):
        # Kiểm tra nếu là biên của hình chữ nhật
        if i == 0 or i == chieu_rong - 1 or j == 0 or j == chieu_dai - 1:
            print("*", end="")
        else:
            print(" ", end="")
    # Sau khi in xong một hàng thì xuống dòng
    print()
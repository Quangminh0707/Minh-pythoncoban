luong = float(input("Nhập tiền lương của bạn (triệu đồng) : "))
if luong > 15 :
    thue = luong * 30/100
elif 7 <= luong <= 15:
    thue = luong * 20/100
else:
    thue = luong * 10/100
print("Số tiền thuế thu nhập mà bạn phải đống là : ",thue," triệu đồng" )
#Baitap

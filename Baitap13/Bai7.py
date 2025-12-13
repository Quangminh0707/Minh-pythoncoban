nam = int(input("Nhập vào năm bạn muốn kiểm tra : "))
if nam %4 == 0 and nam % 100 !=0 :
    print("Đây là năm nhuận") 
elif nam %100==0 and nam % 400==0:
    print("Đây là năm nhuận")
else: 
    print("Năm đó không phải là năm nhuận!")

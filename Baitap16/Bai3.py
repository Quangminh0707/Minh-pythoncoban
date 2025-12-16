doanhso = float(input("Nhập vào doanh thu cua bạn (triệu đồng) : "))
if doanhso <= 100 :
    hoahong = doanhso*5/100
elif doanhso <= 300:
    hoahong = doanhso*10/100
else : 
    hoahong = doanhso*20/100
print("SỐ TIỀN HOA HỒNG MÀ BẠN NHẬN ĐƯỢC LÀ : ", hoahong)
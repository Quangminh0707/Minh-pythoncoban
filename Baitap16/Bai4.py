a = float(input("Nhập vào số phút mà bạn đã gọi để tính cước phí : "))
phicodinh= 25000
muc1 = a * 600
muc2 = muc1 + (a*400)
muc3 = muc1 +muc2 + (a*200)
if a <= 50 : 
    print("Số cước phí mà bạn phải trả là a : ",muc1 + phicodinh)
elif 50 < a <= 200 : 
    print("Số cước phí mà bạn phải trả là " , muc2+phicodinh)
else : 
    print("Số cước phí mà bạn phải trả là : ",muc3 +phicodinh)
import random 
a = random.randint(0,10)
solan = 1 
toida = 3
while solan <= toida : 
    doan = int(input("Đoán một số từ 0 đến 10 : "))
    solan += 1
    if doan == a:
        print("Chúc mừng bạn đã đoán đúng !")
        break
    else : 
        if solan < toida :
            print("Sai rồi! Gợi ý: Số bí mật lớn hơn số bạn đoán.")
        else:
            print("Sai rồi! Gợi ý: Số bí mật nhỏ hơn số bạn đoán.")
else : 
    print("Rất tiêc bạn đã hết lượt đoán rồi I_I . Số đúng là ",a)
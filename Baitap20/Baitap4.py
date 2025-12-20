import random 
a = random.randint(1,100)
solan = 0 
toida = 7
while solan <= toida : 
    doan = int(input("Đoán một số từ 1 đến 100 : "))
    solan += 1
    if doan == a:
        print("Chúc mừng bạn đã đoán đúng !")
        break
    else : 
         print("Bạn đoán sai rồi . Thử lần nữa nhé !!")
else : 
    print("Rất tiêc bạn đã hết lượt đoán rồi I_I . Số đúng là ",a)
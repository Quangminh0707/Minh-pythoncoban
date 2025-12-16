a = int(input("Nhập vào số nguyên mà bạn muốn kiểm tra : "))
if a % 3 == 0 :
    if a%5 == 0 :
        print("FIZZ-BUZZ")
    else :
        print("FIZZ")
elif a % 5 == 0 :
    print("BUZZ")
else : 
    print("Số bạn đưa ra không thuộc trường hợp nào !!!")
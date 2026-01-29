n = int(input("Nhập vào một số nguyên dương : "))
print("các số chia hết cho 3 từ 0 đến",n,"là : ")
i = 0 
while i <= n :
    if i % 3 == 0 :
        print(i)
    i +=1
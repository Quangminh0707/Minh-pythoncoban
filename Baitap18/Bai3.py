n = int(input("Nhập vào số nguyên : "))
print("Các ước của số",n,"là : ")
for i in range (1,n+1):
    if n % i == 0 :
        print(i)
listNumbers = []
for i in range (10):
    so = int(input(f"Nhập vào số nguyên thứ {i + 1} :  "))
    listNumbers.append(so)
tong = 0 
for x in listNumbers:
    if x > 10 :
        tong += x 
print(tong)
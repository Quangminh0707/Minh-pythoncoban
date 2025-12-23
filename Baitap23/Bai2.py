import math
n = int(input("Nhập một số nguyên dương: "))
if n < 2:
    print(n," không phải là số nguyên tố")
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(n," không phải là số nguyên tố")
            break
    else:
        print(n," là số nguyên tố")
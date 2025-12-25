a = int(input("Nhập vào số a : "))
b = int(input("Nhập vào số b : "))

tong_a = 0
for i in range(1, a):
    if a % i == 0:
        tong_a += i
tong_b = 0
for i in range(1, b):
    if b % i == 0:
        tong_b += i
if tong_a == b and tong_b == a:
    print(f"{a} và {b} là cặp số thân thiết")
else:
    print(f"{a} và {b} không phải là cặp số thân thiết")
import math

def chu_vi(r):
    return 2 * math.pi * r

def dien_tich(r):
    return math.pi * r ** 2

r = float(input("Nhập vào bán kính hình tròn : "))
print(chu_vi(r))
print(dien_tich(r))
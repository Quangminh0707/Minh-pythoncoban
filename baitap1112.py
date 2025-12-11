#Bài 1
a = int(input("Nhập vào số nguyên a : "))
b = int(input("Nhập vào số nguyên b : "))
bt = a**b
print("Kết quả biểu thức là :",bt)
# Bài 2
import math

r = float(input("Nhập vào bán kính của hình tròn : "))
C = 2*r*math.pi
S = math.pi*r*r
print("Chu vi của hình tròn là: ", C,"Diện tích của hình tròn là:", S)
# Bài 3 
ts = float(input("Nhập vào tử số a = "))
ms = float(input("NHập vào mẫu số b = ")) 
x = ts/ms
print("Bạn đã nhập phân số a/b có kết quả đổi ra số thực = ",x)
#Bài 4 
do = int(input("Nhập vào độ °F để tiến hành chuyển sang độ °C : "))
F = (do*1.8)+32
print("Kết quả là : ",F)
# Bài 5
so = int(input("Nhập số nguyên cần chuyển đổi : "))
chuoi = str(so)
m = float(so)
boo = bool(so)
print("sau khi chuyển đổi thì ta cacsoos theo thứ tự là chuỗi,số thực,đúng sai : ",chuoi,m,boo)
#Bài 6 
so1 = int(input("Nhập vào số nguyên có ba chữ số: "))
tong = (so1//100)+((so1//10)%10)+(so1%10)
print("Tổng của ba chữ số bạn đã đưa vào là ",tong)
#Bài 7
n = int(input("Nhập số a : "))
j = int(input("Nhập số b : "))
n,j=j,n
print(n,j)
#Bài 8
income = float(input('Nhập sô tiền cần gửi : '))
year = int(input("Nhập số năm cần gửi : "))
laisuat = int(input("Nhập vào phần trăm lãi suất : "))
Tong_tien = income + (1 + laisuat/100)**year
Tien_lai = Tong_tien - income 
print("Tổng tiền bạn có sau số năm bạn gửi tiền vào ngân hàng là :",Tong_tien)
print("Tiền lãi bạn nhận được sau số năm bạn gửi tiền là : ",Tien_lai)

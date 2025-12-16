print("Phương trình bậc 2 có dạng : ax^2 + bx + c = 0")
import math
a = float(input("Nhập vào biến a : "))
b = float(input("Nhập vào biến b : "))
c = float(input("Nhập vào biến c : "))
delta= b**2 - 4*a*c
if a == 0 : 
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else: 
            print("Nghiệm của phương trình là : ",-c/b)
else:
    if delta < 0 :
        print("Phương trình vô nghiệm !")
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép x1=x2=",x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Nghiệm thứ nhất là : ",x1)
        print("Nghiệm thứ hai là : ",x2)
        
    
 





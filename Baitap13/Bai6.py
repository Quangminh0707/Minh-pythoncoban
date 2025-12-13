height = float(input("Nhập chiều cao của bạn(cm) : "))
weight = float(input("Nhập cân nặng của bạn(kg) : "))
heights = height/100
bmi = weight/(heights**2)
if bmi<18.5:
    print("Bạn đang bị thiếu cân ")
elif 18.5 <= bmi <= 25.0:
    print(" Bạn đang có cân nặng bình thường")

elif 25.0 <= bmi < 30.0:
    print("Bạn đang bị thừa cân ")
else:
    print("Bạn đang bị béo phì !!!")
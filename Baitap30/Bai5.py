def tim_min(a,b,c):
    gtnn = a 
    if b < gtnn : gtnn = b
    if c < gtnn : gtnn = c
    return gtnn 
a = int(input("Nhập vào số a : "))
b = int(input("Nhập vào số b : "))
c = int(input("Nhập vào số c : "))
print(tim_min(a,b,c))
listNumbers = []
for i in range (10):
    so = int(input(f"Nhập vào số nguyên thứ {i + 1} :  "))
    listNumbers.append(so)
solonhon5 = [] 
for x in listNumbers :
    if x > 5 : 
        solonhon5.append(x)
dem = len(solonhon5)
print("Các sốm lớn hơn 5 là : ",*solonhon5)
print(f"Vậy có {dem} số lớn hơn 5")
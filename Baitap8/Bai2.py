listNumbers = []
for i in range (10):
    so = int(input(f"Nhập vào số nguyên thứ {i + 1} :  "))
    listNumbers.append(so)
GTLN = max(listNumbers)
Vitri = listNumbers.index(GTLN)
print("Giá trị lớn nhất trong 10 số đã cho là : ",GTLN) 
print("Vị trí của số đó trong danh sách là : ",Vitri+1)

a = input("Nhập vào tên của bạn : ")
b = input("Nhập vào ký tự bạn muốn tìm trong tên : ")
tontai =  False 
for i in a :
    if i == b :
        tontai = True
        break
if tontai:
    print(b,"có xuất hiện trong tên!")
else:
    print(b,"không xuất hiện trong tên!")
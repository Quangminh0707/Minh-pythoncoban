def tong_chan(n):
    s = 0
    for i in range(0, n + 1, 2):
        s += i
    return s

n = int(input('Nhập vào số nguyên : '))
print("Tổng các số chẵn từ 0 đến {n} là: ",tong_chan(n))
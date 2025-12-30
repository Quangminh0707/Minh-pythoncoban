def giai_thua(n):
    if n < 0:
        return "Giai thừa không xác định cho số âm"
    elif n == 0:
        return 1
    else:
        a = 1
        for i in range(1, n + 1):
            a *= i  
        return a
n = int(input("nhập vào số nguyên : "))
print(giai_thua(n))
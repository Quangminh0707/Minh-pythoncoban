def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập n: "))
print(f"Các số nguyên tố từ 1 đến {n} là:", end=" ")

for i in range(1, n + 1):
    if snt(i):
        print(i, end=" ")
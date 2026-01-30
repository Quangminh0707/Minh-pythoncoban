import number_utils
n = int(input("Nhập một số: "))
print(f"Số chẵn: {number_utils.is_even(n)}")
print(f"Số lẻ: {number_utils.is_odd(n)}")
print(f"Số nguyên tố: {number_utils.is_prime(n)}")
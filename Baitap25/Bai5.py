import random
password = str(random.randint(100, 999)) 

found = False
for i in range(10):
    if found: break
    for j in range(10):
        if found: break
        for k in range(10):
            a = str(i) + str(j) + str(k)
            print("Thử: " + a)
            if a == password:
                print("Password found: " + a)
                found = True
                break
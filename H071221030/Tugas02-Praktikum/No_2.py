a = str(input("golongan = "))
b = int(input("daya = "))
c = float(input("Pemakaian = "))

if a == "R1":
    if b == 900:
        d = 1352*c
        print("> jumlah tagihan anda :", d)
    elif b == 1300:
        d = 1444.70*c        
        print("> jumlah tagihan anda :", d)
    elif b == 2200:
        d = 1444.70*c        
        print("> jumlah tagihan anda :", d)
    else :
        print("> data tidak valid")
elif a == "R2":
    if b>=3500 and b<=5500:
        d = 1699.53*c
        print("> jumlah tagihan anda :", d)
    else :
        print("> data tidak valid")
elif a == "R3":
    if b>=6600:
        d = 1699.53*c
        print("> jumlah tagihan anda :", d)
    else :
        print("> data tidak valid")
elif a == "B2":
    if b>=6600 and b<=200000:
        d = 1444.70*c
        print("> jumlah tagihan anda :", d)
    else :
         print("> data tidak valid")
elif a == "B3":
    if b>200000:
        d = 1114.74*c
        print("> jumlah tagihan anda :", d)
    else :
         print("> data tidak valid")
elif a == "I3":
    if b>=200000:
        d = 1314.12*c
        print("> jumlah tagihan anda :", d)
    else :
         print("> data tidak valid")
elif a == "P1":
    if b>=6600 and b<=200000:
        d = 1523.28*c
        print("> jumlah tagihan anda :", d)
    else :
         print("> data tidak valid")
else :
    print("> data tidak valid")
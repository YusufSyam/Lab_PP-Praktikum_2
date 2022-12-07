bil1 = int(input("Masukkan bilangan 1: "))
bil2 = int(input("Masukkan bilangan 2: "))

def hitung_fpb(x, y):
    if x > y:
        terkecil = y
    else:
        terkecil = x

    for i in range (1, terkecil+1):
        if ((x % i == 0) and (y % i == 0)):
         fpb = i 
    return fpb

print ("FPB", (bil1, bil2), "=", hitung_fpb(bil1, bil2))
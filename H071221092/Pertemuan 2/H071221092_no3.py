a, b, c, d, e= input().split(" ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)

except:
    print("Inputan Tidak Valid")

else:
    genap   = 0
    ganjil  = 0
    positif = 0
    negatif = 0

    for i in [a, b, c, d, e]:

        if i > 0:
            positif+=1
        elif i < 0:
            negatif+=1
        if i%2==0:
            genap+=1
        else:
            ganjil+=1

    print(genap,"Angka Genap")
    print(ganjil,"Angka Ganjil")
    print(positif,"Angka Positif")
    print(negatif,"Angka Negatif")

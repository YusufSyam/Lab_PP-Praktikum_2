from math import floor


a = int(input("a : "))
b = int(input("b : "))
c = int(b-a)

cepek = 0
gocap = 0
jicap = 0
cap = 0
goceng = 0
noceng = 0
seceng = 0

if c <= 0 :
    print("Tidak ada kembalian")
else :
    while c >= 100000 :
        d = floor(c/100000)
        cepek = cepek + d
        c = c%100000
    while c >= 50000 :
        d = floor(c/50000)
        gocap = gocap + d
        c = c%50000
    while c >= 20000 :
        d = floor(c/20000)
        jicap = jicap + d
        c = c%20000
    while c >= 10000 :
        d = floor(c/10000)
        cap = cap + d
        c = c%10000
    while c >= 5000 :
        d = floor(c/5000)
        goceng = goceng + d
        c = c%5000
    while c >= 2000 :
        d = floor(c/2000)
        noceng = noceng + d
        c = c%2000
    while c >= 1000 :
        d = floor(c/1000)
        seceng = seceng + d
        c = c%1000
    print(cepek, "uang Rp. 100.000")
    print(gocap, "uang Rp. 50.000")
    print(jicap, "uang Rp. 20.000")
    print(cap, "uang Rp. 10.000")
    print(goceng, "uang Rp. 5.000")
    print(noceng, "uang Rp. 2.000")
    print(seceng, "uang Rp. 1.000")
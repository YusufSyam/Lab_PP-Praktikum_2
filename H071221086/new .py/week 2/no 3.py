import sys
ganjil = 0
genap = 0
positif = 0
negatif = 0

a,b,c,d,e = input('masukkan angka: ').split()

if not a.isnumeric():
    if a[0] == '-' and len(a) > 1:
        negatif+=1
    else:
        sys.exix('inputan tidak valid')
a = int(a)
if a % 2 == 0 or a == 0:
    genap+=1
elif a % 2 != 0:
    ganjil+=1
else:
    print('inputan tidak valid')

if a > 0:
    positif+=1

if not b.isnumeric():
    if b[0] == '-' and len(b) > 1:
        negatif+=1
    else:
        sys.exit('inputan tidak valid')
b = int(b)
if b % 2 == 0 or b == 0:
    genap+=1
else:
    ganjil+=1

if b > 0:
    positif+=1

if not c.isnumeric():
    if c[0] == '-' and len (c) > 1:
        negatif+=1
    else:
        sys.exit('inputan tidak valid')
c=int(c)
if c % 2 == 0 or c == 0:
    genap+=1
else:
    ganjil+=1

if c > 0:
    positif +=1

if not d.isnumeric():
    if d[0] == '-' and len (d) > 1:
        negatif+=1
    else:
        sys.exit ('inputan tidak valid')
d=int(d)
if d % 2 == 0 or d == 0:
    genap+=1
else:
    ganjil+=1

if d > 0:
    positif +=1

if not e.isnumeric():
    if e[0] == '-' and len (e) > 1:
        negatif+=1
    else:
        sys.exit ('inputan tidak valid')
e=int(e)
if e % 2 == 0 or e == 0:
    genap+=1
else:
    ganjil+=1

if e > 0:
    positif +=1

print(genap,'angka genap')
print(ganjil,'angka ganjil')
print(positif,'angka positif')
print(negatif,'angka negatif')


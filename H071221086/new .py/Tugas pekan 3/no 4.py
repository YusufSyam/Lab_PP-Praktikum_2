x = int(input('awal: '))
y = int(input('akhir: '))

for x in range(x, y+1):
    if x==0:
        print('nol')
    elif x%2==0 and x<0:
        print(x, 'genap negatif')
    elif x%2!=0 and x>0:
        print(x, 'genap positif')
    elif x%2!=0 and x<0:
        print(x, 'ganjil negatif')
    elif x%2!=0 and x>0:
        print(x, 'ganjil positif')
    elif y==0:
        print('nol')
    elif y%2==0 and y<0:
        print(y, 'genap negatif')
    elif y%2==0 and y>0:
        print(y, 'genap positif')
    elif y%2!=0 and y<0:
        print(y, 'ganjil negatif')
    elif y%2!=0 and y>0:
        print(y, 'ganjil positif')
        
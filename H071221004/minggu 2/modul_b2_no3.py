angka = input().split(" ")

try:
    angka = [int(int_angka) for int_angka in angka]
except:
    print('Inputan Tidak Valid')
else:
    genap=0
    ganjil=0
    positif=0
    negatif=0

    for i in angka:
    

        if i>0:
            positif +=1
        elif i<0:
            negatif +=1

        if i%2==0:
            genap+=1
        elif i%2==1:
            ganjil +=1


    print(genap, 'Angka Genap')
    print(ganjil, 'Angka Ganjil')
    print(positif, 'Angka Positif')
    print(negatif,'Angka Negatif')



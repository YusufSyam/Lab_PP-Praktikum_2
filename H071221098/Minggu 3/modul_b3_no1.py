kolom = int(input())
jumlah_angka = int(input())
baris = jumlah_angka//kolom

for i in range(baris): 
    for j in range(kolom):
        print((i*kolom)+j+1,end=' ')

    print()
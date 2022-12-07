file = input()
jumlah = int(input())

nama = []
nim = []
angkatan = []

for i in range(jumlah): #perulangan untuk isi biodata sebanyak jumlah yang kita mau
    isi_nama = input('masukkan nama: ').replace(' ','_')
    if len(isi_nama) <= 20:
        nama.append(isi_nama)
    else:
        print('gagal')
        exit()
    isi_nim = input('masukkan nim: ')
    nim.append(isi_nim)
    isi_angkatan = input('masukkan angkatan: ')
    angkatan.append(isi_angkatan)

#if len(isi_nama) <= 20:
    with open(f"{file}.txt","w") as f:
        nama_terpanjang = nama[0]
        #mencari nama yang terpanjang
        for panjang in nama:
            if len(panjang) > len(nama_terpanjang): 
                nama_terpanjang = panjang

        #baris pertama atau paling atas dari tabel
        f.write('+-'+('-'*len(nama_terpanjang))+'-+')
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        #baris kedua untuk kolom format nama. nim, angkatan
        f.write('\n| nama'+(' '*(len(nama_terpanjang)-5))+' |')
        f.write(' nim'+(' '*(12-4))+'|')
        f.write(' angkatan'+(' '*(10-9))+'|')

        #baris ketiga batas antara format dan isi
        f.write('\n+-'+('-'*len(nama_terpanjang))+'-+')
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        #baris selanjutnya isi sesuai banyak data yang di input
        for x in range(jumlah):
            f.write('\n| ')
            f.write(nama[0])
            f.write(' '*(len(nama_terpanjang)-len(nama[0]))+' | ')
            f.write(nim[0])
            f.write(' '*(11-len(nim[0]))+'|')
            f.write(angkatan[0])
            f.write((' '*(9 - len(angkatan[0])))+'|')
        #baris paling akhir sebagai penutup
        f.write('\n+-'+('-'*len(nama_terpanjang))+'-+')
        f.write(('-'*12)+'+')
        f.write(('-'*10)+'+')

        print("berhasil")
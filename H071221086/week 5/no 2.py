print('Selamat datang untuk memulai, silahkan input data anda')
nama = input('input nama: ')
umur = int(input('input umur: '))
alamat = input('input alamat: ')
while True:
    print('==========================================================')
    print(f'Selamat datang {nama} seilahkan pilih opsi')
    print('==========================================================')
    print('1. Detail anda')
    print('2. Ubah nama')
    print('3. Ubah umur')
    print('4. Ubah alamat')
    print('5. Keluar')
    print('==========================================================')
    opsi = int(input('input opsi: '))
    print('==========================================================')
    if opsi == 1:
        print ('Data anda salah')
        print (f'Nama: {nama}')
        print (f'Umur: {umur}')
        print (f'Alamat: {alamat}')
    elif opsi == 2:
        nama = input('silahkan input nama baru: ')
        print('data anda sukses diperbarui')
    elif opsi == 3:
        umur = input('silahkan input umur baru: ')
        print('data anda sukses diperbarui')
    elif opsi == 4:
        alamat = input('silahkan input alamat baru: ')
        print('data anda sukses diperbarui')
    elif opsi == 5:
       print('==========================================================')
       print(f'Selamat Tinggal {nama}')
       exit()
    else: 
        print('Inputan Salah')
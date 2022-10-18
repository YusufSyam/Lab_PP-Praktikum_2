print("=" * 60)
print("    Selamat Datang untuk Memulai Silahkan Input Data Anda      ")
print("=" * 60)

nama = input("Input nama : ")
umur = input("Input umur : ")
alamat = input("Input Alamat : ")

print("=" * 60)
print(f"          Selamat Datang {nama} Silahkan Pilih Opsi       ")

def opsi():
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur" )
    print("4. Ubah Alamat")
    print("5. Keluar")
print("=" * 60)

while True:
    opsi()
    print("=" * 60)
    pilihan = int(input("Input Opsi : "))
    print("=" * 60)
    if pilihan == 1:
        print( f" Nama  : {nama} ")
        print(f" Umur   : {umur} ")
        print(f" Alamat : {alamat} ")
    elif pilihan == 2:
        nama = input("Silahkan Input Nama Baru : ")
        print("Data Anda Sukses Diperbarui")
    elif pilihan == 3:
        umur = input('Silahkan Input Umur Baru : ' )
        print("Data Anda Sukses Diperbarui")
    elif pilihan == 4:
        alamat = input("Silahkan Input Alamat Baru : ")
        print("Data Anda Sukses Diperbarui")
    elif pilihan == 5:
        print(f'                    Selamat Tinggal {nama}              ')
        break
    else: 
        print('Opsi Salah')




    




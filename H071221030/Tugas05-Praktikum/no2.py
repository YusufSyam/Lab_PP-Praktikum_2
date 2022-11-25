print("Selamat datang untuk memulai silahkan input data anda")
nama = str(input("Input nama: "))
umur = int(input("Input umur: "))
alamat = str(input("Input alamat: "))

while True :
    print("==================================================")
    print(f"Selamat datang {nama} silahkan pilih opsi")
    print("==================================================")
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("==================================================")
    opsi = int(input("Input opsi: "))
    if opsi == 1 :
        print("==================================================")
        print("Data anda adalah")
        print(f"Nama: {nama}")
        print(f"Umur: {umur}")
        print(f"Alamat: {alamat}")
    elif opsi == 2 :
        nama = str(input("Silahkan Input nama baru: "))
        print("Data anda sukses di diperbarui")
    elif opsi == 3 :
        umur = int(input("Silahkan Input umur baru: "))
        print("Data anda sukses di diperbarui")
    elif opsi == 4 :
        alamat = str(input("Silahkan Input alamat baru: "))
        print("Data anda sukses di diperbarui")
    elif opsi == 5 :
        print("==================================================")
        print(f"Selamat Tinggal {nama}")
        break
print ("Selamat datang untuk memulai silahkan input data")

nama   = input("Input nama: ")
umur   = input("Input umur: ")
alamat = input("input alamat: ")

data   = {
    "Nama"   : nama,
    "Umur"   : umur,
    "Alamat" : alamat,
}

while True:  
    print ("========================")
    print (f"selamat datang {nama}, Pilih Opsi")
    print ("========================")
    print ("1. Detail Anda")
    print ("2. Ubah nama")
    print ("3. Ubah umur")
    print ("4. ubah alamat")
    print ("5. Keluar")
    print ("========================")
    opsi= int(input("input opsi: "))

    print ("========================")
    if opsi == 1:
        print ("Data anda adalah")
        print ("Nama: ", data["Nama"])
        print ("Umur: ", data["Umur"])
        print ("Alamat: ", data ["Alamat"])
    elif opsi == 2:
        nama = input('Silahkan input data nama baru: ')
        data['Nama'] = nama
        print('Data anda sukses diperbaharui')
    elif opsi == 3:
        umur = int(input('Silahkan input data umur baru: '))
        data['Umur'] = umur
        print('Data anda sukses diperbaharui')
    elif opsi == 4:
        alamat = input('Silahkan input data alamat baru: ')
        data['Alamat'] = alamat
        print('Data anda sukses diperbaharui')
    elif opsi == 5:
        print(f'Selamat tinggal {nama}')
        break
    else:
        print('Opsi salah, masukkan ulang opsi yang benar!')
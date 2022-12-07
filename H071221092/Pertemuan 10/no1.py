import re
import os

def menu():
    print('=' * 50)
    print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
    print('1. Detail Anda')
    print('2. Ubah Nama')
    print('3. Jumlah Data pada File')
    print('4. Save Data pada File')
    print('5. Buat Data Baru')
    print('6. Keluar')
    print('=' * 50)

data = None

while True:
    menu()
    opsi = input("Silahkan Pilih Opsi Anda : ")

    try:
        opsi = int(opsi)
    except:
        print("Inputan salah")
    else:
        match opsi:
            case 1:
                if data == None:
                    print('=' * 50)
                    print('Data Saat Ini Kosong')
                else:
                    print('=' * 50)
                    print('Nama :', data['Nama'])
                    print('Email :', data['Email'])
                    print('Password :', data['Password'])
            case 2:
                if data == None:
                    print('=' * 50)
                    print('Data Saat Ini Kosong')
                else:
                    print('=' * 50)
                    data['Nama'] = input("Silahkan Input Nama Baru : ")
            case 3:
                print('=' * 50)
                banyak_baris = 0
                file = input("Silahkan Masukkan Nama File : ") + '.txt'
                print("Berhasil")
                try:
                    with open(file) as baca:
                        data_file = re.findall(fr"@student\.unhas\.ac\.id", baca.read())
                        print(f"Jumlah Data Adalah : {data_file.count('@student.unhas.ac.id')}")
                except:
                    print("Tidak Terdapat File dengan nama " + file)
                    print("Jumlah Data Pada File : 0 Data")
            case 4:
                if data == None:
                    print('=' * 50)
                    print('Data Saat Ini Kosong')
                else:
                    print('=' * 50)
                    file_name = input(
                        "Silahkan Masukkan Nama File : ") + '.txt'
                    try:
                    
                        if os.path.exists(file_name):
                            with open(file_name, 'a') as file:
                                file.write(f"\n|Nama\t\t: {data['Nama']}\n")
                                file.write(f"|Email\t\t: {data['Email']}\n")
                                file.write(f"|Password\t: {data['Password']}\n")
                                file.write(f"=" * 60)
                        else:
                            with open(file_name, 'x') as file:
                                file.write("=" * 60)
                                file.write(f"\n|Data Yang Tersimpan|\n")
                                file.write("=" * 75)
                                file.write(f"\n|Nama\t\t: {data['Nama']}\n")
                                file.write(f"|Email\t\t: {data['Email']}\n")
                                file.write(f"|Password\t: {data['Password']}\n")
                                file.write("=" * 60)
                        data = None
                        print("Berhasil")
                    except:
                        print("Gagal")

            case 5:
                data = {
                    "Nama": "",
                    "Email": "",
                    "Password": ""
                }
                print('=' * 50)
                data["Nama"] = input("Silahkan Masukkan Nama Anda  : ")
                while True:
                    email = input("Silahkan Masukkan Email Anda : ")
                    if re.fullmatch("^[a-z0-9]{1,}(@student\.unhas\.ac\.id$)", (email)):
                        data["Email"] = email
                        break
                    else:
                        print('=' * 50)
                        print("Email Yang Anda Masukkan Salah")
                        print('=' * 50)
                while True:
                    password = input("Silahkan Masukkan Password Anda : ")
                    if re.fullmatch(".{8,20}", (password)):
                        if re.findall("[A-Z]+", (password)) and re.findall("[a-z]+", (password)) and re.findall("[0-9]+", (password)):
                            data["Password"] = password
                            break
                        else:
                            print('=' * 50)
                            print("Password yang anda masukkan terlalu lemah")
                            print(
                                "Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                            print('=' * 50)
                    else:
                        print('=' * 50)
                        print("Password Harus Memiliki Panjang 8-20 Karakter")
                        print('=' * 50)
            case 6:
                print('=' * 50)
                print('Sampai Jumpa Lagi')
                break
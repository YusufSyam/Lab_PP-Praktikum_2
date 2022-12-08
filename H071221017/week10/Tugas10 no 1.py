import re
nama = []
email = []
password = []

while True :
    print("="*50)
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Jumlah Data pada File")
    print("4. Save Data pada File")
    print("5. Buat Data Baru")
    print("6. Keluar")
    pilihan = input("Silahkan Pilih Opsi Anda : ")

    try :
        pilihan = int(pilihan)
    except : 
        print("="*50)
        print("Pilihan tidak tersedia")
    else :

        if pilihan == 1 :
            if len(nama) == 0 :
                print("Data saat ini kosong")
            else :
                print("="*50)
                print("Data anda adalah : ")
                for i in range(len(nama)):
                    print(f"Nama : {nama[i]}")
                    print(f"Email : {email[i]}")
                    print(f"Password : {password[i]}")
                    print()

        elif pilihan == 2 :
            if len(nama) == 0 :
                print("Data saat ini kosong")
            else :
                print("="*50)
                i = int(input("Pilih Data : ")) ; i = i-1
                nama[i] = str(input("Silahkan Input Nama Baru : "))

        elif pilihan == 3 :
            name = str(input("Silahkan Masukkan Nama File : ")) ; name = name + ".txt"
            try :
                with open(name, "r") as done:
                    done.read()
            except :
                print(f"Tidak Terdapat File dengan Nama {name}")
            else :
                with open(name, "r") as done :
                    x = done.readlines()
                    x = len(x) - 3 - (2*len(nama))
                    print(f"Jumlah Data Pada File : {x} Data")

        elif pilihan == 4 :
            if len(nama) == 0 :
                print("Data saat ini kosong")
            else :
                name = str(input("Silahkan Masukkan Nama File : ")) ; name = name + ".txt"
                try :
                    with open(name, "r") as done:
                        done.read()
                except :
                    with open(name , "w") as nope :
                        nope.write("+")
                        nope.write("="*100)
                        nope.write("\n|Data yang Tersimpan\n")
                        nope.write("+")
                        nope.write("="*100)
                        for i in range(len(nama)):
                            nope.write("\n|Nama")
                            nope.write(" "*12)
                            nope.write(": ")
                            nope.write(nama[i])
                            nope.write("\n|Email")
                            nope.write(" "*11)
                            nope.write(": ")
                            nope.write(email[i])
                            nope.write("\n|Password")
                            nope.write(" "*8)
                            nope.write(": ")
                            nope.write(password[i])
                            nope.write("\n+")
                            nope.write("="*100)
                else :
                    with open(name, "r+") as done :
                        for i in range(len(nama)):
                            done.write("\n|Nama")
                            done.write(" "*12)
                            done.write(": ")
                            done.write(nama[i])
                            done.write("\n|Email")
                            done.write(" "*11)
                            done.write(": ")
                            done.write(email[i])
                            done.write("\n|Password")
                            done.write(" "*8)
                            done.write(": ")
                            done.write(password[i])
                            done.write("\n+")
                            done.write("="*100)
                print("Berhasil")

        elif pilihan ==  5 :
            print("="*50)
            name = str(input("Silahkan Masukkan Nama Anda : ")) ; nama.append(name)
            while True :
                adress = str(input("Silahkan Masukkan Email Anda : "))
                adress1 = "[a-z0-9]+@student\.unhas\.ac\.id"
                rege = re.findall(adress1, adress)
                if rege :
                    email.append(adress)
                    while True :
                        sandi = str(input("Silahkan Masukkan Password Anda : "))
                        if 8 <= len(sandi) <= 20 :
                            sandi1 = "[A-Z]+[a-z]+[0-9]"
                            regp = re.match(sandi1, sandi)
                            if regp :
                                password.append(sandi)
                                break
                            else :
                                print("="*50)
                                print("Password Yang anda masukkan terlalu lemah")
                                print("Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                                print("="*50)
                        else :
                            print("="*50)
                            print("Password Harus Memiliki Panjang 8-20")
                            print("="*50)
                    break
                else :
                    print("="*50)
                    print("Email yang anda masukkan salah")
                    print("="*50)

        elif pilihan == 6 :
            print("="*50)
            print("Sampai jumpa lagi")
            break
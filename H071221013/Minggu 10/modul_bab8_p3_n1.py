print("\nSelamat datang untuk memulai silahkan input data anda")

# nama = input("Input Nama : ")
data= []

def menu():
    print("=" * 50)
    print("   selamat datang silahkan pilih opsi menu anda     ")
    print("=" * 50)
menu()

i = 1
while i > 0 :
    print('1. Detail Anda')
    print('2. Ubah Nama')
    print('3. Jumlah Data pada File')
    print('4. Save Data pada File')
    print('5. Buat Data Baru')
    print('6. Keluar')

    print("=" * 50)
    a= input("          silahkan pilih opsi anda : ")
    print(50*'=')

    try :
        a = int(a)

    except :
        print("inputan salah")

    else :
        if a == 1:
            if len(data)== 0:
                print('Data saat ini kosong')
            else:
                print("data anda adalah")
                print('='* 50)
                
                for detail in data:
                    print(f'nama : {detail["nama"]}')
                    print(f'email : {detail["email"]}')
                    print(f'password : {detail["password"]}')
                    print(50*'=')


        elif a == 2:
            if len(data)== 0:
                print('Data saat ini kosong')
                print('=' * 50)
            else:
                print('=' * 50)
                newName= input("silahkan input nama baru : ")
                data[-1]["nama"] = newName

        elif a == 3:
            nama_file= input("Masukkan Nama File: ") + ".txt"

            with open(f"{nama_file}", "r") as file:
                x = file.read()
                print("Berhasil")
                print("Jumlah Data Pada File : ", x.count("Nama"))
                print('=' * 50)


        elif a == 4:
            if len(data)== 0:
                print("Data Saat Ini Kosong")
                print('=' * 50)
            else:
                print('=' * 50)

                file= input("Masukkan nama file : ") + ".txt"
                print("Berhasil")
                print('=' * 50)

                with open(file, "w") as file:
                    file.write("+" + "="*50 + "+\n")
                    file.write("|" + "Data Yang Tersimpan" + "\n")
                    file.write("+" + "="*50 + "+\n")

                    for detail in data:
                        file.write("| Nama \t\t\t: " + detail["nama"] +"\n")
                        file.write("| Email \t\t\t: " + detail["email"] + "\n")
                        file.write("| Password \t\t: " + detail["password"] + "\n")
                        file.write("+" + "="*50 + "+\n")


        elif a == 5:
            print("Data anda adalah")
            print('=' * 50)
            nama= input("silahkan masukkan nama anda : ")
            detail= {}
            detail['nama']= nama
            email= input("silahkan masukkan email anda : ")
            detail['email']= email
            password= input("silahkan masukkan password anda : ")
            detail['password']= password
            print('=' * 50)



            data.append(detail)

        if a == 6:
            print("Sampai Jumpa")
            print('=' * 50)
            break
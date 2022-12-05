print("\nSelamat datang untuk memulai silahkan input data anda")

data= []

def menu():
    print(50*'=')
    print(" selamat datang silahkan pilih opsi menu anda")
    print(50*'=')
menu()

i = 1
while i > 0 :
    print('1. Detail Anda')
    print('2. Ubah Nama')
    print('3. Jumlah Data pada File')
    print('4. Save Data pada File')
    print('5. Buat Data Baru')
    print('6. Keluar')

    print(50*'=')
    a= input("silahkan pilih opsi anda : ")
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
                print(50*'=')
                
                for detail in data:
                    print(f'nama : {detail["nama"]}')
                    print(f'email : {detail["email"]}')
                    print(f'password : {detail["password"]}')
                    print(50*'=')

        elif a == 2:
            if len(data)== 0:
                print('Data saat ini kosong')
            else:
                print(50*'=')
                newName= input("silahkan input nama baru : ")
                data[-1]["nama"]=newName

        elif a == 3:
            if len(x) == 0:
                print('tidak terdapat file')  
            else:        
                namaFile= input("masukkan nama file : ") + '.txt'
                with open(f"{namaFile}", 'r') as baca:
                    x= baca.read()
                    print("jumlah data pada file : ", x.count('Nama'))
                    print("berhasil")

        elif a == 4:
            if len(data)== 0:
                print('Data saat ini kosong')    
            else:
                print(50*'=')    
                namaFile= input("masukkan nama file baru: ")+".txt"
                with open(f'{namaFile}', 'w') as file:
                    file.write(f"+{'='*70}\n")
                    file.write(f"| Data yang Tersimpan\n")
                    file.write(f"+{'='*70}\n")
                    
                    for detail in data:
                        file.write(f"| Nama \t\t\t : {detail['nama']}\n")
                        file.write(f"| email \t\t : {detail['email']}\n")
                        file.write(f"| password \t\t : {detail['password']}\n")
                        file.write(f"+{'='*70}\n")

        elif a == 5:
            print("Data anda adalah")
            nama= input("silahkan masukkan nama anda : ")
            detail= {}
            detail['nama']= nama
            email= input("silahkan masukkan email anda : ")
            detail['email']= email
            password= input("silahkan masukkan password anda : ")
            detail['password']= password

            data.append(detail)

        if a == 6:
            print('sampai jumpa lagi')
            print(50*'=')
            break


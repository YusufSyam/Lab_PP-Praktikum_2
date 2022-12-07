def user () :
    global nama
    global age
    global alamat
    print ("Selamat datang untuk memulai silahkan input data anda")
    nama = input('nama:')
    age = input('umur:')
    alamat = input('alamat:')
def exit():
    print ("="*30)
    print (f"Selamat Tinggal {nama}")
    print ("="*30)
def detail ():
    print ("="*30)
    print ("Data anda adalah")
    print (f"Nama: {nama}")
    print (f"Umur: {age}")
    print (f"Alamat: {alamat}""")
    main ()
def ubah_nama() :
    global nama
    nama = input("Silahkan Input nama baru :")
    print ("Data anda sukses di diperbarui")
    main ()
def ubah_umur() :
    global age
    age = input("Silahkan Input umur baru :")
    print ("Data anda sukses di diperbarui")
    main ()
def ubah_alamat() :
    global alamat
    alamat = input("Silahkan Input alamat baru :")
    print ("Data anda sukses di diperbarui")
    main ()
def main ():
    print ("="*30)
    print (f"Selamat datang {nama} silahkan pilih opsi")
    print ("="*30)
    print ("""1. Detail anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar""")
    print ("="*30)
    pilih = ''
    opsi = [1,2,3,4,5]
    while pilih not in opsi:
        try :
            pilih = int(input("pilihan: "))
            print ("="*30)
            if pilih == 1 : detail()
            if pilih == 2 : ubah_nama()
            elif pilih == 3 : ubah_umur ()
            elif pilih == 4 : ubah_alamat ()
            elif pilih == 5 : exit ()
        except :
            print ("Pilihan anda tidak valid")
            print ("="*30)
user ()
main ()



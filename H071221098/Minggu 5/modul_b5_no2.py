def get_detail():
    global detail
    print("Data anda adalah")
    print("Nama:", detail["Nama"])
    print("Umur:", detail["Umur"])
    print("Alamat:", detail["Alamat"])

def ubah_nama():
    global detail
    detail["Nama"] = input("Silahkan input nama baru: ")
    print("Data anda sukses diperbarui")

def ubah_umur():
    global detail
    detail["Umur"] = input("Silahkan input umur baru: ")
    print("Data anda sukses diperbarui")

def ubah_alamat():
    global detail
    detail["Alamat"] = input("Silahkan input alamat baru: ")
    print("Data anda sukses diperbarui")

print("Selamat datang untuk memulai silahkan input data anda")

detail = {
       "Nama":  input("Input nama: "),
       "Umur": input("Input umur: "),
       "Alamat": input("Input alamat: ")
}

while True:
    print("==================================================")
    print("Selamat datang", detail["Nama"], "silahkan pilih opsi")
    print("==================================================")
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("==================================================")

    a = int(input("Input opsi: "))
    print("==================================================")

    if a == 1:
        get_detail()
    elif a == 2:
        ubah_nama()
    elif a == 3:
        ubah_umur()
    elif a == 4:
        ubah_alamat()
    elif a == 5:
        break
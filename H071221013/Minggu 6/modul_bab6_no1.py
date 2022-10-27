x = input("Masukkan nama file1 : ")
y = input("Masukkan nama file2 : ")

try:
    with open(x + ".txt", "r") as file:
        data = file.read()

    with open(y + ".txt", "w") as file:
        if (data != -1):
            file.write(data)

    print("Berhasil")
except:
    print("Gagal")
file = input("Masukkan Nama File : ") + ".txt"
x = int(input("Masukkan Jumlah Asisten: "))

file1 = open(file, "w+")

try:
    file1.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    file1.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    file1.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")

    for i in range(x):
        nama = input("Masukkan Nama Asisten : ")
        nim = input("Masukkan NIM Asisten : ")
        angkatan = str(input("Masukkan Angkatan Asisten : "))
        panjang_nama = len(nama)
        panjang_nim = len(nim)
        panjang_angkatan = len(angkatan)


        tulis = "| " + nama + (" " * (22 - panjang_nama -1) + "| " + nim + (" " * (12 - panjang_nim - 1) + "| " + angkatan + (" " * (10 - panjang_angkatan - 1)) + "|\n"))  
        
        file1.write(tulis)

    file1.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    file1.close()

except:
    print("Gagal")


    
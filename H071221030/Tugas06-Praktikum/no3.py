file = str(input("Nama file : ")) ; file = file + ".txt"
ass = int(input("Jumlah asisten : "))
nama = []
kelas = []
angkatan = []
for i in range(ass):
    print(f"Asisten ke-{i+1}")
    name = str(input("Nama : "))
    clas = str(input("NIM : "))
    year = str(input("Angkatan : "))
    nama.append(name)
    kelas.append(clas)
    angkatan.append(year)

try :
    with open(file, "w") as text :
        text.write("+----------------------+-----------+----------+\n")
        text.write("| Nama                 | NIM       | Angkatan |\n")
        text.write("+----------------------+-----------+----------+\n")
        for i in range(ass):
            if len(nama[i]) > 20 :
                print(nama[i][4000])
            else :
                text.write("| ")
                text.write(nama[i])
                text.write(" " * (21-(len(nama[i]))))
                text.write("| ")
                text.write(kelas[i])
                text.write(" " * (10-(len(kelas[i]))))
                text.write("| ")
                text.write(angkatan[i])
                text.write(" " * (9-(len(angkatan[i]))))
                text.write("|")
                text.write("\n")
        text.write("+----------------------+-----------+----------+\n")
except :
    print("\nGagal")
else :
    print("\nBerhasil")
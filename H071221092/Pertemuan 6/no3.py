a = input () + ".txt"
b = int (input ())

try:
    with open (a, "w") as file:
        tulis = ("""-----------------------------------------
|     nama     |   Nim   |   angkatan   |
-----------------------------------------""")
        for i in range (b):
            nama = input ("Nama : ").replace(" ", "_")
            Nim  = input("NIM  :")
            angkatan = input("Angkatan:")
            tulis += "\n| "+nama + " "*(14-len(nama))+"|"+Nim+ " "*(8-len(Nim))+"|"+angkatan+ " "*(14-len(angkatan))+"|"
        tulis += "\n-----------------------------------------"
        file.write (tulis)
except:
    print ('Tidak berhasil')
else:
    print ("Berhasil")
a = str (input()) ; a = a +".txt"
b = int (input()) 

try :
    with open (a,"w") as origin :
        origin.write("+------------------+---------------+-------------+"+"\n")
        origin.write("|Nama              |Nim            |Angkatan     |"+"\n")
        origin.write("+------------------+---------------+-------------+"+"\n")

        for i in range(b) :
            nama = input("masukkan nama :")
            nim = input("masukkan nim :")
            angkatan = input("masukkan angkatan :")
            
            if len(nama) >= 20 :
                raise TypeError
            nama = nama.replace(" ","_")
            
            origin.write("|"+nama+" "*(18-len(nama))+"|"+nim+" "*(15-len(nim))+"|"+angkatan+" "*(13-len(angkatan))+"|"+"\n")
    
        origin.write("+------------------+---------------+-------------+")
    print ("\nBerhasil")
except :
    print ("\nGagal")


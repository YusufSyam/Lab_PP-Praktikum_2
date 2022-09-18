print("Masukkan Keinginan:\n1. Cari char berdasarkan nilai / angka ASCII\n2. Cari nilai ASCII dari sebuah char")
jawaban= input("=> ")


if(jawaban=="1"): print("Char = {}".format(chr(int(input("Masukkan angka ASCII: ")))))
elif(jawaban=="2"):
    try:
        print("Angka Ascii = {}".format(ord(input("Masukkan char: "))))
    except:
        print("Input Cuma Angka")
else: print("Input salah")


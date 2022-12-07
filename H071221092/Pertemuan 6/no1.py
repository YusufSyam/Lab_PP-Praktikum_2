a = input () + ".txt"
b = input () + ".txt"

try:
    with open (a, "r") as file:
        baca = file.read()
except:
    print ('Tidak berhasil')
else:
    with open (b, "w") as copy:
        copy.write(baca)
    print ('Berhasil')
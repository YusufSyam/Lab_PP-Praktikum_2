data = int(input("Masukkan detik: "))
jam = data//3600
sisa = data % 3600 
menit = sisa //60
detik = sisa % 60

print("%s : %s : %s" % (jam,menit,detik))

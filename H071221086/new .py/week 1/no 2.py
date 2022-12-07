#konversi detik ke jam

data = int(input('masukkan detik: '))
jam = data//3600
sisa = data % 3600
menit = sisa // 60
detik = sisa % 60

print("%d jam %d menit %d detik" % (jam,menit,detik))
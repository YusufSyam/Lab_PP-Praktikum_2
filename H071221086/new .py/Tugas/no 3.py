# Konversi detik ke jam
'''Nim= H071221086'''
a= 8
b= 6
detik= ((1000*a)+(100*b)-(10*a))
print(detik)

data = int(input("masukkan detik: "))
jam = data //3600
sisa = data % 3600
menit = sisa // 60
detik = sisa % 60

print("%d jam %d menit %d detik" % (jam,menit,detik))
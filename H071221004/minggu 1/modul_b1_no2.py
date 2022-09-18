print('=====Program Konversi Detik Ke Jam=====')
detik = int(input('Masukkan Jumlah detik yang ingin di konversi : '))
 
jam = detik//3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
Detik = sisa_detik % 60

print(jam ,':' , menit , ':' , Detik)
derajat = 360
satu_hari = 3600*24

perbandingan = satu_hari/derajat

n = float(input("n :"))
hasil_detik = (6*3600) + n*perbandingan

if hasil_detik > (3600*24):
    hasil_detik %= (3600*24)

jam = int (hasil_detik // 3600)
menit = int( (hasil_detik - (jam*3600))// 60)
detik = int (hasil_detik -jam*3600 - (menit*60))

if jam <= 6 and jam <= 12 :
    print ("selamat pagi")
if jam > 12 and jam <= 15 :
    print ("selamat siang")
if jam > 15 and jam <= 18 :
    print ("selamat sore")
if jam > 18 and jam <= 24 :
    print ("selamat malam")

print (f'{jam:02d}:{menit:02d}:{detik:02d}')
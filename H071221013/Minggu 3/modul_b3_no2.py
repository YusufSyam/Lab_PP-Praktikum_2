n= float(input(" "))
satu_hari= 3600*24
derajat= 360

perbandingan= satu_hari/derajat 


hasil_detik= (6*3600) + n*perbandingan
if hasil_detik>(3600*24):
    hasil_detik%= (3600*24)

jam= int(hasil_detik//3600)
menit= int( (hasil_detik-(jam*3600))//60)
detik= int(hasil_detik-(jam*3600)-(menit*60))

if jam>=6 and jam<12:
    print('Selamat Pagi')
elif jam>=12 and jam<=15:
    print('Selamat Siang')
elif jam>=16 and jam<=18:
    print('Selamat Sore')
elif jam>=19 and jam<=24:
    print('Selamat Malam')


print(f'{jam:02d}:{menit:02d}:{detik:02d}')


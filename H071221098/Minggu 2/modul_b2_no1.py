nilai = int(input('masukkan nilai dalam angka 1-100: '))

hasil = None
if nilai <= 100 and nilai > 90:
    hasil = 'A'
elif nilai <= 90 and nilai > 80:
    hasil = 'B'
elif nilai <= 80 and nilai > 70:
    hasil = 'C'
elif nilai <= 70 and nilai > 60:
    hasil = 'D'
elif nilai <= 60 and nilai > 40:
    hasil = 'E'
elif nilai <= 40 and nilai < 40:
    hasil = 'F'
elif nilai <= 900 and nilai > 100:
    hasil = 'Inputan Salah,masukkan nilai 1-100'
else:
    print('inputan salah')
print('Nilai {} = {}'.format(nilai, hasil))
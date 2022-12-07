print('--- Pilih bangun datar ---')
print('1. Kotak')
print('2. Lingkaran')
print('3. Segitiga')
print('4. Belah Ketupat')
print('5. Jajar Genjang')

operasi = int(input('input angka sesuai dengan bangun datar'))

if operasi == 1:
    a = int(input('masukkan nilai sisi: '))
    print(a * a)
elif operasi == 2:
    a = int(input('masukkan nilai jari-jari: '))
    print(3.14 * (a * a))
elif operasi == 3:
    a = int(input('masukkan nilai alas: '))
    b = int(input('masukkan nilai tinggi: '))
    print(0.5 * a * b)
elif operasi == 4:
    a = int(input('masukkan nilai d1: '))
    b = int(input('masukkan nilai d2: '))
    print(0.5 * a * b)
elif operasi == 5:
    a = int(input('masukkan nilai alas: '))
    b = int(input('masukkan nilai tinggi: '))
    print(a * b) 
else:
    print('salah input')
    

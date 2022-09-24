print('\n========================')
print(' Program Konversi Nilai ')
print('========================')

nilai = int(input('\nNilai = '))

if nilai>= 90 and nilai<=100:
    print('Nilai', nilai , "= 'A'")
elif nilai >=80 :
    print('Nilai', nilai , "= 'B'")
elif nilai >=70 :
    print('Nilai', nilai , "= 'C'")
elif nilai >=60 :
    print('Nilai', nilai , "= 'D'")
elif nilai >=40 :
    print('Nilai', nilai , "= 'E'")
elif nilai<40 and nilai>=0:
    print('Nilai', nilai , "= 'F'")
elif nilai<0:
    print(nilai,'inputan salah, Masukkan nilai 0-100')
elif nilai>100:
    print(nilai,'Inputan salah, Masukkan nilai 0-100')